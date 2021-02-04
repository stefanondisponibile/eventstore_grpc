"""Subscriptions Manager."""

from typing import Sequence, Optional, Callable, Iterable
from eventstore_grpc.subscription import Subscription


class SubscriptionsManager:
    """A Subscription Manager."""

    def __init__(self):
        self._subscriptions = {}

    @property
    def subscriptions(self):
        return [elm for elm in self._subscriptions.keys()]

    def subscribe(self, stream_name: str, stream: Iterable, handler: Callable):
        """Subscribes to a stream."""
        if stream_name in self._subscriptions:
            raise ValueError(f"{stream_name} already subscribed.")

        self._subscriptions[stream_name] = Subscription(
            stream=stream, handler=handler, name=stream_name
        )
        self._start_subscription(stream_name)
        return self

    def _start_subscription(self, stream_name: str):
        """Runs the subscription's thread."""
        self._subscriptions[stream_name].subscribed = True
        self._subscriptions[stream_name].start()
        return self

    def unsubscribe(self, stream_name: str):
        """Unsubscribes from a stream."""
        if stream_name not in self._subscriptions:
            raise ValueError(f"Subscription not found: {stream_name}")

        # TODO: Should make a grpc call here?
        subscription = self._subscriptions.pop(stream_name)
        subscription.subscribed = False
        return self
