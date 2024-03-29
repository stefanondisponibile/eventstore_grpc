"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import code_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Status(google.protobuf.message.Message):
    """The `Status` type defines a logical error model that is suitable for
    different programming environments, including REST APIs and RPC APIs. It is
    used by [gRPC](https://github.com/grpc). Each `Status` message contains
    three pieces of data: error code, error message, and error details.

    You can find out more about this error model and how to work with it in the
    [API Design Guide](https://cloud.google.com/apis/design/errors).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    DETAILS_FIELD_NUMBER: builtins.int
    code: code_pb2.Code.ValueType
    """The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code]."""

    message: typing.Text
    """A developer-facing error message, which should be in English. Any
    user-facing error message should be localized and sent in the
    [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.
    """

    @property
    def details(self) -> google.protobuf.any_pb2.Any:
        """A list of messages that carry the error details.  There is a common set of
        message types for APIs to use.
        """
        pass
    def __init__(
        self,
        *,
        code: code_pb2.Code.ValueType = ...,
        message: typing.Text = ...,
        details: typing.Optional[google.protobuf.any_pb2.Any] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["details", b"details"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "code", b"code", "details", b"details", "message", b"message"
        ],
    ) -> None: ...

global___Status = Status
