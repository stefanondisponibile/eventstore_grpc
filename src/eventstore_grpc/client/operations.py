"""
Operations Mixins.
"""

from eventstore_grpc import operations
from eventstore_grpc.proto import operations_pb2, operations_pb2_grpc, shared_pb2
from eventstore_grpc.core import ClientBase


class Operations(ClientBase):
    """Handles Operations."""

    def merge_indexes(self, **kwargs) -> shared_pb2.Empty:
        """Merges indexes."""
        stub = operations_pb2_grpc.OperationsStub(self.channel)
        result = operations.merge_indexes(stub, **kwargs)
        return result

    def resign_node(self, **kwargs) -> shared_pb2.Empty:
        """Resigns node."""
        stub = operations_pb2_grpc.OperationsStub(self.channel)
        result = operations.resign_node(stub, **kwargs)
        return result

    def restart_persistent_subscriptions(self, **kwargs) -> shared_pb2.Empty:
        """Restarts persistent subscriptions."""
        stub = operations_pb2_grpc.OperationsStub(self.channel)
        result = operations.restart_persistent_subscriptions(stub, **kwargs)
        return result

    def set_node_priority(self, priority: int, **kwargs) -> shared_pb2.Empty:
        """Sets node priority.
        
        Args:
            priority: the priority level for the node you're currently connected to.
        """
        stub = operations_pb2_grpc.OperationsStub(self.channel)
        result = operations.set_node_priority(stub, priority, **kwargs)
        return result

    def shutdown(self, **kwargs) -> shared_pb2.Empty:
        """Shuts the node down."""
        stub = operations_pb2_grpc.OperationsStub(self.channel)
        result = operations.shutdown(stub, **kwargs)
        return result

    def start_scavenge(
        self, thread_count: int, start_from_chunk: int, **kwargs
    ) -> operations_pb2.ScavengeResp:
        """Starts a scavenge operation."""
        stub = operations_pb2_grpc.OperationsStub(self.channel)
        result = operations.start_scavenge(
            stub, thread_count=thread_count, start_from_chunk=start_from_chunk, **kwargs
        )
        return result

    def stop_scavenge(self, scavenge_id: str, **kwargs) -> operations_pb2.ScavengeResp:
        """Stops a scavenge operation."""
        stub = operations_pb2_grpc.OperationsStub(self.channel)
        result = operations.stop_scavenge(stub, scavenge_id=scavenge_id, **kwargs)
        return result
