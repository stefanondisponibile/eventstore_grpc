"""
Gossip Mixins.
"""

from typing import Optional, List
from eventstore_grpc import gossip
from eventstore_grpc.proto import gossip_pb2, gossip_pb2_grpc


class Gossip:
    """Handles Gossip Operations."""

    def get_cluster_info(self, **kwargs):
        """Gets cluster info."""
        stub = gossip_pb2_grpc.GossipStub(self.channel)
        result = gossip.read(stub, **kwargs)
        return result
