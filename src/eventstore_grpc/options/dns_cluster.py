"""
DNS Cluster Options.
"""

import dataclasses

from eventstore_grpc.options.client import ClientOptions
from eventstore_grpc.options.discovery import DiscoveryOptions


@dataclasses.dataclass
class DNSClusterOptions(ClientOptions, DiscoveryOptions):
    discover: str
