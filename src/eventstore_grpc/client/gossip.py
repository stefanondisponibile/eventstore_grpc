"""
Gossip Mixins.
"""

from eventstore_grpc import gossip
from eventstore_grpc.proto.gossip_pb2 import ClusterInfo
from eventstore_grpc.proto import gossip_pb2_grpc
from eventstore_grpc.core import ClientBase


class Gossip(ClientBase):
    """Handles Gossip Operations."""

    def get_cluster_info(self, **kwargs) -> ClusterInfo:
        """Gets cluster info."""
        stub = gossip_pb2_grpc.GossipStub(self.channel)
        result = gossip.read(stub, **kwargs)
        return result
