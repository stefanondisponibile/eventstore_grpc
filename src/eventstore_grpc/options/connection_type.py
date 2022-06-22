"""
Connection Type Options.
"""

from typing import Union
from eventstore_grpc import options

ConnectionTypeOptions = Union[
    options.DNSClusterOptions,
    options.GossipClusterOptions,
    options.SingleNodeOptions,
]
