"""Transport Layer"""

import logging
from typing import Optional, Union

import grpc

from eventstore_grpc import discovery

from .auth import Auth
from .settings import KeepAlive

log = logging.getLogger(__name__)


class Transport:
    def __init__(
        self,
        hosts: Union[str, list[str]],
        discover: Optional[bool] = None,
        tls: Optional[bool] = None,
        keep_alive: Optional[KeepAlive] = None,  # TODO: maybe remove?
        auth: Optional[Auth] = None,
    ) -> None:
        """Transport layer."""
        if not isinstance(hosts, list):
            hosts = [hosts]

        if len(hosts) < 1:
            raise ValueError("You must specify at least one node.")

        self._hosts = hosts
        self._auth = auth
        self._tls = tls
        self._keep_alive = keep_alive
        self._discover = discover
        self._channel = self._new_channel()

    def refresh_channel(self) -> "Transport":
        """Gets a new channel."""
        self._channel = self._new_channel()

    def _new_channel(self) -> grpc.Channel:
        if self.is_insecure:
            return grpc.insecure_channel(self.target)
        return grpc.secure_channel(self.target, credentials=self.credentials)

    def _get_target_node(self) -> str:
        """Gets the target node, using discovery when needed."""
        if self.multinode_cluster:
            return discovery.discover_endpoint(
                self._hosts,
                credentials=self.credentials if self.tls else None,
            )
        else:
            return self._hosts[-1]

    @property
    def is_insecure(self) -> bool:
        return not self._tls and (
            not self._auth or not any([self._auth.username, self._auth.password])
        )

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

    @property
    def tls(self):
        return self._tls

    @property
    def keep_alive(self) -> KeepAlive:
        return self._keep_alive

    @property
    def discover(self) -> bool:
        return self._discover
