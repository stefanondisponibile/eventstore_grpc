"""
Merge Indexes.
"""

from eventstore_grpc.proto import operations_pb2, operations_pb2_grpc, shared_pb2


def merge_indexes(
    stub: operations_pb2_grpc.OperationsStub, **kwargs
) -> shared_pb2.Empty:
    """Merge Indexes."""
    return stub.MergeIndexes(shared_pb2.Empty(), **kwargs)
