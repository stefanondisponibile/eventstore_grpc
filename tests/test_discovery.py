from eventstore_grpc.proto import gossip_pb2
from eventstore_grpc import discovery
import pytest
from unittest import mock
from datetime import datetime, timedelta


@pytest.fixture
def members() -> list[gossip_pb2.MemberInfo]:
    m1 = gossip_pb2.MemberInfo()
    m1.state = gossip_pb2.MemberInfo.VNodeState.Leader
    m2 = gossip_pb2.MemberInfo()
    m2.state = gossip_pb2.MemberInfo.VNodeState.Follower
    m3 = gossip_pb2.MemberInfo()
    m3.state = gossip_pb2.MemberInfo.VNodeState.Shutdown
    return [m1, m2, m3]


def test_in_allowed_state() -> None:
    member = gossip_pb2.MemberInfo()
    for v in gossip_pb2.MemberInfo.VNodeState.values():
        member.state = v
        if v == gossip_pb2.MemberInfo.VNodeState.Shutdown:
            assert discovery.in_allowed_states(member) is False
        else:
            assert discovery.in_allowed_states(member) is True


def test_is_leader() -> None:
    member = gossip_pb2.MemberInfo()
    for v in gossip_pb2.MemberInfo.VNodeState.values():
        member.state = v
        if v == gossip_pb2.MemberInfo.VNodeState.Leader:
            assert discovery.is_leader(member) is True
        else:
            assert discovery.is_leader(member) is False


def test_is_follower() -> None:
    member = gossip_pb2.MemberInfo()
    for v in gossip_pb2.MemberInfo.VNodeState.values():
        member.state = v
        if v == gossip_pb2.MemberInfo.VNodeState.Follower:
            assert discovery.is_follower(member) is True
        else:
            assert discovery.is_follower(member) is False


class TestDetermineBestNode:
    def test_preference_leader(self, members: list[gossip_pb2.MemberInfo]) -> None:
        best_node = discovery.determine_best_node(preference="leader", members=members)
        assert members[0] is best_node

    def test_preference_follower(self, members: list[gossip_pb2.MemberInfo]) -> None:
        best_node = discovery.determine_best_node(
            preference="follower", members=members
        )
        assert members[1] is best_node

    def test_preference_random(self, members: list[gossip_pb2.MemberInfo]) -> None:
        best_node = discovery.determine_best_node(preference="random", members=members)
        assert best_node in members[:2]


@pytest.mark.parametrize("seconds", range(0, 330, 30))
def test_create_deadline(seconds: int) -> None:
    now = datetime.now()
    expected = now + timedelta(seconds=seconds)
    with mock.patch(
        "eventstore_grpc.discovery.datetime.datetime",
    ) as dt:
        dt.now.return_value = now
        assert expected == discovery.create_deadline(seconds=seconds)
