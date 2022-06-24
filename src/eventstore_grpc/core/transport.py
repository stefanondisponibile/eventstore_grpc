"""Transport Layer"""

import logging
from typing import Optional, Union
from urllib.parse import urlparse

import grpc

from .settings import KeepAlive
from .auth import Auth
from eventstore_grpc import discovery

log = logging.getLogger(__name__)


class Transport:
    def __init__(
        self,
        hosts: Union[str, list[str]],
        discover: Optional[bool] = None,
        tls: Optional[bool] = None,
        keep_alive: Optional[KeepAlive] = None,
        auth: Optional[Auth] = None,
    ) -> None:
        """Transport layer."""
        if not isinstance(hosts, list):
            hosts = [hosts]

        if len(hosts) < 1:
            raise ValueError("You must specify at least one node.")

        self._hosts = hosts
        self._tls = tls
        self._keep_alive = keep_alive
        self._discover = discover
        self._auth = auth
        self._channel = self._new_channel()

    def _new_channel(self) -> grpc.Channel:
        """Returns a new grpc channel."""
        if not self._tls and not any([self._auth._username, self._auth._password]):
            return grpc.insecure_channel(self.target)
        else:
            return grpc.secure_channel(self.target, credentials=self.credentials)

    @property
    def credentials(self) -> grpc.ChannelCredentials:
        return self._auth.credentials

    @property
    def target(self) -> str:
        return self._get_target_node()

    @property
    def channel(self) -> grpc.Channel:
        return self._channel

    @property
    def multinode_cluster(self) -> bool:
        return len(self._hosts) > 1

    @property
    def hosts(self) -> list[str]:
        return self._hosts

    def _get_target_node(self) -> str:
        """Gets the target node, using discovery when needed."""
        if self.multinode_cluster:
            target = discovery.discover_endpoint(
                self._hosts,
                credentials=self._get_credentials() if self.tls else None,
            )
            for host in self._hosts:
                if host == target:
                    return host
            else:
                raise RuntimeError("Couldn't choose a Node with discovery.")
        else:
            return self._hosts[-1]

    @property
    def tls(self):
        return self._tls

    @property
    def keep_alive(self) -> KeepAlive:
        return self._keep_alive

    @property
    def discover(self) -> bool:
        return self._discover
