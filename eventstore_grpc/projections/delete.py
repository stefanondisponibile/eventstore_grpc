"""Delete projections."""

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc


def delete_projection(
    stub: projections_pb2_grpc.ProjectionsStub,
    name: str,
    delete_emitted_streams: bool = True,
    delete_state_stream: bool = True,
    delete_checkpoint_stream: bool = True,
    **kwargs,
) -> projections_pb2.DeleteResp:
    """Deletes a projection."""
    request = projections_pb2.DeleteReq()
    options = projections_pb2.DeleteReq.Options()
    options.name = name
    options.delete_emitted_streams = delete_emitted_streams
    options.delete_state_stream = delete_state_stream
    options.delete_checkpoint_stream = delete_checkpoint_stream
    request.options.CopyFrom(options)
    response = stub.Delete(request, **kwargs)
    return response
