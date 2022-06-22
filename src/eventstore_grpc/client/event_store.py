from eventstore_grpc.client import (
    Gossip,
    Operations,
    Persistent,
    Projections,
    Streams,
    Users,
    Subscriptions,
)

from eventstore_grpc.core import ClientBase


class EventStore(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gossip = Gossip(self._transport)
        self.operations = Operations(self._transport)
        self.persistent = Persistent(self._transport)
        self.projections = Projections(self._transport)
        self.subscriptions = Subscriptions(self._transport)
        self.streams = Streams(self._transport)
        if self._transport.tls:
            self.users = Users(self._transport)

    @classmethod
    def from_connection_string(cls, connection_string: str) -> "EventStore":
        return super().from_connection_string(connection_string)
