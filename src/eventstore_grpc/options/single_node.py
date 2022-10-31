"""
Single Node Options.
"""

import dataclasses

from eventstore_grpc import options


@dataclasses.dataclass
class SingleNodeOptions(options.ClientOptions):
    endpoint: str
