"""Reset projections."""

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc


def reset_projection(
    stub: projections_pb2_grpc.ProjectionsStub, name: str, write_checkpoint: bool = True, **kwargs
) -> projections_pb2.ResetResp:
    """Resets a projection."""
    request = projections_pb2.ResetReq()
    options = projections_pb2.ResetReq.Options()
    options.name = name
    options.write_checkpoint = write_checkpoint
    request.options.CopyFrom(options)
    response = stub.Reset(request, **kwargs)
    return response
