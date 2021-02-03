"""Disable projections."""

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc


def disable_projection(
    stub: projections_pb2_grpc.ProjectionsStub,
    name: str,
    write_checkpoint: bool = True,
    **kwargs
) -> projections_pb2.DisableResp:
    """Disables a projection."""
    request = projections_pb2.DisableReq()
    options = projections_pb2.DisableReq.Options()
    options.name = name
    options.write_checkpoint = write_checkpoint
    request.options.CopyFrom(options)
    response = stub.Disable(request, **kwargs)
    return response
