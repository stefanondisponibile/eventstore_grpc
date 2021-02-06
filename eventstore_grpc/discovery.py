"""
Discovery and gossip helpers.
"""

import grpc
from typing import Dict, List
from eventstore_grpc.proto import gossip_pb2, gossip_pb2_grpc
import datetime
from eventstore_grpc import gossip
import random


def discover_endpoint(
    candidates: List,
    credentials: grpc.ChannelCredentials = None,
    discovery_interval: int = 100,  # used to delay what? Each iter?
    max_discovery_attempts: int = 10,
    gossip_timeout: int = 5,
    node_preference: str = "RANDOM",
    settings: Dict = {},
) -> str:
    discover_attempts = 0

    while discover_attempts < max_discovery_attempts:
        discover_attempts += 1

        for candidate in candidates:
            try:
                members = list_cluster_members(
                    candidate, credentials, create_deadline(gossip_timeout)
                )
                endpoint = determine_best_node(node_preference, members)
                if endpoint:
                    return f"{endpoint['address']}:{endpoint['port']}"
            except Exception as err:
                print(err)
                print(f"Failed to get cluster list from {candidate}")
                raise err
                continue
    raise Exception("Couldn't match an endpoint.")


def in_allowed_states(member: Dict[str, str]) -> bool:
    if member["state"] == gossip_pb2.MemberInfo.VNodeState.Shutdown:
        return False
    else:
        return True


def is_leader(member: gossip_pb2.MemberInfo) -> bool:
    return member["state"] == gossip_pb2.MemberInfo.VNodeState.Leader


def is_follower(member: gossip_pb2.MemberInfo) -> bool:
    return member["state"] == gossip_pb2.MemberInfo.VNodeState.Follower


def determine_best_node(preference, members: List[gossip_pb2.MemberInfo]):
    sorted_nodes = list(filter(in_allowed_states, members))
    final_member = None
    if preference.lower() == "leader":
        final_member = random.choice([elm for elm in sorted_nodes if is_leader(elm)])
    elif preference.lower() == "follower":
        final_member = random.choice([elm for elm in sorted_nodes if is_follower(elm)])
    elif preference.lower() == "random":
        final_member = random.choice(sorted_nodes)

    if final_member and final_member["http_end_point"]:
        return {
            "address": final_member["http_end_point"]["address"],
            "port": final_member["http_end_point"]["port"],
        }


def create_deadline(seconds: int):
    return datetime.datetime.now() + datetime.timedelta(seconds=seconds)


def list_cluster_members(uri: str, credentials: grpc.ChannelCredentials, deadline):
    if credentials is None:
        credentials = grpc.ssl_channel_credentials()
    with grpc.secure_channel(uri, credentials) as channel:
        stub = gossip_pb2_grpc.GossipStub(channel)
        info = gossip.read(stub)
        members = []
        for grpc_member in info.members:
            http_end_point = None
            grpc_http_end_point = grpc_member.http_end_point
            if grpc_member.HasField("http_end_point"):
                http_end_point = {
                    "address": grpc_http_end_point.address,
                    "port": grpc_http_end_point.port,
                }
            member = {
                "instance_id": grpc_member.instance_id.string,
                "timestamp": grpc_member.time_stamp,
                "state": grpc_member.state,
                "is_alive": grpc_member.is_alive,
                "http_end_point": http_end_point,
            }
            members.append(member)
    return members
