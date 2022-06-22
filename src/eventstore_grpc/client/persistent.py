"""
Persistents Mixin.
"""

from typing import Union
from eventstore_grpc import constants, persistent
from eventstore_grpc.proto import persistent_pb2, persistent_pb2_grpc
from eventstore_grpc.core import ClientBase


class Persistent(ClientBase):
    """Handles Persistent operations."""

    def create_persistent_subscription(
        self,
        stream: str,
        group_name: str,
        resolve_link_to_s: bool = False,
        from_revision: Union[int, str] = constants.START,
        extra_statistics: bool = False,
        message_timeout_ms: int = 30000,
        checkpoint_after_ms: int = 2000,
        max_retry_count: int = 10,
        min_checkpoint_count: int = 10,
        max_checkpoint_count: int = 1000,
        max_subscriber_count: Union[str, int] = 0,
        live_buffer_size: int = 20,
        history_buffer_size: int = 500,
        strategy: str = "ROUND_ROBIN",
        **kwargs
    ) -> persistent_pb2.CreateResp:
        stub = persistent_pb2_grpc.PersistentSubscriptionsStub(self.channel)
        result = persistent.create_persistent_subscription(
            stub=stub,
            stream=stream,
            group_name=group_name,
            resolve_link_to_s=resolve_link_to_s,
            from_revision=from_revision,
            extra_statistics=extra_statistics,
            message_timeout_ms=message_timeout_ms,
            checkpoint_after_ms=checkpoint_after_ms,
            max_retry_count=max_retry_count,
            min_checkpoint_count=min_checkpoint_count,
            max_checkpoint_count=max_checkpoint_count,
            max_subscriber_count=max_subscriber_count,
            live_buffer_size=live_buffer_size,
            history_buffer_size=history_buffer_size,
            strategy=strategy,
            **kwargs,
        )
        return result

    def update_persistent_subscription(
        self,
        resolve_link_to_s: bool = False,
        from_revision: Union[str, int] = constants.START,
        extra_statistics: bool = False,
        message_timeout_ms: int = 30000,
        checkpoint_after_ms: int = 2000,
        max_retry_count: int = 10,
        min_checkpoint_count: int = 10,
        max_checkpoint_count: int = 1000,
        max_subscriber_count: Union[str, int] = 0,
        live_buffer_size: int = 20,
        history_buffer_size: int = 500,
        strategy: str = "ROUND_ROBIN",
        **kwargs
    ) -> persistent_pb2.UpdateResp:
        stub = persistent_pb2_grpc.PersistentSubscriptionsStub(self.channel)
        result = persistent.update_persistent_subscription(
            stub,
            resolve_link_to_s=resolve_link_to_s,
            from_revision=from_revision,
            extra_statistics=extra_statistics,
            message_timeout_ms=message_timeout_ms,
            checkpoint_after_ms=checkpoint_after_ms,
            max_retry_count=max_retry_count,
            min_checkpoint_count=min_checkpoint_count,
            max_checkpoint_count=max_checkpoint_count,
            max_subscriber_count=max_subscriber_count,
            live_buffer_size=live_buffer_size,
            history_buffer_size=history_buffer_size,
            strategy=strategy,
            **kwargs,
        )
        return result

    def delete_persistent_subscription(
        self, stream: str, group: str
    ) -> persistent_pb2.DeleteResp:
        stub = persistent_pb2_grpc.PersistentSubscriptionsStub(self.channel)
        result = persistent.delete_persistent_subscription(
            stub=stub, stream=stream, group=group
        )
        return result
