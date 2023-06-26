from typing import Optional, Union

from eventstore_grpc.client.gossip import Gossip
from eventstore_grpc.client.operations import Operations
from eventstore_grpc.client.persistent import Persistent
from eventstore_grpc.client.projections import Projections
from eventstore_grpc.client.streams import Streams
from eventstore_grpc.client.subscriptions import Subscriptions
from eventstore_grpc.client.users import Users
from eventstore_grpc.core import ClientBase
from eventstore_grpc.core.auth import Auth
from eventstore_grpc.core.settings import KeepAlive
from eventstore_grpc.core.transport import Transport


class EventStore(ClientBase):
    """EventStore Client."""

    def __init__(
        self,
        hosts: Union[str, list[str]],
        discover: Optional[bool] = None,  # TODO: maybe remove?
        tls: Optional[bool] = None,  # TODO: maybe remove and keep just tls_ca_file.
        keep_alive_interval: Optional[int] = None,  # TODO: do we need this?
        keep_alive_timeout: Optional[int] = None,  # TODO: do we need this?
        username: Optional[str] = None,
        password: Optional[str] = None,
        tls_ca_file: Optional[str] = None,
    ) -> None:
        """Initializes a new EventStore Client.

        Args:
            hosts: either a single host url, or multiple ones, as a list.
            discover: whether or not to use discovery.
            tls: whether or not to use tls encryption.
            keep_alive_interval: the number of seconds for the keep alive interval.
            keep_alive_timeout: the number of seconds for the keep alive timeout.
            username: the username.
            password: the password.
            tls_ca_file: the filepath to the certificate to use for tls encryption.

        Raises:
            ValueError: when something goes wrong with the values you passed.
        """
        if not any([keep_alive_interval, keep_alive_timeout]):
            keep_alive = None
        else:
            keep_alive = KeepAlive()
            if keep_alive_interval:
                keep_alive.interval = keep_alive_interval
            if keep_alive_timeout:
                keep_alive.timeout = keep_alive_timeout

        if not tls and tls_ca_file:
            raise ValueError(f"tls is {tls} but you specified a ca_file: {tls_ca_file}")

        if any([username, password]) and not all([username, password]):
            raise ValueError(
                "You must specify both username AND password, or none of them."
            )

        super().__init__(
            Transport(
                hosts=hosts,
                discover=discover,
                tls=tls,
                keep_alive=keep_alive,
                auth=Auth(
                    root_certificate=tls_ca_file, username=username, password=password
                ),
            )
        )
        self.gossip = Gossip(self._transport)
        self.operations = Operations(self._transport)
        self.persistent = Persistent(self._transport)
        self.projections = Projections(self._transport)
        self.subscriptions = Subscriptions(self._transport)
        self.streams = Streams(self._transport)
        if self._transport.tls:  # TODO: is this the right condition?
            self.users = Users(self._transport)
