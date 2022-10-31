"""Update projections."""

from typing import Optional

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc, shared_pb2


def update_projection(
    stub: projections_pb2_grpc.ProjectionsStub,
    name: str,
    query: str,
    track_emitted_streams: Optional[bool] = None,
    **kwargs,
) -> projections_pb2.UpdateResp:
    """Updates a projection."""
    request = projections_pb2.UpdateReq()
    options = projections_pb2.UpdateReq.Options()
    options.name = name
    options.query = query
    if track_emitted_streams is None:
        options.no_emit_options.CopyFrom(shared_pb2.Empty())
    else:
        options.emit_enabled = track_emitted_streams
    request.options.CopyFrom(options)
    response = stub.Update(request, **kwargs)
    return response
