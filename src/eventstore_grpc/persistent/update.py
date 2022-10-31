"""Update persistent subscription."""

from eventstore_grpc.proto import persistent_pb2, persistent_pb2_grpc, shared_pb2
from typing import Optional, Union
from eventstore_grpc.constants import (
    ROUND_ROBIN,
    PINNED,
    DISPATCH_TO_SINGLE,
    START,
    END,
)
import logging

log = logging.getLogger(__name__)


def _build_options_all(
    commit_position: Optional[int] = None,
    prepare_position: Optional[int] = None,
    from_revision: Union[int, str] = None,
) -> persistent_pb2.UpdateReq.AllOptions:
    """Builds option for persistent subscription creation to the $all stream."""
    options = persistent_pb2.UpdateReq.AllOptions()
    if commit_position is not None and prepare_position is not None:
        position = persistent_pb2.UpdateReq.Position(
            commit_position=commit_position, prepare_position=prepare_position
        )
        options.position.CopyFrom(position)
    elif isinstance(from_revision, str):
        if from_revision.lower() == START.lower():
            options.start.CopyFrom(shared_pb2.Empty())
        elif from_revision.lower() == END.lower():
            options.end.CopyFrom(shared_pb2.Empty())
    elif isinstance(from_revision, int):
        raise ValueError(
            f"Invalid value for 'from_revision': {from_revision} (can't be `int`, you must specify commit and prepare position for $all)"
        )
    return options


def _build_options_stream(
    stream: str,
    from_revision: Union[int, str],
) -> persistent_pb2.UpdateReq.StreamOptions:
    """Builds option for persistent subscription creation to some stream."""
    options = persistent_pb2.UpdateReq.StreamOptions(
        stream_identifier=shared_pb2.StreamIdentifier(stream_name=stream.encode())
    )
    if isinstance(from_revision, int):
        options.revision = from_revision
    elif isinstance(from_revision, str):
        if from_revision.lower() == START.lower():
            options.start.CopyFrom(shared_pb2.Empty())
        elif from_revision.lower() == END.lower():
            options.end.CopyFrom(shared_pb2.Empty())
        else:
            raise ValueError(f"Invalid revision: {from_revision}")
    return options


def _build_settings(
    resolve_link_to_s: Optional[bool] = None,
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
    named_consumer_strategy: Optional[str] = None,
) -> persistent_pb2.UpdateReq.Settings:
    settings = persistent_pb2.UpdateReq.Settings()
    if resolve_link_to_s is not None:
        settings.resolve_links = resolve_link_to_s
    if extra_statistics is not None:
        settings.extra_statistics = extra_statistics
    if max_retry_count is not None:
        settings.max_retry_count = max_retry_count
    if min_checkpoint_count is not None:
        settings.min_checkpoint_count = min_checkpoint_count
    if max_checkpoint_count is not None:
        settings.max_checkpoint_count = max_checkpoint_count
    if max_subscriber_count is not None:
        settings.max_subscriber_count = max_subscriber_count
    if live_buffer_size is not None:
        settings.live_buffer_size = live_buffer_size
    if read_batch_size is not None:
        settings.read_batch_size = read_batch_size
    if history_buffer_size is not None:
        settings.history_buffer_size = history_buffer_size
    if message_timeout_ms is not None:
        settings.message_timeout_ms = message_timeout_ms
    if checkpoint_after_ms is not None:
        settings.checkpoint_after_ms = checkpoint_after_ms
    if named_consumer_strategy is not None:
        if named_consumer_strategy.lower() == ROUND_ROBIN.lower():
            settings.named_consumer_strategy = (
                persistent_pb2.UpdateReq.ConsumerStrategy.RoundRobin
            )
        elif named_consumer_strategy.lower() == PINNED.lower():
            settings.named_consumer_strategy = (
                persistent_pb2.UpdateReq.ConsumerStrategy.Pinned
            )
        elif named_consumer_strategy.lower() == DISPATCH_TO_SINGLE.lower():
            settings.named_consumer_strategy = (
                persistent_pb2.UpdateReq.ConsumerStrategy.DispatchToSingle
            )
        else:
            raise ValueError(f"Invalid consumer strategy: {named_consumer_strategy}")
    return settings


def update_persistent_subscription(
    stub: persistent_pb2_grpc.PersistentSubscriptionsStub,
    group_name: str,
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
    named_consumer_strategy: Optional[str] = None,
    **kwargs,
) -> persistent_pb2.UpdateResp:
    """Updates a persistent subscription."""

    if history_buffer_size is None:
        # TODO: talk with EventStoreDB about this behavior?
        log.warning(
            f"If you don't send `history_buffer_size` EventStoreDB will hang indefinitely: forcing it to its default value -> 500"
        )
        history_buffer_size = 500
    settings = _build_settings(
        resolve_link_to_s=resolve_link_to_s,
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
        named_consumer_strategy=named_consumer_strategy,
    )
    options = persistent_pb2.UpdateReq.Options(settings=settings, group_name=group_name)
    if stream is None:  # $all
        options.all.CopyFrom(
            _build_options_all(
                commit_position=commit_position,
                prepare_position=prepare_position,
                from_revision=from_revision,
            )
        )
    else:
        options.stream.CopyFrom(
            _build_options_stream(stream=stream, from_revision=from_revision)
        )
    request = persistent_pb2.UpdateReq(options=options)
    response = stub.Update(request, **kwargs)
    return response
