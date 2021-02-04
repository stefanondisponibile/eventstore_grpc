"""List projections."""

from typing import Iterable
from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc, shared_pb2


def list_continuous_projections(
    stub: projections_pb2_grpc.ProjectionsStub, **kwargs
) -> Iterable[projections_pb2.StatisticsResp]:
    """Lists continuous projections."""
    request = projections_pb2.StatisticsReq()
    options = options.continuous.CopyFrom(shared_pb2.Empty())
    request.options.CopyFrom(options)
    response = stub.Statistics(request, **kwargs)
    return response


def list_one_time_projections(
    stub: projections_pb2_grpc.ProjectionsStub, **kwargs
) -> Iterable[projections_pb2.StatisticsResp]:
    """Lists one time projections."""
    request = projections_pb2.StatisticsReq()
    options = projections_pb2.StatisticsReq.Options()
    options.one_time = shared_pb2.Empty()
    request.options.CopyFrom(options)
    response = stub.Statistics(request, **kwargs)
    return response


def list_transient_projections(
    stub: projections_pb2_grpc.ProjectionsStub, **kwargs
) -> Iterable[projections_pb2.StatisticsResp]:
    """Lists transient projections."""
    request = projections_pb2.StatisticsReq()
    options = projections_pb2.StatisticsReq.Options()
    options.transient.CopyFrom(shared_pb2.Empty())
    request.options.CopyFrom(options)
    response = stub.Statistics(request, **kwargs)
    return response
