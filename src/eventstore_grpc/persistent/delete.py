"""Delete persisten subscription."""


from eventstore_grpc.proto import persistent_pb2, persistent_pb2_grpc, shared_pb2


def delete_persistent_subscription(
    stub: persistent_pb2_grpc.PersistentSubscriptionsStub, stream: str, group: str
) -> persistent_pb2.DeleteResp:
    """Deletes a persistent subscription."""
    request = persistent_pb2.DeleteReq()
    options = persistent_pb2.DeleteReq.Options()
    identifier = shared_pb2.StreamIdentifier()
    identifier.streamName = stream.encode()
    options.stream_identifier.CopyFrom(identifier)
    options.group_name = group
    request.options.CopyFrom(options)
    response = stub.Delete(request)
    return response
