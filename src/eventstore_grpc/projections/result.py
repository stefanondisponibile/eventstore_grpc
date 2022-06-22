"""Get projection results."""

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc


def get_projection_result(
    stub: projections_pb2_grpc.ProjectionsStub,
    name: str,
    from_partition: str = None,
    **kwargs
) -> projections_pb2.ResultResp:
    """Gets a projection result."""
    request = projections_pb2.ResultReq()
    options = projections_pb2.ResultReq.Options()
    options.name = name
    options.partition = from_partition or ""
    request.options.CopyFrom(options)
    response = stub.Result(request, **kwargs)
    return response
