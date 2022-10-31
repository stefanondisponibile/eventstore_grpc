"""Replay parked messages for a persistent subscription."""

from eventstore_grpc.proto import persistent_pb2, persistent_pb2_grpc, shared_pb2
from typing import Optional


def replay_parked(
    stub: persistent_pb2_grpc.PersistentSubscriptionsStub,
    group_name: str,
    stream_name: Optional[str] = None,
    stop_at: Optional[int] = None,
    **kwargs,
) -> persistent_pb2.ReplayParkedResp:
    """Gets info about a persistent subscription."""
    options = persistent_pb2.ReplayParkedReq.Options(group_name=group_name)
    if stream_name is None:  # $all
        options.all.CopyFrom(shared_pb2.Empty())
    else:
        options.stream_identifier.CopyFrom(
            shared_pb2.StreamIdentifier(stream_name=stream_name.encode())
        )
    if stop_at is not None:
        options.stop_at = stop_at
    else:
        options.no_limit.CopyFrom(shared_pb2.Empty())
    request = persistent_pb2.ReplayParkedReq(options=options)
    response = stub.ReplayParked(request, **kwargs)
    return response
