"""Transport Layer"""

import logging
from typing import Optional, Union

import dns.exception
import dns.resolver
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
        return self

    def _new_channel(self) -> grpc.Channel:
        if self.is_insecure:
            return grpc.insecure_channel(self.target)
        return grpc.secure_channel(self.target, credentials=self.credentials)

    def _resolve_gossip_seed(self) -> list[str]:
        """Resolves the gossip seed using DNS records."""
        if self.multinode_cluster:
            raise ValueError("Nothing to resolve if you have the hosts already.")
        domain = self.hosts[-1]
        default_port = 2112
        seed = [f"{el.address}:{default_port}" for el in dns.resolver.resolve(domain)]
        if not seed:
            raise Exception(f"Couldn't resolve {domain} to any address.")
        return seed

    def _get_target_node(self) -> str:
        """Gets the target node, using discovery when needed."""
        if self.multinode_cluster or self._discover:
            return discovery.discover_endpoint(
                self._resolve_gossip_seed() if self._discover else self._hosts,
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
    def credentials(self) -> grpc.ChannelCredentials | None:
        if self._auth is not None:
            return self._auth.credentials
        return None

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
    def keep_alive(self) -> KeepAlive | None:
        return self._keep_alive

    @property
    def discover(self) -> bool | None:
        return self._discover
