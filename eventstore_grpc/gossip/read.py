"""
Read Gossip.
"""

from eventstore_grpc.proto import gossip_pb2, gossip_pb2_grpc, shared_pb2


def read(stub: gossip_pb2_grpc.GossipStub, **kwargs) -> gossip_pb2.ClusterInfo:
    """Reads Gossip."""
    return stub.Read(shared_pb2.Empty())
