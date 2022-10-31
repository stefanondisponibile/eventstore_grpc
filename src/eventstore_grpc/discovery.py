"""
Discovery and gossip helpers.
"""

import logging
import random
from collections.abc import Iterable
from typing import List

import grpc

from eventstore_grpc import gossip
from eventstore_grpc.proto import gossip_pb2, gossip_pb2_grpc

log = logging.getLogger(__name__)


def discover_endpoint(
    candidates: List,
    credentials: grpc.ChannelCredentials = None,
    max_discovery_attempts: int = 10,
    vnode_state: gossip_pb2.MemberInfo.VNodeState = gossip_pb2.MemberInfo.Leader,
) -> str:
    """Discovers an endpoint to connect to.

    Args:
        candidates: a list of candidates nodes to use for discovery.
        credentials: the channel credentials to use for listing cluster members.
        max_discovery_attempts: the maximum number of discovery attempts that will be
                                made to determine the best node.
        node_preference: the type of node to prefer.

    Returns:
        The url of the selected node.

    Raises:
        Exception: when it's not possible to match any node.
    """

    discover_attempts = 0

    while discover_attempts < max_discovery_attempts:
        discover_attempts += 1

        for candidate in candidates:
            try:
                members = list_cluster_members(
                    candidate,
                    credentials,
                )
                member_info = determine_best_node(vnode_state, members)
                if member_info is not None:
                    endpoint = member_info.http_end_point
                    return f"{endpoint.address}:{endpoint.port}"
            except Exception as err:
                log.error(f"Failed to get cluster list from: {candidate}")
                raise err
    raise Exception("Couldn't match an endpoint.")  # pragma: nocover


def determine_best_node(
    preference: gossip_pb2.MemberInfo.VNodeState, members: List[gossip_pb2.MemberInfo]
) -> gossip_pb2.MemberInfo:
    """Selects the best node, given a `preference`.

    Args:
        preference: the type of node that you want to choose (e.g. `leader`).
        members: a list of nodes (as gossip_pb2.MemeberInfo objects) to choose from.

    Returns:
        The selected node from members, of None if none of the objects satisfies the
        requested preference.
    """
    candidates = [member for member in members if member.state is preference]
    return random.choice(candidates) if candidates else None


def list_cluster_members(
    uri: str, credentials: grpc.ChannelCredentials
) -> Iterable[gossip_pb2.MemberInfo]:
    """Lists cluster memeber using the provided uri to connect to the cluster.

    You can use this function to get information about the nodes in the cluster.
    The MemberInfo objects returned can give information like the state of the node
    (Initializing, Leader, ...), the instance id, is_alive, and the endpoint of
    the node (address, port).

    Args:
        uri: the URI that will be used to connect to the node.
        credentials: the ChannelCredentials to use to connect to the node.

    Returns:
        The nodes information as gossip_pb2.MemberInfo objects.
    """
    with grpc.secure_channel(uri, credentials) as channel:
        stub = gossip_pb2_grpc.GossipStub(channel)
        info = gossip.read(stub)
    return info.members
