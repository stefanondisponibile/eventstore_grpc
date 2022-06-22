"""
EventStore Transport configuration.

Configuration is mainly passed through a connection string.

You can use the official `Connection Details builder`_ from the EventStore website to create your own connection string.

The connection string is divided in **three main parts**: (mode)://(nodes)?(options)

1. **mode**: can be either `esdb` or `esdb+discovery`
2. **nodes**: is a list of urls.
3. **options**: some options.

.. _Connection Details builder: https://developers.eventstore.com/clients/grpc/#connection-details
"""

import logging
from multiprocessing import connection
from typing import Optional
from urllib.parse import urlparse

import grpc

from .settings import KeepAlive, Node
from eventstore_grpc import discovery

log = logging.getLogger(__name__)


class Transport:
    def __init__(
        self,
        nodes: list[Node],
        discover: bool = False,
        tls: Optional[bool] = None,
        keep_alive: Optional[KeepAlive] = None,
    ) -> None:
        """Transport layer."""

        if len(nodes) < 1:
            raise ValueError("You must specify at least one node.")

        self._nodes = nodes
        self._tls = tls
        self._keep_alive = keep_alive
        self._discover = discover
        self._channel = self._new_channel()

    def _new_channel(self) -> grpc.Channel:
        """Returns a new grpc channel."""
        if not self._tls:
            return grpc.insecure_channel(self.target)
        else:
            return grpc.secure_channel(self.target, credentials=self._get_credentials())

    def _get_credentials(self, *args, **kwargs) -> grpc.ChannelCredentials:
        return grpc.ssl_channel_credentials(*args, **kwargs)

    @property
    def target(self) -> str:
        return self._get_target_node().get_url()

    @property
    def channel(self) -> grpc.Channel:
        return self._channel

    @property
    def multinode_cluster(self) -> bool:
        return len(self._nodes) > 1

    @property
    def nodes(self) -> list[Node]:
        return self._nodes

    def _get_target_node(self) -> Node:
        """Gets the target node, using discovery when needed."""
        if self.multinode_cluster:
            target = discovery.discover_endpoint(
                [node.get_url() for node in self.nodes],
                credentials=self._get_credentials() if self.tls else None,
            )
            for node in self.nodes:
                if node.get_url() == target:
                    return node
            else:
                raise RuntimeError("Couldn't choose a Node with discovery.")
        else:
            return self.nodes[-1]

    @property
    def tls(self):
        return self._tls

    @property
    def keep_alive(self) -> KeepAlive:
        return self._keep_alive

    @property
    def discover(self) -> bool:
        return self._discover

    @classmethod
    def from_connection_string(cls, connection_string: str) -> "Transport":
        """Parses a connection string to create a Transport instance."""
        discover = "+discover://" in connection_string
        tls = "tls=true" in connection_string.lower()
        parts = connection_string.partition("://")[-1].split("?")
        nodes = []
        for node in parts[0].split(","):
            if ":" in node:
                host, port = node.split(":")
            else:
                host, port = node, None
            nodes.append(Node(host=host, port=port))
        # TODO: parse KeepAlive settings
        return cls(nodes=nodes, discover=discover, tls=tls)



    # @classmethod
    # def from_connection_string(cls, connection_string: str) -> "Transport":
    #     """Parses a connection_string to create a Transport instance."""
    #     parts = connection_string.partition("://")
    #     if not any(parts):
    #         raise ValueError(f"Invalid connection string: {connection_string}")
    #     discover = parts[0].endswith("+discover")
    #     nodes = []
    #     for elm in parts[2].rpartition("?")[-1].split(","):
    #         if not elm.startswith("http://") or elm.startswith("https://"):
    #             elm = "http://" + elm
    #         url = urlparse(elm)
    #         node = Node(host=url.netloc)
    #         if url.port:
    #             node.port = url.port
    #         if url.scheme:
    #             node.scheme = None  # hacky way of NOT passing a scheme.
    #         nodes.append(node)
    #     if not nodes:
    #         raise ValueError("You must provide at least one node.")
    #     if "tls=true" in connection_string.lower():
    #         tls = True
    #     else:
    #         tls = False
    #     return cls(nodes=nodes, discover=discover, tls=tls)
