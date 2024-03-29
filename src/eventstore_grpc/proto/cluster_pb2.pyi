"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import shared_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GossipRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INFO_FIELD_NUMBER: builtins.int
    SERVER_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> global___ClusterInfo: ...
    @property
    def server(self) -> global___EndPoint: ...
    def __init__(
        self,
        *,
        info: typing.Optional[global___ClusterInfo] = ...,
        server: typing.Optional[global___EndPoint] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["info", b"info", "server", b"server"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["info", b"info", "server", b"server"],
    ) -> None: ...

global___GossipRequest = GossipRequest

class ViewChangeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVER_ID_FIELD_NUMBER: builtins.int
    SERVER_HTTP_FIELD_NUMBER: builtins.int
    ATTEMPTED_VIEW_FIELD_NUMBER: builtins.int
    @property
    def server_id(self) -> shared_pb2.UUID: ...
    @property
    def server_http(self) -> global___EndPoint: ...
    attempted_view: builtins.int
    def __init__(
        self,
        *,
        server_id: typing.Optional[shared_pb2.UUID] = ...,
        server_http: typing.Optional[global___EndPoint] = ...,
        attempted_view: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "server_http", b"server_http", "server_id", b"server_id"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "attempted_view",
            b"attempted_view",
            "server_http",
            b"server_http",
            "server_id",
            b"server_id",
        ],
    ) -> None: ...

global___ViewChangeRequest = ViewChangeRequest

class ViewChangeProofRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVER_ID_FIELD_NUMBER: builtins.int
    SERVER_HTTP_FIELD_NUMBER: builtins.int
    INSTALLED_VIEW_FIELD_NUMBER: builtins.int
    @property
    def server_id(self) -> shared_pb2.UUID: ...
    @property
    def server_http(self) -> global___EndPoint: ...
    installed_view: builtins.int
    def __init__(
        self,
        *,
        server_id: typing.Optional[shared_pb2.UUID] = ...,
        server_http: typing.Optional[global___EndPoint] = ...,
        installed_view: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "server_http", b"server_http", "server_id", b"server_id"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "installed_view",
            b"installed_view",
            "server_http",
            b"server_http",
            "server_id",
            b"server_id",
        ],
    ) -> None: ...

global___ViewChangeProofRequest = ViewChangeProofRequest

class PrepareRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVER_ID_FIELD_NUMBER: builtins.int
    SERVER_HTTP_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    @property
    def server_id(self) -> shared_pb2.UUID: ...
    @property
    def server_http(self) -> global___EndPoint: ...
    view: builtins.int
    def __init__(
        self,
        *,
        server_id: typing.Optional[shared_pb2.UUID] = ...,
        server_http: typing.Optional[global___EndPoint] = ...,
        view: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "server_http", b"server_http", "server_id", b"server_id"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "server_http", b"server_http", "server_id", b"server_id", "view", b"view"
        ],
    ) -> None: ...

global___PrepareRequest = PrepareRequest

class PrepareOkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VIEW_FIELD_NUMBER: builtins.int
    SERVER_ID_FIELD_NUMBER: builtins.int
    SERVER_HTTP_FIELD_NUMBER: builtins.int
    EPOCH_NUMBER_FIELD_NUMBER: builtins.int
    EPOCH_POSITION_FIELD_NUMBER: builtins.int
    EPOCH_ID_FIELD_NUMBER: builtins.int
    EPOCH_LEADER_INSTANCE_ID_FIELD_NUMBER: builtins.int
    LAST_COMMIT_POSITION_FIELD_NUMBER: builtins.int
    WRITER_CHECKPOINT_FIELD_NUMBER: builtins.int
    CHASER_CHECKPOINT_FIELD_NUMBER: builtins.int
    NODE_PRIORITY_FIELD_NUMBER: builtins.int
    CLUSTER_INFO_FIELD_NUMBER: builtins.int
    view: builtins.int
    @property
    def server_id(self) -> shared_pb2.UUID: ...
    @property
    def server_http(self) -> global___EndPoint: ...
    epoch_number: builtins.int
    epoch_position: builtins.int
    @property
    def epoch_id(self) -> shared_pb2.UUID: ...
    @property
    def epoch_leader_instance_id(self) -> shared_pb2.UUID: ...
    last_commit_position: builtins.int
    writer_checkpoint: builtins.int
    chaser_checkpoint: builtins.int
    node_priority: builtins.int
    @property
    def cluster_info(self) -> global___ClusterInfo: ...
    def __init__(
        self,
        *,
        view: builtins.int = ...,
        server_id: typing.Optional[shared_pb2.UUID] = ...,
        server_http: typing.Optional[global___EndPoint] = ...,
        epoch_number: builtins.int = ...,
        epoch_position: builtins.int = ...,
        epoch_id: typing.Optional[shared_pb2.UUID] = ...,
        epoch_leader_instance_id: typing.Optional[shared_pb2.UUID] = ...,
        last_commit_position: builtins.int = ...,
        writer_checkpoint: builtins.int = ...,
        chaser_checkpoint: builtins.int = ...,
        node_priority: builtins.int = ...,
        cluster_info: typing.Optional[global___ClusterInfo] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "cluster_info",
            b"cluster_info",
            "epoch_id",
            b"epoch_id",
            "epoch_leader_instance_id",
            b"epoch_leader_instance_id",
            "server_http",
            b"server_http",
            "server_id",
            b"server_id",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "chaser_checkpoint",
            b"chaser_checkpoint",
            "cluster_info",
            b"cluster_info",
            "epoch_id",
            b"epoch_id",
            "epoch_leader_instance_id",
            b"epoch_leader_instance_id",
            "epoch_number",
            b"epoch_number",
            "epoch_position",
            b"epoch_position",
            "last_commit_position",
            b"last_commit_position",
            "node_priority",
            b"node_priority",
            "server_http",
            b"server_http",
            "server_id",
            b"server_id",
            "view",
            b"view",
            "writer_checkpoint",
            b"writer_checkpoint",
        ],
    ) -> None: ...

global___PrepareOkRequest = PrepareOkRequest

class ProposalRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVER_ID_FIELD_NUMBER: builtins.int
    SERVER_HTTP_FIELD_NUMBER: builtins.int
    LEADER_ID_FIELD_NUMBER: builtins.int
    LEADER_HTTP_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    EPOCH_NUMBER_FIELD_NUMBER: builtins.int
    EPOCH_POSITION_FIELD_NUMBER: builtins.int
    EPOCH_ID_FIELD_NUMBER: builtins.int
    EPOCH_LEADER_INSTANCE_ID_FIELD_NUMBER: builtins.int
    LAST_COMMIT_POSITION_FIELD_NUMBER: builtins.int
    WRITER_CHECKPOINT_FIELD_NUMBER: builtins.int
    CHASER_CHECKPOINT_FIELD_NUMBER: builtins.int
    NODE_PRIORITY_FIELD_NUMBER: builtins.int
    @property
    def server_id(self) -> shared_pb2.UUID: ...
    @property
    def server_http(self) -> global___EndPoint: ...
    @property
    def leader_id(self) -> shared_pb2.UUID: ...
    @property
    def leader_http(self) -> global___EndPoint: ...
    view: builtins.int
    epoch_number: builtins.int
    epoch_position: builtins.int
    @property
    def epoch_id(self) -> shared_pb2.UUID: ...
    @property
    def epoch_leader_instance_id(self) -> shared_pb2.UUID: ...
    last_commit_position: builtins.int
    writer_checkpoint: builtins.int
    chaser_checkpoint: builtins.int
    node_priority: builtins.int
    def __init__(
        self,
        *,
        server_id: typing.Optional[shared_pb2.UUID] = ...,
        server_http: typing.Optional[global___EndPoint] = ...,
        leader_id: typing.Optional[shared_pb2.UUID] = ...,
        leader_http: typing.Optional[global___EndPoint] = ...,
        view: builtins.int = ...,
        epoch_number: builtins.int = ...,
        epoch_position: builtins.int = ...,
        epoch_id: typing.Optional[shared_pb2.UUID] = ...,
        epoch_leader_instance_id: typing.Optional[shared_pb2.UUID] = ...,
        last_commit_position: builtins.int = ...,
        writer_checkpoint: builtins.int = ...,
        chaser_checkpoint: builtins.int = ...,
        node_priority: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "epoch_id",
            b"epoch_id",
            "epoch_leader_instance_id",
            b"epoch_leader_instance_id",
            "leader_http",
            b"leader_http",
            "leader_id",
            b"leader_id",
            "server_http",
            b"server_http",
            "server_id",
            b"server_id",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "chaser_checkpoint",
            b"chaser_checkpoint",
            "epoch_id",
            b"epoch_id",
            "epoch_leader_instance_id",
            b"epoch_leader_instance_id",
            "epoch_number",
            b"epoch_number",
            "epoch_position",
            b"epoch_position",
            "last_commit_position",
            b"last_commit_position",
            "leader_http",
            b"leader_http",
            "leader_id",
            b"leader_id",
            "node_priority",
            b"node_priority",
            "server_http",
            b"server_http",
            "server_id",
            b"server_id",
            "view",
            b"view",
            "writer_checkpoint",
            b"writer_checkpoint",
        ],
    ) -> None: ...

global___ProposalRequest = ProposalRequest

class AcceptRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVER_ID_FIELD_NUMBER: builtins.int
    SERVER_HTTP_FIELD_NUMBER: builtins.int
    LEADER_ID_FIELD_NUMBER: builtins.int
    LEADER_HTTP_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    @property
    def server_id(self) -> shared_pb2.UUID: ...
    @property
    def server_http(self) -> global___EndPoint: ...
    @property
    def leader_id(self) -> shared_pb2.UUID: ...
    @property
    def leader_http(self) -> global___EndPoint: ...
    view: builtins.int
    def __init__(
        self,
        *,
        server_id: typing.Optional[shared_pb2.UUID] = ...,
        server_http: typing.Optional[global___EndPoint] = ...,
        leader_id: typing.Optional[shared_pb2.UUID] = ...,
        leader_http: typing.Optional[global___EndPoint] = ...,
        view: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "leader_http",
            b"leader_http",
            "leader_id",
            b"leader_id",
            "server_http",
            b"server_http",
            "server_id",
            b"server_id",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "leader_http",
            b"leader_http",
            "leader_id",
            b"leader_id",
            "server_http",
            b"server_http",
            "server_id",
            b"server_id",
            "view",
            b"view",
        ],
    ) -> None: ...

global___AcceptRequest = AcceptRequest

class LeaderIsResigningRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LEADER_ID_FIELD_NUMBER: builtins.int
    LEADER_HTTP_FIELD_NUMBER: builtins.int
    @property
    def leader_id(self) -> shared_pb2.UUID: ...
    @property
    def leader_http(self) -> global___EndPoint: ...
    def __init__(
        self,
        *,
        leader_id: typing.Optional[shared_pb2.UUID] = ...,
        leader_http: typing.Optional[global___EndPoint] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "leader_http", b"leader_http", "leader_id", b"leader_id"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "leader_http", b"leader_http", "leader_id", b"leader_id"
        ],
    ) -> None: ...

global___LeaderIsResigningRequest = LeaderIsResigningRequest

class LeaderIsResigningOkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LEADER_ID_FIELD_NUMBER: builtins.int
    LEADER_HTTP_FIELD_NUMBER: builtins.int
    SERVER_ID_FIELD_NUMBER: builtins.int
    SERVER_HTTP_FIELD_NUMBER: builtins.int
    @property
    def leader_id(self) -> shared_pb2.UUID: ...
    @property
    def leader_http(self) -> global___EndPoint: ...
    @property
    def server_id(self) -> shared_pb2.UUID: ...
    @property
    def server_http(self) -> global___EndPoint: ...
    def __init__(
        self,
        *,
        leader_id: typing.Optional[shared_pb2.UUID] = ...,
        leader_http: typing.Optional[global___EndPoint] = ...,
        server_id: typing.Optional[shared_pb2.UUID] = ...,
        server_http: typing.Optional[global___EndPoint] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "leader_http",
            b"leader_http",
            "leader_id",
            b"leader_id",
            "server_http",
            b"server_http",
            "server_id",
            b"server_id",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "leader_http",
            b"leader_http",
            "leader_id",
            b"leader_id",
            "server_http",
            b"server_http",
            "server_id",
            b"server_id",
        ],
    ) -> None: ...

global___LeaderIsResigningOkRequest = LeaderIsResigningOkRequest

class ClusterInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MEMBERS_FIELD_NUMBER: builtins.int
    @property
    def members(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___MemberInfo
    ]: ...
    def __init__(
        self,
        *,
        members: typing.Optional[typing.Iterable[global___MemberInfo]] = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["members", b"members"]
    ) -> None: ...

global___ClusterInfo = ClusterInfo

class EndPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ADDRESS_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    address: typing.Text
    port: builtins.int
    def __init__(
        self,
        *,
        address: typing.Text = ...,
        port: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["address", b"address", "port", b"port"],
    ) -> None: ...

global___EndPoint = EndPoint

class MemberInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _VNodeState:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _VNodeStateEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            MemberInfo._VNodeState.ValueType
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Initializing: MemberInfo._VNodeState.ValueType  # 0
        DiscoverLeader: MemberInfo._VNodeState.ValueType  # 1
        Unknown: MemberInfo._VNodeState.ValueType  # 2
        PreReplica: MemberInfo._VNodeState.ValueType  # 3
        CatchingUp: MemberInfo._VNodeState.ValueType  # 4
        Clone: MemberInfo._VNodeState.ValueType  # 5
        Follower: MemberInfo._VNodeState.ValueType  # 6
        PreLeader: MemberInfo._VNodeState.ValueType  # 7
        Leader: MemberInfo._VNodeState.ValueType  # 8
        Manager: MemberInfo._VNodeState.ValueType  # 9
        ShuttingDown: MemberInfo._VNodeState.ValueType  # 10
        Shutdown: MemberInfo._VNodeState.ValueType  # 11
        ReadOnlyLeaderless: MemberInfo._VNodeState.ValueType  # 12
        PreReadOnlyReplica: MemberInfo._VNodeState.ValueType  # 13
        ReadOnlyReplica: MemberInfo._VNodeState.ValueType  # 14
        ResigningLeader: MemberInfo._VNodeState.ValueType  # 15

    class VNodeState(_VNodeState, metaclass=_VNodeStateEnumTypeWrapper):
        pass
    Initializing: MemberInfo.VNodeState.ValueType  # 0
    DiscoverLeader: MemberInfo.VNodeState.ValueType  # 1
    Unknown: MemberInfo.VNodeState.ValueType  # 2
    PreReplica: MemberInfo.VNodeState.ValueType  # 3
    CatchingUp: MemberInfo.VNodeState.ValueType  # 4
    Clone: MemberInfo.VNodeState.ValueType  # 5
    Follower: MemberInfo.VNodeState.ValueType  # 6
    PreLeader: MemberInfo.VNodeState.ValueType  # 7
    Leader: MemberInfo.VNodeState.ValueType  # 8
    Manager: MemberInfo.VNodeState.ValueType  # 9
    ShuttingDown: MemberInfo.VNodeState.ValueType  # 10
    Shutdown: MemberInfo.VNodeState.ValueType  # 11
    ReadOnlyLeaderless: MemberInfo.VNodeState.ValueType  # 12
    PreReadOnlyReplica: MemberInfo.VNodeState.ValueType  # 13
    ReadOnlyReplica: MemberInfo.VNodeState.ValueType  # 14
    ResigningLeader: MemberInfo.VNodeState.ValueType  # 15

    INSTANCE_ID_FIELD_NUMBER: builtins.int
    TIME_STAMP_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    IS_ALIVE_FIELD_NUMBER: builtins.int
    HTTP_END_POINT_FIELD_NUMBER: builtins.int
    INTERNAL_TCP_FIELD_NUMBER: builtins.int
    EXTERNAL_TCP_FIELD_NUMBER: builtins.int
    INTERNAL_TCP_USES_TLS_FIELD_NUMBER: builtins.int
    EXTERNAL_TCP_USES_TLS_FIELD_NUMBER: builtins.int
    LAST_COMMIT_POSITION_FIELD_NUMBER: builtins.int
    WRITER_CHECKPOINT_FIELD_NUMBER: builtins.int
    CHASER_CHECKPOINT_FIELD_NUMBER: builtins.int
    EPOCH_POSITION_FIELD_NUMBER: builtins.int
    EPOCH_NUMBER_FIELD_NUMBER: builtins.int
    EPOCH_ID_FIELD_NUMBER: builtins.int
    NODE_PRIORITY_FIELD_NUMBER: builtins.int
    IS_READ_ONLY_REPLICA_FIELD_NUMBER: builtins.int
    ADVERTISE_HOST_TO_CLIENT_AS_FIELD_NUMBER: builtins.int
    ADVERTISE_HTTP_PORT_TO_CLIENT_AS_FIELD_NUMBER: builtins.int
    ADVERTISE_TCP_PORT_TO_CLIENT_AS_FIELD_NUMBER: builtins.int
    @property
    def instance_id(self) -> shared_pb2.UUID: ...
    time_stamp: builtins.int
    state: global___MemberInfo.VNodeState.ValueType
    is_alive: builtins.bool
    @property
    def http_end_point(self) -> global___EndPoint: ...
    @property
    def internal_tcp(self) -> global___EndPoint: ...
    @property
    def external_tcp(self) -> global___EndPoint: ...
    internal_tcp_uses_tls: builtins.bool
    external_tcp_uses_tls: builtins.bool
    last_commit_position: builtins.int
    writer_checkpoint: builtins.int
    chaser_checkpoint: builtins.int
    epoch_position: builtins.int
    epoch_number: builtins.int
    @property
    def epoch_id(self) -> shared_pb2.UUID: ...
    node_priority: builtins.int
    is_read_only_replica: builtins.bool
    advertise_host_to_client_as: typing.Text
    advertise_http_port_to_client_as: builtins.int
    advertise_tcp_port_to_client_as: builtins.int
    def __init__(
        self,
        *,
        instance_id: typing.Optional[shared_pb2.UUID] = ...,
        time_stamp: builtins.int = ...,
        state: global___MemberInfo.VNodeState.ValueType = ...,
        is_alive: builtins.bool = ...,
        http_end_point: typing.Optional[global___EndPoint] = ...,
        internal_tcp: typing.Optional[global___EndPoint] = ...,
        external_tcp: typing.Optional[global___EndPoint] = ...,
        internal_tcp_uses_tls: builtins.bool = ...,
        external_tcp_uses_tls: builtins.bool = ...,
        last_commit_position: builtins.int = ...,
        writer_checkpoint: builtins.int = ...,
        chaser_checkpoint: builtins.int = ...,
        epoch_position: builtins.int = ...,
        epoch_number: builtins.int = ...,
        epoch_id: typing.Optional[shared_pb2.UUID] = ...,
        node_priority: builtins.int = ...,
        is_read_only_replica: builtins.bool = ...,
        advertise_host_to_client_as: typing.Text = ...,
        advertise_http_port_to_client_as: builtins.int = ...,
        advertise_tcp_port_to_client_as: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "epoch_id",
            b"epoch_id",
            "external_tcp",
            b"external_tcp",
            "http_end_point",
            b"http_end_point",
            "instance_id",
            b"instance_id",
            "internal_tcp",
            b"internal_tcp",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "advertise_host_to_client_as",
            b"advertise_host_to_client_as",
            "advertise_http_port_to_client_as",
            b"advertise_http_port_to_client_as",
            "advertise_tcp_port_to_client_as",
            b"advertise_tcp_port_to_client_as",
            "chaser_checkpoint",
            b"chaser_checkpoint",
            "epoch_id",
            b"epoch_id",
            "epoch_number",
            b"epoch_number",
            "epoch_position",
            b"epoch_position",
            "external_tcp",
            b"external_tcp",
            "external_tcp_uses_tls",
            b"external_tcp_uses_tls",
            "http_end_point",
            b"http_end_point",
            "instance_id",
            b"instance_id",
            "internal_tcp",
            b"internal_tcp",
            "internal_tcp_uses_tls",
            b"internal_tcp_uses_tls",
            "is_alive",
            b"is_alive",
            "is_read_only_replica",
            b"is_read_only_replica",
            "last_commit_position",
            b"last_commit_position",
            "node_priority",
            b"node_priority",
            "state",
            b"state",
            "time_stamp",
            b"time_stamp",
            "writer_checkpoint",
            b"writer_checkpoint",
        ],
    ) -> None: ...

global___MemberInfo = MemberInfo
