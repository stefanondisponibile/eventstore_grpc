"""
DNS Cluster Options.
"""

import dataclasses
from eventstore_grpc import options


@dataclasses.dataclass
class DNSClusterOptions(options.ClientOptions, options.DiscoveryOptions):
    discover: str
