"""
Subscriptions Mixin.
"""

from typing import Union, Optional, Dict, Callable
from eventstore_grpc import constants, subscriptions
import signal
from eventstore_grpc.core import ClientBase


class Subscriptions(ClientBase):
    """Handles Subscriptions operations."""

    def _initialize_subscriptions_manager(self):
        if getattr(self, "_subscriptions_manager", None) is None:
            self._subscriptions_manager = subscriptions.SubscriptionsManager(
                self.channel
            )
            signal.signal(signal.SIGINT, self.kill)
            signal.signal(signal.SIGTERM, self.kill)

    def kill(self, signum, frame):
        print("\033[38;5;120mGracefully shutting down...\033[0m")
        self.unsubscribe_all()

    def subscribe_to_stream(
        self,
        stream: str,
        from_revision: Union[str, int] = constants.START,
        resolve_link_to_s: bool = False,
        handler: Optional[Callable] = None,
        **kwargs,
    ):
        self._initialize_subscriptions_manager()
        subscription_id = self._subscriptions_manager.subscribe_to_stream(
            stream=stream,
            from_revision=from_revision,
            resolve_link_to_s=resolve_link_to_s,
            handler=handler,
            **kwargs,
        )
        return subscription_id

    def subscribe_to_all(
        self,
        from_position: Union[str, int] = constants.START,
        resolve_link_to_s: bool = False,
        filters: Optional[Dict] = None,
        handler: Optional[Callable] = None,
        **kwargs,
    ):
        self._initialize_subscriptions_manager()
        subscription_id = self._subscriptions_manager.subscribe_to_all(
            from_position=from_position,
            resolve_link_to_s=resolve_link_to_s,
            filters=filters,
            handler=handler,
            **kwargs,
        )
        return subscription_id

    def subscribe_persistent(
        self,
        stream: str,
        group_name: str,
        buffer_size: int = 10,
        handler: Optional[Callable] = None,
        **kwargs,
    ):
        self._initialize_subscriptions_manager()
        subscription_id = self._subscriptions_manager.subscribe_persistent(
            stream=stream,
            group_name=group_name,
            buffer_size=buffer_size,
            handler=handler,
            **kwargs,
        )
        return subscription_id

    def unsubscribe(self, subscription_id: str):
        self._initialize_subscriptions_manager()
        return self._subscriptions_manager.unsubscribe(subscription_id)

    def unsubscribe_all(self):
        self._initialize_subscriptions_manager()
        for k in self._subscriptions_manager.subscription_ids:
            self.unsubscribe(k)
