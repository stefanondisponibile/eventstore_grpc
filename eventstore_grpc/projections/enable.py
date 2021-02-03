"""Enable projections."""

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc


def enable_projection(
    stub: projections_pb2_grpc.ProjectionsStub, name: str, **kwargs
) -> projections_pb2.DisableResp:
    """Enables a projection."""
    request = projections_pb2.EnableReq()
    options = projections_pb2.EnableReq.Options()
    options.name = name
    request.options.CopyFrom(options)
    response = stub.Enable(request, **kwargs)
    return response
