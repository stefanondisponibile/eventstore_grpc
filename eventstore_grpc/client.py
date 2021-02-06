"""
Client.
"""

import abc
import grpc
from eventstore_grpc import mixins, connection_string_parser
from eventstore_grpc import options, discovery
from typing import List, Union


class ClientBase(abc.ABC):
    """Handles EventStoreDB operations."""

    def __init__(
        self,
        connection_string: str,
    ):
        """Initializes the EventStoreDBClient.

        Args:
            connection_string: the string to connect to the gRPC channel.
        """
        self._connection = connection_string_parser.Connection.from_connection_string(
            connection_string
        )
        self.channel = self._connection.channel

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.connection_string}')"

    def close(self):
        if getattr(self, "_subscriptions_manager", None):
            self.unsubscribe_all()
        self.channel.close()


class EventStoreDBClient(
    mixins.Streams,
    mixins.Projections,
    mixins.Users,
    mixins.Operations,
    mixins.Gossip,
    mixins.Persistent,
    mixins.Subscriptions,
    ClientBase,
):
    pass
