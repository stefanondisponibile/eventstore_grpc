"""
Create continuous projection.
"""

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc


def create_continuous_projection(
    stub: projections_pb2_grpc.ProjectionsStub,
    name: str,
    query: str,
    track_emitted_streams: bool = False,
    **kwargs,
) -> projections_pb2.CreateResp:
    """Creates a continuous projection."""
    request = projections_pb2.CreateReq()
    options = projections_pb2.CreateReq.Options()
    continuous = projections_pb2.CreateReq.Options.Continuous()
    continuous.name = name
    continuous.track_emitted_streams = track_emitted_streams
    options.continuous.CopyFrom(continuous)
    options.query = query
    request.options.CopyFrom(options)
    response = stub.Create(request, **kwargs)
    return response