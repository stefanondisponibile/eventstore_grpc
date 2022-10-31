"""List persistent subscriptions."""

from typing import Optional

from eventstore_grpc.proto import persistent_pb2, persistent_pb2_grpc, shared_pb2


def list_persistent(
    stub: persistent_pb2_grpc.PersistentSubscriptionsStub,
    stream_name: Optional[str] = None,
    list_all: bool = False,
    **kwargs,
) -> persistent_pb2.ReplayParkedResp:
    """Lists persistent subscriptions."""
    options = persistent_pb2.ListReq.Options()
    if not list_all:
        stream_option = persistent_pb2.ListReq.StreamOption()
        if stream_name is not None:
            stream_option.stream.CopyFrom(
                shared_pb2.StreamIdentifier(stream_name=stream_name.encode())
            )
        else:
            stream_option.all.CopyFrom(shared_pb2.Empty())
        options.list_for_stream.CopyFrom()
    else:
        options.list_all_subscriptions.CopyFrom(shared_pb2.Empty())
    request = persistent_pb2.ListReq(options=options)
    response = stub.ReplayParked(request, **kwargs)
    return response
