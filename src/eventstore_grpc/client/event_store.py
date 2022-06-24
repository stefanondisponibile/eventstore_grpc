from typing import Optional, Union

from eventstore_grpc.client import (
    Gossip,
    Operations,
    Persistent,
    Projections,
    Streams,
    Subscriptions,
    Users,
)
from eventstore_grpc.core import ClientBase
from eventstore_grpc.core.transport import Transport
from eventstore_grpc.core.settings import KeepAlive
from eventstore_grpc.core.auth import Auth


class EventStore(ClientBase):
    def __init__(
        self,
        hosts: Union[str, list[str]],
        discover: Optional[bool] = None,
        tls: Optional[bool] = None,
        keep_alive_interval: Optional[int] = None,
        keep_alive_timeout: Optional[int] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        tls_ca_file: Optional[str] = None,
    ):
        if not any([keep_alive_interval, keep_alive_timeout]):
            keep_alive = None
        else:
            keep_alive = KeepAlive()
            if keep_alive_interval:
                keep_alive.interval = keep_alive.interval
            if keep_alive_timeout:
                keep_alive.timeout = keep_alive.timeout

        if not tls and tls_ca_file:
            raise ValueError(f"tls is {tls} but you specified a ca_file: {tls_ca_file}")

        auth = Auth(root_certificate=tls_ca_file)

        if all([username, password]):
            auth.username = username
            auth.password = password

        super().__init__(
            Transport(
                hosts=hosts,
                discover=discover,
                tls=tls,
                keep_alive=keep_alive,
                auth=auth,
            )
        )
        self.gossip = Gossip(self._transport)
        self.operations = Operations(self._transport)
        self.persistent = Persistent(self._transport)
        self.projections = Projections(self._transport)
        self.subscriptions = Subscriptions(self._transport)
        self.streams = Streams(self._transport)
        if self._transport.tls:
            self.users = Users(self._transport)
