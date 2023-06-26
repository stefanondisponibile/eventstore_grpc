"""Get Info about a persistent subscription."""

from typing import Optional

from eventstore_grpc.proto import persistent_pb2, persistent_pb2_grpc, shared_pb2


def get_info(
    stub: persistent_pb2_grpc.PersistentSubscriptionsStub,
    group_name: str,
    stream_name: Optional[str] = None,
    **kwargs,
) -> persistent_pb2.GetInfoResp:
    """Gets info about a persistent subscription."""
    options = persistent_pb2.GetInfoReq.Options(group_name=group_name)
    if stream_name is None:  # $all
        options.all.CopyFrom(shared_pb2.Empty())
    else:
        options.stream_identifier.CopyFrom(
            shared_pb2.StreamIdentifier(stream_name=stream_name.encode())
        )
    request = persistent_pb2.GetInfoReq(options=options)
    response = stub.GetInfo(request, **kwargs)
    return response
