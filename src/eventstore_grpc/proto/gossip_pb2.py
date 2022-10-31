# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gossip.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eventstore_grpc.proto import shared_pb2 as shared__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0cgossip.proto\x12\x19\x65vent_store.client.gossip\x1a\x0cshared.proto"E\n\x0b\x43lusterInfo\x12\x36\n\x07members\x18\x01 \x03(\x0b\x32%.event_store.client.gossip.MemberInfo")\n\x08\x45ndPoint\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r"\xfc\x03\n\nMemberInfo\x12-\n\x0binstance_id\x18\x01 \x01(\x0b\x32\x18.event_store.client.UUID\x12\x12\n\ntime_stamp\x18\x02 \x01(\x03\x12?\n\x05state\x18\x03 \x01(\x0e\x32\x30.event_store.client.gossip.MemberInfo.VNodeState\x12\x10\n\x08is_alive\x18\x04 \x01(\x08\x12;\n\x0ehttp_end_point\x18\x05 \x01(\x0b\x32#.event_store.client.gossip.EndPoint"\x9a\x02\n\nVNodeState\x12\x10\n\x0cInitializing\x10\x00\x12\x12\n\x0e\x44iscoverLeader\x10\x01\x12\x0b\n\x07Unknown\x10\x02\x12\x0e\n\nPreReplica\x10\x03\x12\x0e\n\nCatchingUp\x10\x04\x12\t\n\x05\x43lone\x10\x05\x12\x0c\n\x08\x46ollower\x10\x06\x12\r\n\tPreLeader\x10\x07\x12\n\n\x06Leader\x10\x08\x12\x0b\n\x07Manager\x10\t\x12\x10\n\x0cShuttingDown\x10\n\x12\x0c\n\x08Shutdown\x10\x0b\x12\x16\n\x12ReadOnlyLeaderless\x10\x0c\x12\x16\n\x12PreReadOnlyReplica\x10\r\x12\x13\n\x0fReadOnlyReplica\x10\x0e\x12\x13\n\x0fResigningLeader\x10\x0f\x32S\n\x06Gossip\x12I\n\x04Read\x12\x19.event_store.client.Empty\x1a&.event_store.client.gossip.ClusterInfoB&\n$com.eventstore.dbclient.proto.gossipb\x06proto3'
)


_CLUSTERINFO = DESCRIPTOR.message_types_by_name["ClusterInfo"]
_ENDPOINT = DESCRIPTOR.message_types_by_name["EndPoint"]
_MEMBERINFO = DESCRIPTOR.message_types_by_name["MemberInfo"]
_MEMBERINFO_VNODESTATE = _MEMBERINFO.enum_types_by_name["VNodeState"]
ClusterInfo = _reflection.GeneratedProtocolMessageType(
    "ClusterInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLUSTERINFO,
        "__module__": "gossip_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.gossip.ClusterInfo)
    },
)
_sym_db.RegisterMessage(ClusterInfo)

EndPoint = _reflection.GeneratedProtocolMessageType(
    "EndPoint",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENDPOINT,
        "__module__": "gossip_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.gossip.EndPoint)
    },
)
_sym_db.RegisterMessage(EndPoint)

MemberInfo = _reflection.GeneratedProtocolMessageType(
    "MemberInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _MEMBERINFO,
        "__module__": "gossip_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.gossip.MemberInfo)
    },
)
_sym_db.RegisterMessage(MemberInfo)

_GOSSIP = DESCRIPTOR.services_by_name["Gossip"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n$com.eventstore.dbclient.proto.gossip"
    _CLUSTERINFO._serialized_start = 57
    _CLUSTERINFO._serialized_end = 126
    _ENDPOINT._serialized_start = 128
    _ENDPOINT._serialized_end = 169
    _MEMBERINFO._serialized_start = 172
    _MEMBERINFO._serialized_end = 680
    _MEMBERINFO_VNODESTATE._serialized_start = 398
    _MEMBERINFO_VNODESTATE._serialized_end = 680
    _GOSSIP._serialized_start = 682
    _GOSSIP._serialized_end = 765
# @@protoc_insertion_point(module_scope)
