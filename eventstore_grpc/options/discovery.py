"""
Discovery Options.
"""

import dataclasses

@dataclasses.dataclass
class DiscoveryOptions:
    max_discover_attempts: int  # How many times to attempt connection before raising.
    discovery_interval: int  # How long to wait before retrying (in seconds).
    gossip_timeout: int  # How long to wait for the request to time out (in seconds).
    node_preference: str  # Preferred node type.
