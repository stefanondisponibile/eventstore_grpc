from datetime import datetime, timedelta
from unittest import mock

import pytest
from _pytest.monkeypatch import MonkeyPatch
from eventstore_grpc import discovery
from eventstore_grpc.proto import gossip_pb2


@pytest.fixture
def members() -> list[gossip_pb2.MemberInfo]:
    m1 = gossip_pb2.MemberInfo()
    m1.state = gossip_pb2.MemberInfo.VNodeState.Leader
    m2 = gossip_pb2.MemberInfo()
    m2.state = gossip_pb2.MemberInfo.VNodeState.Follower
    m3 = gossip_pb2.MemberInfo()
    m3.state = gossip_pb2.MemberInfo.VNodeState.Shutdown
    return [m1, m2, m3]


class FakeException(Exception):
    pass


def test_discover_endpoint_when_error(monkeypatch: MonkeyPatch) -> None:
    def fake_list_cluster_members(*args, **kwargs) -> None:
        raise FakeException("Fake!")

    monkeypatch.setattr(
        "eventstore_grpc.discovery.list_cluster_members", fake_list_cluster_members
    )
    candidates = ["localhost:123", "localhost:456"]
    with pytest.raises(FakeException):
        discovery.discover_endpoint(candidates=candidates)


class TestDetermineBestNode:
    def test_preference_leader(self, members: list[gossip_pb2.MemberInfo]) -> None:
        preference = gossip_pb2.MemberInfo.Leader
        best_node = discovery.determine_best_node(preference=preference, members=members)
        assert members[0] is best_node

    def test_preference_follower(self, members: list[gossip_pb2.MemberInfo]) -> None:
        preference = gossip_pb2.MemberInfo.Follower
        best_node = discovery.determine_best_node(
            preference=preference, members=members
        )
        assert members[1] is best_node
