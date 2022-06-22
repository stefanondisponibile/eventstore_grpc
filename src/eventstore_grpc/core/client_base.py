"""EventStoreDB client."""

from .transport import Transport


class ClientBase:
    def __init__(self, transport: Transport) -> None:
        """Initializes a ClientBase.
        
        Args:
            transport (Transport): an instance of a Transport Class.
        """

        self._transport = transport

    @property
    def channel(self):
        """The gRPC channel from the underlying transport class."""
        return self._transport.channel

    @classmethod
    def from_connection_string(cls, connection_string: str) -> "ClientBase":
        """Creates a new Client from a connection string.

        Args:
            connection_string (str): a connection string.

        Returns:
            client (ClientBase)
        """
        return cls(
            transport=Transport.from_connection_string(
                connection_string=connection_string
            )
        )
