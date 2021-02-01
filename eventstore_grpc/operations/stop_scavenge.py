"""
Stop Scavenge.
"""

from eventstore_grpc.proto import operations_pb2, operations_pb2_grpc


def stop_scavenge(
    stub: operations_pb2_grpc.OperationsStub,
    scavenge_id: str,
    **kwargs
) -> operations_pb2.ScavengeResp:
    """Stops scavenge."""
    request = operations_pb2.StopScavengeReq()
    options = operations_pb2.StartScavengeReq.Options()
    options.scavenge_id = scavenge_id
    request.options.CopyFrom(options)
    response = stub.StopScavenge(request, **kwargs)
    return response
