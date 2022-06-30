"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class StartScavengeReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Options(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        THREAD_COUNT_FIELD_NUMBER: builtins.int
        START_FROM_CHUNK_FIELD_NUMBER: builtins.int
        thread_count: builtins.int
        start_from_chunk: builtins.int
        def __init__(self,
            *,
            thread_count: builtins.int = ...,
            start_from_chunk: builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["start_from_chunk",b"start_from_chunk","thread_count",b"thread_count"]) -> None: ...

    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___StartScavengeReq.Options: ...
    def __init__(self,
        *,
        options: typing.Optional[global___StartScavengeReq.Options] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options"]) -> None: ...
global___StartScavengeReq = StartScavengeReq

class StopScavengeReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Options(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        SCAVENGE_ID_FIELD_NUMBER: builtins.int
        scavenge_id: typing.Text
        def __init__(self,
            *,
            scavenge_id: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["scavenge_id",b"scavenge_id"]) -> None: ...

    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___StopScavengeReq.Options: ...
    def __init__(self,
        *,
        options: typing.Optional[global___StopScavengeReq.Options] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options"]) -> None: ...
global___StopScavengeReq = StopScavengeReq

class ScavengeResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _ScavengeResult:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ScavengeResultEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ScavengeResp._ScavengeResult.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Started: ScavengeResp._ScavengeResult.ValueType  # 0
        InProgress: ScavengeResp._ScavengeResult.ValueType  # 1
        Stopped: ScavengeResp._ScavengeResult.ValueType  # 2
    class ScavengeResult(_ScavengeResult, metaclass=_ScavengeResultEnumTypeWrapper):
        pass

    Started: ScavengeResp.ScavengeResult.ValueType  # 0
    InProgress: ScavengeResp.ScavengeResult.ValueType  # 1
    Stopped: ScavengeResp.ScavengeResult.ValueType  # 2

    SCAVENGE_ID_FIELD_NUMBER: builtins.int
    SCAVENGE_RESULT_FIELD_NUMBER: builtins.int
    scavenge_id: typing.Text
    scavenge_result: global___ScavengeResp.ScavengeResult.ValueType
    def __init__(self,
        *,
        scavenge_id: typing.Text = ...,
        scavenge_result: global___ScavengeResp.ScavengeResult.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["scavenge_id",b"scavenge_id","scavenge_result",b"scavenge_result"]) -> None: ...
global___ScavengeResp = ScavengeResp

class SetNodePriorityReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PRIORITY_FIELD_NUMBER: builtins.int
    priority: builtins.int
    def __init__(self,
        *,
        priority: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["priority",b"priority"]) -> None: ...
global___SetNodePriorityReq = SetNodePriorityReq
