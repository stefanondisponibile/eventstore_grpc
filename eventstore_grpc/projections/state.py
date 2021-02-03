"""Get projection states."""

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc


def get_projection_state(
    stub: projections_pb2_grpc.ProjectionsStub, name: str, **kwargs
) -> projections_pb2.StateResp:
    """Gets a projection's state."""
    request = projections_pb2.StateReq()
    options = projections_pb2.StateReq.Options()
    options.name = name
    request.options.CopyFrom(options)
    response = stub.State(request, **kwargs)
    return response
