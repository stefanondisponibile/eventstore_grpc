"""
Channel Credential Options.
"""

import dataclasses


@dataclasses.dataclass
class ChannelCredentialOptions:
    insecure: bool
    root_certificate: bytes | None = None
    private_key: bytes | None = None
    cert_chain: bytes | None = None
    verify_options: bool | None = None  # ? apparently it is not possible to skip verification in the Python client. https://github.com/grpc/grpc/issues/10721
