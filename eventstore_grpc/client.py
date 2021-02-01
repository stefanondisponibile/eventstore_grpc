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
        self.connection_string = connection_string
        parsed = connection_string_parser.parse(connection_string)
        self.connection_type_options = parsed[0]
        self.channel_credential_options = parsed[1]
        if isinstance(
            self.connection_type_options,
            (options.DNSClusterOptions, options.GossipClusterOptions),
        ):
            if self.channel_credential_options.insecure:
                self.credentials = None
            else:
                self.credentials = grpc.ssl_channel_credentials(
                    root_certificates=self.channel_credential_options.root_certificate,
                    private_key=self.channel_credential_options.private_key,
                )
            self.endpoint = discovery.discover_endpoint(
                self.endpoints, self.credentials
            )
        else:
            self.endpoint = self.endpoints[0]

        if self.channel_credential_options.insecure:
            self.channel = grpc.insecure_channel(self.endpoint)
        else:
            self.channel = grpc.secure_channel(self.endpoint, self.credentials)

    @property
    def endpoints(self):
        if isinstance(self.connection_type_options, options.SingleNodeOptions):
            endpoints = [self.connection_type_options.endpoint]
        elif isinstance(self.connection_type_options, options.DNSClusterOptions):
            endpoints = [self.connection_type_options.discover]
        elif isinstance(self.connection_type_options, options.GossipClusterOptions):
            endpoints = self.connection_type_options.endpoints
        else:
            endpoints = []
        return [f"{elm['host']}:{elm['port']}" for elm in endpoints]

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.connection_string}')"


class EventStoreDBClient(
    mixins.Streams,
    mixins.Users,
    mixins.Operations,
    mixins.Gossip,
    ClientBase,
):
    pass
