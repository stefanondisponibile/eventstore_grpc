"""
Create transient projection.
"""

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc, shared_pb2


def create_transient_projection(
    stub: projections_pb2_grpc.ProjectionsStub,
    name: str,
    query: str,
    **kwargs,
) -> projections_pb2.CreateResp:
    """Creates a one time projection."""
    request = projections_pb2.CreateReq()
    options = projections_pb2.CreateReq.Options()
    transient = projections_pb2.CreateReq.Options.Transient()
    transient.name = name
    options.transient.CopyFrom(transient)
    options.query = query
    request.options.CopyFrom(options)
    response = stub.Create(request, **kwargs)
    return response
