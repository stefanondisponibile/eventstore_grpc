import grpc

from eventstore_grpc.core import client_base, transport


def test_client_base_init() -> None:
    t = transport.Transport(hosts="localhost:2113")
    cb = client_base.ClientBase(transport=t)
    assert isinstance(cb._transport, transport.Transport)
    assert isinstance(cb.channel, grpc.Channel)
