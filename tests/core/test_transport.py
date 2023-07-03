import importlib.resources
from collections import namedtuple
from typing import Union
from unittest.mock import MagicMock

import dns.resolver
import grpc
import pytest
from _pytest.monkeypatch import MonkeyPatch

from eventstore_grpc import discovery
from eventstore_grpc.core import transport
from eventstore_grpc.core.auth import Auth
from eventstore_grpc.core.settings import KeepAlive


@pytest.mark.parametrize(
    "hosts",
    ["localhost:2113", ["localhost:2113"], ["localhost:2113", "localhost:2112"]],
)
def test_transport_init(hosts: Union[str, list[str]]) -> None:
    discover = False
    tls = True
    keep_alive = KeepAlive()
    username = "admin"
    password = "changeit"
    root_certificate = importlib.resources.path("tests.fixtures", "ca.crt")
    discovery.discover_endpoint = MagicMock(
        return_value=hosts if isinstance(hosts, str) else hosts[-1]
    )
    auth = Auth(username=username, password=password, root_certificate=root_certificate)
    t = transport.Transport(
        hosts=hosts, discover=discover, tls=tls, keep_alive=keep_alive, auth=auth
    )
    assert t.discover is discover
    assert t.keep_alive is keep_alive
    assert t.tls is tls
    assert t._auth is auth
    assert isinstance(t.target, str)
    assert isinstance(t.channel, grpc.Channel)
    if isinstance(hosts, str):
        assert hosts == t.target
        assert [hosts] == t.hosts
        assert t.multinode_cluster is False
    else:
        assert hosts[-1] == t.target
        assert hosts == t.hosts
        if len(hosts) > 1:
            assert t.multinode_cluster is True
        else:
            assert t.multinode_cluster is False


def test_transport_should_raise_when_no_hosts() -> None:
    with pytest.raises(ValueError):
        transport.Transport(hosts=[])


def test_resolve_gossip_seed(monkeypatch: MonkeyPatch) -> None:
    username = "admin"
    password = "changeit"
    root_cert = "certs/ca/ca.crt"
    auth = Auth(username=username, password=password, root_certificate=root_cert)
    discover = True
    tls = True
    keep_alive = KeepAlive()
    hosts = "example.com"
    MockAnswer = namedtuple("MockAnswer", ["address"])
    mock_dns_answers = [
        MockAnswer(address="localhost"),
    ]
    monkeypatch.setattr(dns.resolver, "resolve", lambda _: mock_dns_answers)
    t = transport.Transport(
        hosts=hosts, discover=discover, tls=tls, keep_alive=keep_alive, auth=auth
    )
    assert t.hosts[0] is hosts
    expected = [el.address + ":2112" for el in mock_dns_answers]
    assert expected == t._resolve_gossip_seed()
