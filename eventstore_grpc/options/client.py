"""
Client Options.
"""

import dataclasses


@dataclasses.dataclass
class ClientOptions:
    throw_on_append_failure: bool
