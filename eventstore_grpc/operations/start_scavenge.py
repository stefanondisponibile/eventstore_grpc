"""
Start Scavenge.
"""

from eventstore_grpc.proto import operations_pb2, operations_pb2_grpc


def start_scavenge(
    stub: operations_pb2_grpc.OperationsStub,
    thread_count: int,
    start_from_chunk: int,
    **kwargs
) -> operations_pb2.ScavengeResp:
    """Starts scavenge."""
    request = operations_pb2.StartScavengeReq()
    options = operations_pb2.StartScavengeReq.Options()
    options.thread_count = thread_count
    options.start_from_chunk = start_from_chunk
    request.options.CopyFrom(options)
    response = stub.StartScavenge(request, **kwargs)
    return response
