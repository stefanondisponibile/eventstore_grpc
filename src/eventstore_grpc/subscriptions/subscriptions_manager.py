"""Subscriptions Manager.

Dev notes:

There should be 2 different "types" of subscriptions involved:
    1.  OneWay Subscription: the server streams events to the client, which handles them.
    2.  TwoWay Subscription: the server streams events to the client, which handles them *and*
        tells back the server which events to consider acknowledged and which ones not.

In both cases, there should be some mechanism for the client to cancel the gRPC call.
If this can be controlled by the user of the library, this means that the channel (or the stub)
must be reachable from inside the thread. This shouldn't be a problem, since both grpc channels
and stubs should be thread-safe: https://github.com/grpc/grpc/issues/9320

In both cases, the library's user must control over what he can do with an event, probably
by providing a callback to invoke within the thread (streaming) loop.

In case of the TwoWay Subscription, we could consider instructing the library's user to
raise a specific Exception carrying the information to complete the Nack request, or provide
a default mechanism in case of different exceptions.
"""

from __future__ import annotations

import logging
import uuid
from typing import Callable, Dict, Optional, Union
from uuid import UUID

import grpc

from eventstore_grpc import constants, persistent, streams
from eventstore_grpc.proto import persistent_pb2_grpc, streams_pb2_grpc
from eventstore_grpc.subscriptions.requests_stream import RequestsStream
from eventstore_grpc.subscriptions.subscription import Subscription

log = logging.getLogger(__name__)


class SubscriptionsManager:
    """A Subscription Manager."""

    def __init__(self, channel: grpc.Channel):
        self._registry: dict[str, Subscription] = {}
        self._channel = channel
        self._streams_stub = streams_pb2_grpc.StreamsStub(self._channel)
        self._persistent_stub = persistent_pb2_grpc.PersistentSubscriptionsStub(
            self._channel
        )

    @property
    def subscription_ids(self):
        return [elm for elm in self._registry.keys()]

    def subscribe(
        self,
    ):
        raise NotImplementedError

    def register(
        self, subscription: Subscription, id_: str | UUID | None = None
    ) -> str:
        """Registers a subscription to the registry."""
        id_ = id_ or uuid.uuid4()

        if id_ in self._registry:
            raise ValueError(f"Already Registered: {id_}")

        self._registry[str(id_)] = subscription
        return str(id_)

    def subscribe_to_stream(
        self,
        stream: str,
        from_revision: Union[str, int] = constants.START,
        resolve_link_to_s: bool = False,
        handler: Optional[Callable] = None,
        **kwargs,
    ):
        # Create a requests stream.
        request = streams.get_stream_subscription_request(
            stream=stream,
            from_revision=from_revision,
            resolve_link_to_s=resolve_link_to_s,
        )
        requests_stream = RequestsStream(handler=handler, queue=[request])
        # Create a new Subscription object.
        stub = self._streams_stub
        subscription = Subscription(
            requests_stream=requests_stream,
            stub=stub,
            manager=self,
            name=stream,
            **kwargs,
        )
        # Register the object to the manager.
        subscription_id = self.register(subscription, id_=stream)
        # Run it.
        subscription.start()
        return subscription_id

    def subscribe_to_all(
        self,
        from_position: str | dict[str, int] = constants.START,
        resolve_link_to_s: bool = False,
        filters: Optional[Dict] = None,
        handler: Optional[Callable] = None,
        **kwargs,
    ):
        # Create a requests stream.
        request = streams.get_all_subscription_request(
            from_position=from_position,
            resolve_link_to_s=resolve_link_to_s,
            filters=filters,
        )
        requests_stream = RequestsStream(handler=handler, queue=[request])
        # Create a new Subscription object.
        stub = self._streams_stub
        name = "$all"
        subscription = Subscription(
            requests_stream=requests_stream,
            stub=stub,
            manager=self,
            name=name,
            **kwargs,
        )
        # Register the object to the manager.
        subscription_id = self.register(subscription, id_=name)
        # Run it.
        subscription.start()
        return subscription_id

    def subscribe_persistent(
        self,
        stream: str,
        group_name: str,
        buffer_size: int = 10,
        handler: Optional[Callable] = None,
        **kwargs,
    ):
        # Create a requests stream.
        request = persistent.options_request(
            stream=stream, group_name=group_name, buffer_size=buffer_size
        )
        requests_stream = RequestsStream(
            handler=handler, queue=[request], persistent=True
        )
        # Create a new Subscription object.
        stub = self._persistent_stub
        name = f"{stream}-{group_name}"
        subscription = Subscription(
            requests_stream=requests_stream,
            stub=stub,
            manager=self,
            name=name,
            **kwargs,
        )
        # Register the object to the manager.
        subscription_id = self.register(subscription, id_=name)
        # Run it.
        subscription.start()
        return subscription_id

    def unsubscribe(self, stream_name: str, timeout: int = 5):
        """Unsubscribes from a stream."""
        if stream_name not in self._registry:
            log.error(f"Subscription not found: {stream_name}")
            return None

        subscription: Subscription = self._registry.pop(stream_name)
        subscription.revoke()
        log.info("\033[38;5;190mSubscription revoked.\033[0m")
        return subscription.join(timeout=timeout)
