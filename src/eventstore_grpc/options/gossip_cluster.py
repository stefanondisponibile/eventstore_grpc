"""
Gossip Cluster Options.
"""

import dataclasses
from typing import List

from eventstore_grpc.options.client import ClientOptions
from eventstore_grpc.options.discovery import DiscoveryOptions


@dataclasses.dataclass
class GossipClusterOptions(ClientOptions, DiscoveryOptions):
    endpoints: List[str]
