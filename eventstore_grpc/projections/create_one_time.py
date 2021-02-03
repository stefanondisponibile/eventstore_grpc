"""
Create one time projection.
"""

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc, shared_pb2


def create_one_time_projection(
    stub: projections_pb2_grpc.ProjectionsStub,
    query: str,
    track_emitted_streams: bool = False,
    **kwargs,
) -> projections_pb2.CreateResp:
    """Creates a one time projection."""
    request = projections_pb2.CreateReq()
    options = projections_pb2.CreateReq.Options()
    options.query = query
    options.one_time.CopyFrom(shared_pb2.Empty())
    request.options.CopyFrom(options)
    response = stub.Create(request, **kwargs)
    return response
