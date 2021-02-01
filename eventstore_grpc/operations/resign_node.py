"""
Resign Node.
"""

from eventstore_grpc.proto import operations_pb2, operations_pb2_grpc, shared_pb2

def resign_node(stub: operations_pb2_grpc.OperationsStub, **kwargs) -> shared_pb2.Empty:
    """Resign Node."""
    return stub.ResignNode(shared_pb2.Empty(), **kwargs)
