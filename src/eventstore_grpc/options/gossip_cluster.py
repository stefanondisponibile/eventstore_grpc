"""
Gossip Cluster Options.
"""

from typing import List
import dataclasses
from eventstore_grpc import options


@dataclasses.dataclass
class GossipClusterOptions(options.ClientOptions, options.DiscoveryOptions):
    endpoints: List[str]
