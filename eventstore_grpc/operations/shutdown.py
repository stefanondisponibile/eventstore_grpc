"""
Shutdown.
"""

from eventstore_grpc.proto import operations_pb2, operations_pb2_grpc, shared_pb2

def shutdown(stub: operations_pb2_grpc.OperationsStub, **kwargs) -> shared_pb2.Empty:
    """Shuts down EvenStoreDB."""
    return stub.Shutdown(shared_pb2.Empty(), **kwargs)
