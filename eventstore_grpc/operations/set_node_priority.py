"""
Set Node Priority.
"""

from eventstore_grpc.proto import operations_pb2, operations_pb2_grpc, shared_pb2


def set_node_priority(stub: operations_pb2_grpc.OperationsStub, priority: int, **kwargs) -> shared_pb2.Empty():
    """Sets node priority."""
    request = operations_pb2.SetNodePriorityReq()
    request.priority = priority
    response = stub.SetNodePriority(request, **kwargs)
    return response
