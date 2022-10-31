import importlib.resources

import pytest

from eventstore_grpc import client
from eventstore_grpc.client import (
    Gossip,
    Operations,
    Persistent,
    Projections,
    Streams,
    Subscriptions,
    Users,
)


def test_eventstore_client_basic_init() -> None:
    event_store = client.EventStore(hosts=["localhost:2113"])
    assert isinstance(event_store.gossip, Gossip)
    assert isinstance(event_store.operations, Operations)
    assert isinstance(event_store.persistent, Persistent)
    assert isinstance(event_store.projections, Projections)
    assert isinstance(event_store.subscriptions, Subscriptions)
    assert isinstance(event_store.streams, Streams)
    assert not hasattr(event_store, "users")


def test_eventstore_init_with_keepalive() -> None:
    ka_interval = 42
    ka_timeout = 24
    event_store = client.EventStore(
        hosts=["localhost:2113"],
        keep_alive_interval=ka_interval,
        keep_alive_timeout=ka_timeout,
    )
    assert event_store._transport.keep_alive.interval == ka_interval
    assert event_store._transport.keep_alive.timeout == ka_timeout


def test_should_raise_if_tls_and_no_ca_file() -> None:
    with pytest.raises(ValueError):
        client.EventStore(hosts=["localhos:2113"], tls_ca_file="some-file.cert")


def test_should_set_username_and_password() -> None:
    username, password = "some-username", "some-password"
    event_store = client.EventStore(
        hosts=["localhost:2113"],
        username=username,
        password=password,
        tls=True,
        tls_ca_file=importlib.resources.path("tests.fixtures", "ca.crt"),
    )  # TODO dig a little bit into this: we really need tls in this case?
    assert event_store._transport._auth.username == username
    assert event_store._transport._auth.password == password
    assert isinstance(event_store.users, Users)
