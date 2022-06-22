from eventstore_grpc.core import client_base
from grpc import Call, Channel
from typing import Callable


def test_client_base(connection_string: str) -> None:
    client = client_base.ClientBase.from_connection_string(
        connection_string=connection_string
    )
    assert isinstance(client.channel, Channel)
