"""
Restart persistent subscriptions.
"""

from eventstore_grpc.proto import operations_pb2, operations_pb2_grpc, shared_pb2

def restart_persistent_subscriptions(stub: operations_pb2_grpc.OperationsStub, **kwargs) -> shared_pb2.Empty:
    """Restart persistent subscriptions."""
    return stub.RestartPersistentSubscriptions(shared_pb2.Empty(), **kwargs)
