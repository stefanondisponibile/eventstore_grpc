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

class CreateReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Options(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        LOGIN_NAME_FIELD_NUMBER: builtins.int
        PASSWORD_FIELD_NUMBER: builtins.int
        FULL_NAME_FIELD_NUMBER: builtins.int
        GROUPS_FIELD_NUMBER: builtins.int
        login_name: typing.Text
        password: typing.Text
        full_name: typing.Text
        @property
        def groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
        def __init__(self,
            *,
            login_name: typing.Text = ...,
            password: typing.Text = ...,
            full_name: typing.Text = ...,
            groups: typing.Optional[typing.Iterable[typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["full_name",b"full_name","groups",b"groups","login_name",b"login_name","password",b"password"]) -> None: ...

    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___CreateReq.Options: ...
    def __init__(self,
        *,
        options: typing.Optional[global___CreateReq.Options] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options"]) -> None: ...
global___CreateReq = CreateReq

class CreateResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___CreateResp = CreateResp

class UpdateReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Options(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        LOGIN_NAME_FIELD_NUMBER: builtins.int
        PASSWORD_FIELD_NUMBER: builtins.int
        FULL_NAME_FIELD_NUMBER: builtins.int
        GROUPS_FIELD_NUMBER: builtins.int
        login_name: typing.Text
        password: typing.Text
        full_name: typing.Text
        @property
        def groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
        def __init__(self,
            *,
            login_name: typing.Text = ...,
            password: typing.Text = ...,
            full_name: typing.Text = ...,
            groups: typing.Optional[typing.Iterable[typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["full_name",b"full_name","groups",b"groups","login_name",b"login_name","password",b"password"]) -> None: ...

    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___UpdateReq.Options: ...
    def __init__(self,
        *,
        options: typing.Optional[global___UpdateReq.Options] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options"]) -> None: ...
global___UpdateReq = UpdateReq

class UpdateResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___UpdateResp = UpdateResp

class DeleteReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Options(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        LOGIN_NAME_FIELD_NUMBER: builtins.int
        login_name: typing.Text
        def __init__(self,
            *,
            login_name: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["login_name",b"login_name"]) -> None: ...

    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___DeleteReq.Options: ...
    def __init__(self,
        *,
        options: typing.Optional[global___DeleteReq.Options] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options"]) -> None: ...
global___DeleteReq = DeleteReq

class DeleteResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___DeleteResp = DeleteResp

class EnableReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Options(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        LOGIN_NAME_FIELD_NUMBER: builtins.int
        login_name: typing.Text
        def __init__(self,
            *,
            login_name: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["login_name",b"login_name"]) -> None: ...

    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___EnableReq.Options: ...
    def __init__(self,
        *,
        options: typing.Optional[global___EnableReq.Options] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options"]) -> None: ...
global___EnableReq = EnableReq

class EnableResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___EnableResp = EnableResp

class DisableReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Options(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        LOGIN_NAME_FIELD_NUMBER: builtins.int
        login_name: typing.Text
        def __init__(self,
            *,
            login_name: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["login_name",b"login_name"]) -> None: ...

    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___DisableReq.Options: ...
    def __init__(self,
        *,
        options: typing.Optional[global___DisableReq.Options] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options"]) -> None: ...
global___DisableReq = DisableReq

class DisableResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___DisableResp = DisableResp

class DetailsReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Options(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        LOGIN_NAME_FIELD_NUMBER: builtins.int
        login_name: typing.Text
        def __init__(self,
            *,
            login_name: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["login_name",b"login_name"]) -> None: ...

    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___DetailsReq.Options: ...
    def __init__(self,
        *,
        options: typing.Optional[global___DetailsReq.Options] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options"]) -> None: ...
global___DetailsReq = DetailsReq

class DetailsResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class UserDetails(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class DateTime(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            TICKS_SINCE_EPOCH_FIELD_NUMBER: builtins.int
            ticks_since_epoch: builtins.int
            def __init__(self,
                *,
                ticks_since_epoch: builtins.int = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["ticks_since_epoch",b"ticks_since_epoch"]) -> None: ...

        LOGIN_NAME_FIELD_NUMBER: builtins.int
        FULL_NAME_FIELD_NUMBER: builtins.int
        GROUPS_FIELD_NUMBER: builtins.int
        LAST_UPDATED_FIELD_NUMBER: builtins.int
        DISABLED_FIELD_NUMBER: builtins.int
        login_name: typing.Text
        full_name: typing.Text
        @property
        def groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
        @property
        def last_updated(self) -> global___DetailsResp.UserDetails.DateTime: ...
        disabled: builtins.bool
        def __init__(self,
            *,
            login_name: typing.Text = ...,
            full_name: typing.Text = ...,
            groups: typing.Optional[typing.Iterable[typing.Text]] = ...,
            last_updated: typing.Optional[global___DetailsResp.UserDetails.DateTime] = ...,
            disabled: builtins.bool = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["last_updated",b"last_updated"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["disabled",b"disabled","full_name",b"full_name","groups",b"groups","last_updated",b"last_updated","login_name",b"login_name"]) -> None: ...

    USER_DETAILS_FIELD_NUMBER: builtins.int
    @property
    def user_details(self) -> global___DetailsResp.UserDetails: ...
    def __init__(self,
        *,
        user_details: typing.Optional[global___DetailsResp.UserDetails] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user_details",b"user_details"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_details",b"user_details"]) -> None: ...
global___DetailsResp = DetailsResp

class ChangePasswordReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Options(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        LOGIN_NAME_FIELD_NUMBER: builtins.int
        CURRENT_PASSWORD_FIELD_NUMBER: builtins.int
        NEW_PASSWORD_FIELD_NUMBER: builtins.int
        login_name: typing.Text
        current_password: typing.Text
        new_password: typing.Text
        def __init__(self,
            *,
            login_name: typing.Text = ...,
            current_password: typing.Text = ...,
            new_password: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["current_password",b"current_password","login_name",b"login_name","new_password",b"new_password"]) -> None: ...

    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___ChangePasswordReq.Options: ...
    def __init__(self,
        *,
        options: typing.Optional[global___ChangePasswordReq.Options] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options"]) -> None: ...
global___ChangePasswordReq = ChangePasswordReq

class ChangePasswordResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___ChangePasswordResp = ChangePasswordResp

class ResetPasswordReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Options(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        LOGIN_NAME_FIELD_NUMBER: builtins.int
        NEW_PASSWORD_FIELD_NUMBER: builtins.int
        login_name: typing.Text
        new_password: typing.Text
        def __init__(self,
            *,
            login_name: typing.Text = ...,
            new_password: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["login_name",b"login_name","new_password",b"new_password"]) -> None: ...

    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___ResetPasswordReq.Options: ...
    def __init__(self,
        *,
        options: typing.Optional[global___ResetPasswordReq.Options] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options"]) -> None: ...
global___ResetPasswordReq = ResetPasswordReq

class ResetPasswordResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___ResetPasswordResp = ResetPasswordResp