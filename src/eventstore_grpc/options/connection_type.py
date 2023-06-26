"""
Connection Type Options.
"""

from typing import Union

from eventstore_grpc.options.dns_cluster import DNSClusterOptions
from eventstore_grpc.options.gossip_cluster import GossipClusterOptions
from eventstore_grpc.options.single_node import SingleNodeOptions

ConnectionTypeOptions = Union[
    DNSClusterOptions,
    GossipClusterOptions,
    SingleNodeOptions,
]
