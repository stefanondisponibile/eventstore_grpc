"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class SupportedMethods(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    METHODS_FIELD_NUMBER: builtins.int
    EVENT_STORE_SERVER_VERSION_FIELD_NUMBER: builtins.int
    @property
    def methods(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___SupportedMethod
    ]: ...
    event_store_server_version: typing.Text
    def __init__(
        self,
        *,
        methods: typing.Optional[typing.Iterable[global___SupportedMethod]] = ...,
        event_store_server_version: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "event_store_server_version",
            b"event_store_server_version",
            "methods",
            b"methods",
        ],
    ) -> None: ...

global___SupportedMethods = SupportedMethods

class SupportedMethod(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    METHOD_NAME_FIELD_NUMBER: builtins.int
    SERVICE_NAME_FIELD_NUMBER: builtins.int
    FEATURES_FIELD_NUMBER: builtins.int
    method_name: typing.Text
    service_name: typing.Text
    @property
    def features(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        typing.Text
    ]: ...
    def __init__(
        self,
        *,
        method_name: typing.Text = ...,
        service_name: typing.Text = ...,
        features: typing.Optional[typing.Iterable[typing.Text]] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "features",
            b"features",
            "method_name",
            b"method_name",
            "service_name",
            b"service_name",
        ],
    ) -> None: ...

global___SupportedMethod = SupportedMethod
