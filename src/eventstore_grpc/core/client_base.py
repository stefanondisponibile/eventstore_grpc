"""EventStoreDB client."""

from .transport import Transport


class ClientBase:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    @property
    def channel(self):
        return self._transport.channel

    @classmethod
    def from_connection_string(cls, connection_string: str) -> "ClientBase":
        return cls(
            transport=Transport.from_connection_string(
                connection_string=connection_string
            )
        )
