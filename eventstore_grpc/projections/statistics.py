"""Get projections statistics."""

from typing import Iterable
from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc


def get_projection_statistics(
    stub: projections_pb2_grpc.ProjectionsStub, name: str, **kwargs
) -> Iterable[projections_pb2.StatisticsResp]:
    """Get projection statistics."""
    request = projections_pb2.StatisticsReq()
    options = projections_pb2.StatisticsReq.Options()
    options.name = name
    request.options.CopyFrom(options)
    response = stub.Statistics(request, **kwargs)
    return response
