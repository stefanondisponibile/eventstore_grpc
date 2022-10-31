"""Delete persisten subscription."""

from typing import Optional
from eventstore_grpc.proto import persistent_pb2, persistent_pb2_grpc, shared_pb2


def delete_persistent_subscription(
    stub: persistent_pb2_grpc.PersistentSubscriptionsStub,
    group: str,
    stream: Optional[str] = None,
) -> persistent_pb2.DeleteResp:
    """Deletes a persistent subscription."""
    request = persistent_pb2.DeleteReq()
    options = persistent_pb2.DeleteReq.Options()
    if stream is not None:
        identifier = shared_pb2.StreamIdentifier()
        identifier.stream_name = stream.encode()
        options.stream_identifier.CopyFrom(identifier)
    else:  # $all
        options.all.CopyFrom(shared_pb2.Empty())
    options.group_name = group
    request.options.CopyFrom(options)
    response = stub.Delete(request)
    return response
