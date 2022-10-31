"""
Gossip Cluster Options.
"""

import dataclasses
from typing import List

from eventstore_grpc import options


@dataclasses.dataclass
class GossipClusterOptions(options.ClientOptions, options.DiscoveryOptions):
    endpoints: List[str]
