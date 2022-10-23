"""Create persistent subscription."""

from typing import Union
from eventstore_grpc.proto import persistent_pb2, persistent_pb2_grpc, shared_pb2
from eventstore_grpc import constants


def create_persistent_subscription(
    stub: persistent_pb2_grpc.PersistentSubscriptionsStub,
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
    max_subscriber_count: int = 0,
    live_buffer_size: int = 20,
    history_buffer_size: int = 500,
    strategy: str = "ROUND_ROBIN",
    **kwargs
) -> persistent_pb2.CreateResp:
    """Creates a persistent subscription."""
    request = persistent_pb2.CreateReq()
    options = persistent_pb2.CreateReq.Options()
    identifier = shared_pb2.StreamIdentifier()
    request_settings = persistent_pb2.CreateReq.Settings()
    request_settings.resolve_links = resolve_link_to_s
    if isinstance(from_revision, int):
        request_settings.revision = from_revision
    elif from_revision == constants.START:
        request_settings.revision = 0
    request_settings.extra_statistics = extra_statistics
    request_settings.message_timeout_ms = message_timeout_ms
    request_settings.checkpoint_after_ms = checkpoint_after_ms
    request_settings.max_retry_count = max_retry_count
    request_settings.min_checkpoint_count = min_checkpoint_count
    request_settings.max_checkpoint_count = max_checkpoint_count
    request_settings.max_subscriber_count = max_subscriber_count
    request_settings.live_buffer_size = live_buffer_size
    request_settings.history_buffer_size = history_buffer_size
    if strategy == "DISPATCH_TO_SINGLE":
        request_settings.named_consumer_strategy = (
            persistent_pb2.CreateReq.DispatchToSingle
        )
    elif strategy == "PINNED":
        request_settings.named_consumer_strategy = persistent_pb2.CreateReq.Pinned
    elif strategy == "ROUND_ROBIN":
        request_settings.named_consumer_strategy = persistent_pb2.CreateReq.RoundRobin
    identifier.stream_name = stream.encode()
    options.group_name = group_name
    options.stream_identifier.CopyFrom(identifier)
    options.settings.CopyFrom(request_settings)
    request.options.CopyFrom(options)
    response = stub.Create(request, **kwargs)
    return response
