"""
Base Request Options.
"""

import base64
import dataclasses
from typing import Dict, List, Optional, Tuple

import grpc


@dataclasses.dataclass
class BaseOptions:
    credentials: Optional[Dict[str, str]] = None
    requires_leader: Optional[bool] = None

    @property
    def metadata(self):
        return as_metadata(self.credentials, self.requires_leader)


def as_metadata(
    credentials: Optional[Dict[str, str]] = None, requires_leader: Optional[bool] = None
) -> Optional[List[Optional[Tuple[str, str]]]]:
    """Returns a valid grpc "metadata" object."""
    metadata = []
    if credentials is not None:
        if all(elm in ["username", "password"] for elm in credentials):
            token = f"{credentials['username']}:{credentials['password']}"
            token = base64.b64encode(token.encode("ascii")).decode("ascii")
            auth = ("authorization", f"Bearer {token}")
            metadata.append(auth)
    if requires_leader is not None:
        req_leader = ("requires-leader", str(requires_leader).lower())
        metadata.append(req_leader)
    return metadata if metadata else None


class EventStoreDBMetadataPlugin(grpc.AuthMetadataPlugin):
    def __init__(
        self, username: str = None, password: str = None, requires_leader: bool = None
    ):
        self._username = username
        self._password = password
        self._requires_leader = requires_leader
        self._metadata = None

    @staticmethod
    def _compile_token(username: str, password: str):
        if not username or not password:
            return None

        if username.strip() and password.strip():
            _key = f"{username}:{password}".encode("ascii")
            token = base64.b64encode(_key).decode("ascii")
            return ("authorization", f"Basic {token}")

    @staticmethod
    def _compile_requires_leader(requires_leader: bool):
        if requires_leader is not None:
            return ("requires-leader", str(requires_leader).lower())

    def compile(self):
        metadata = []
        compiled_token = self._compile_token(self._username, self._password)
        compiled_requires_leader = self._compile_requires_leader(self._requires_leader)
        if compiled_token:
            metadata.append(compiled_token)
        if compiled_requires_leader:
            metadata.append(compiled_requires_leader)
        if metadata:
            self._metadata = tuple(metadata)
        return self

    def __call__(self, context, callback):
        self.compile()
        callback(self._metadata, None)


def as_credentials(
    username: Optional[str] = None,
    password: Optional[str] = None,
    requires_leader: Optional[bool] = None,
) -> grpc.AuthMetadataPlugin:
    return grpc.metadata_call_credentials(
        EventStoreDBMetadataPlugin(username, password, requires_leader),
        EventStoreDBMetadataPlugin.__name__,
    )
