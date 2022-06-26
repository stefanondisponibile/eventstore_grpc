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
