"""
Persistents Mixin.
"""

from email import message
from multiprocessing.spawn import prepare
from optparse import Option
from pydoc import resolve
from typing import Optional, Union

from eventstore_grpc import persistent
from eventstore_grpc.constants import END, ROUND_ROBIN
from eventstore_grpc.core import ClientBase
from eventstore_grpc.proto import persistent_pb2, persistent_pb2_grpc

"""
# TODO
we're not covering
GetInfo
ReplayParked
List
RestartSubsystem

that are listed in the `persistent.proto` file.
Also, we need to support creating persistent subscription for the $all stream.
"""


class Persistent(ClientBase):
    """Handles Persistent operations."""

    def create_persistent_subscription(
        self,
        group_name: str = None,
        stream: Optional[str] = None,
        resolve_link_to_s: bool = False,
        from_revision: Union[int, str] = END,
        commit_position: Optional[int] = None,
        prepare_position: Optional[int] = None,
        extra_statistics: bool = False,
        message_timeout_ms: int = 30000,
        checkpoint_after_ms: int = 2000,
        max_retry_count: int = 10,
        min_checkpoint_count: int = 10,
        max_checkpoint_count: int = 1000,
        max_subscriber_count: int = 0,
        live_buffer_size: int = 500,
        history_buffer_size: int = 500,
        read_batch_size: int = 20,
        strategy: str = ROUND_ROBIN,
        filter_options: Optional[
            persistent_pb2.CreateReq.AllOptions.FilterOptions
        ] = None,
        **kwargs
    ) -> persistent_pb2.CreateResp:
        """Creates a new persistent subscription.

        Args:
            group_name: a group name for the subscription that will be created.
            stream: the name of the stream. A persistent subscription to the `$all`
                    stream will be created if this value is left to `None`.
            resolve_link_to_s: whether or not to resolve events links to actual events.
            from_revision: the subscription will start from the revision specified here.
            extra_statistics: whether to track latency statistics on this subscription.
            message_timeout_ms: the amount of time after which to consider a message as
                                timed out and retried.
            checkpoint_after_ms: the amount of time to try to checkpoint after.
            max_retry_count: the maximum number of retries (due to timeout) before a
                             message is considered to be parked.
            min_checkpoint_count: The minimum number of messages to process before a
                                  checkpoint may be written.
            max_checkpoint_count: The maximum number of messages not checkpointed
                                  before forcing a checkpoint.
            max_subscriber_count: The maximum number of subscribers allowed.
            live_buffer_size: the size of the buffer (in-memory) listening to live
                              messages as they happen before pagin occurs.
            history_buffer_size: The number of events to cache when paging through
                                 history.
            read_batch_size: The number of events read at a time when paging through history.
            strategy: the strategy that will be used to send events to the subscribers
                      of the same group.
            filter_options: an optional FilterOptions instance to use to filter events
                            in the persistent subscription.

        Returns:
            A persistent_pb.CreateResp
        """
        stub = persistent_pb2_grpc.PersistentSubscriptionsStub(self.channel)
        result = persistent.create_persistent_subscription(
            stub=stub,
            stream=stream,
            group_name=group_name,
            resolve_link_to_s=resolve_link_to_s,
            from_revision=from_revision,
            commit_position=commit_position,
            prepare_position=prepare_position,
            extra_statistics=extra_statistics,
            message_timeout_ms=message_timeout_ms,
            checkpoint_after_ms=checkpoint_after_ms,
            max_retry_count=max_retry_count,
            min_checkpoint_count=min_checkpoint_count,
            max_checkpoint_count=max_checkpoint_count,
            max_subscriber_count=max_subscriber_count,
            live_buffer_size=live_buffer_size,
            history_buffer_size=history_buffer_size,
            read_batch_size=read_batch_size,
            strategy=strategy,
            filter_options=filter_options,
            **kwargs,
        )
        return result

    def update_persistent_subscription(
        self,
        group_name: Optional[str] = None,
        stream: Optional[str] = None,
        resolve_link_to_s: Optional[bool] = None,
        from_revision: Optional[Union[int, str]] = None,
        commit_position: Optional[int] = None,
        prepare_position: Optional[int] = None,
        extra_statistics: Optional[bool] = None,
        message_timeout_ms: Optional[int] = None,
        checkpoint_after_ms: Optional[int] = None,
        max_retry_count: Optional[int] = None,
        min_checkpoint_count: Optional[int] = None,
        max_checkpoint_count: Optional[int] = None,
        max_subscriber_count: Optional[int] = None,
        live_buffer_size: Optional[int] = None,
        history_buffer_size: Optional[int] = None,
        read_batch_size: Optional[int] = None,
        strategy: Optional[str] = None,
        **kwargs
    ) -> persistent_pb2.UpdateResp:
        """Updates a persistent subscription.

        Args:
            updates: a dictionary that will be parsed into a UpdateReq message proto.
        """
        stub = persistent_pb2_grpc.PersistentSubscriptionsStub(self.channel)
        result = persistent.update_persistent_subscription(
            stub=stub,
            group_name=group_name,
            stream=stream,
            resolve_link_to_s=resolve_link_to_s,
            from_revision=from_revision,
            commit_position=commit_position,
            prepare_position=prepare_position,
            extra_statistics=extra_statistics,
            message_timeout_ms=message_timeout_ms,
            checkpoint_after_ms=checkpoint_after_ms,
            max_retry_count=max_retry_count,
            min_checkpoint_count=min_checkpoint_count,
            max_checkpoint_count=max_checkpoint_count,
            max_subscriber_count=max_subscriber_count,
            live_buffer_size=live_buffer_size,
            history_buffer_size=history_buffer_size,
            read_batch_size=read_batch_size,
            named_consumer_strategy=strategy,
            **kwargs,
        )
        return result

    def delete_persistent_subscription(
        self,
        group: str,
        stream: Optional[str] = None,
    ) -> persistent_pb2.DeleteResp:
        stub = persistent_pb2_grpc.PersistentSubscriptionsStub(self.channel)
        result = persistent.delete_persistent_subscription(
            stub=stub, stream=stream, group=group
        )
        return result

    def get_info(
        self,
        group_name: str,
        stream_name: Optional[str] = None,
    ) -> persistent_pb2.GetInfoResp:
        """Get info about a persistent subscription.

        Args:
            group: a group name to get info about.
            stream_name: the name of the stream, or None if it's some $all persistent
                         subscription.
        """
        stub = persistent_pb2_grpc.PersistentSubscriptionsStub(self.channel)
        result = persistent.get_info(
            stub=stub, group_name=group_name, stream_name=stream_name
        )
        return result

    def replay_parked(
        self,
        group_name: str,
        stream_name: Optional[str] = None,
        stop_at: Optional[int] = None,
    ) -> persistent_pb2.ReplayParkedResp:
        """Replays parked events.

        Args:
            group_name: the group name.
            stream_name: the name of the stream, or None for $all.
            stop_at: the postition at which to stop.
        """
        stub = persistent_pb2_grpc.PersistentSubscriptionsStub(self.channel)
        result = persistent.replay_parked(
            stub=stub, group_name=group_name, stream_name=stream_name, stop_at=stop_at
        )
        return result

    def list_persistent(
        self,
        stream_name: Optional[str] = None,
        list_all: bool = False,
    ) -> persistent_pb2.ListResp:
        """List persistent subscriptions.

        Args:
            stream_name: the name of the stream.
            list_all: whether to list all the persistent subscriptions available.
        """
        stub = persistent_pb2_grpc.PersistentSubscriptionsStub(self.channel)
        results = persistent.list_persistent(
            stub=stub, stream_name=stream_name, list_all=True
        )
        return results
