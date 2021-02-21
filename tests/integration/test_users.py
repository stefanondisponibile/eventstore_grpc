from eventstore_grpc.proto import users_pb2
from eventstore_grpc.options import SingleNodeOptions


def test_create_user(secure_client, credentials):
    login_name = "john-doe"
    password = "v3rys3cr3t!!!"
    full_name = "John Doe"
    groups = ["testers"]
    result = secure_client.create_user(
        login_name=login_name,
        password=password,
        full_name=full_name,
        groups=groups,
        credentials=credentials,
    )
    assert isinstance(result, users_pb2.CreateResp)


def test_update_user(secure_client, credentials):
    login_name = "updatable-user"
    password = "v3rys3cr3t"
    full_name = "Updatable User"
    groups = []
    secure_client.create_user(
        login_name=login_name,
        password=password,
        full_name=full_name,
        groups=groups,
        credentials=credentials,
    )
    result = secure_client.update_user(
        login_name=login_name,
        password = password,
        full_name=full_name,
        groups=["updatables"],
        credentials=credentials,
    )
    details = secure_client.get_user_details(
        login_name=login_name, credentials=credentials
    )
    assert next(details).user_details.groups == ["updatables"]
    assert isinstance(result, users_pb2.UpdateResp)


def test_delete_user(secure_client, credentials):
    login_name = "deletable-user"
    password = "v3rys3cr3t"
    full_name = "Deletable User"
    groups = []
    secure_client.create_user(
        login_name=login_name,
        password=password,
        full_name=full_name,
        groups=groups,
        credentials=credentials,
    )
    result = secure_client.delete_user(login_name=login_name, credentials=credentials)
    assert isinstance(result, users_pb2.DeleteResp)


def test_enable_user(secure_client, credentials):
    login_name = "enable-user"
    password = "v3rys3cr3t"
    full_name = "Enable User"
    groups = []
    secure_client.create_user(
        login_name=login_name,
        password=password,
        full_name=full_name,
        groups=groups,
        credentials=credentials,
    )
    result = secure_client.enable_user(login_name=login_name, credentials=credentials)
    assert isinstance(result, users_pb2.EnableResp)


def test_disable_user(secure_client, credentials):
    login_name = "disable-user"
    password = "v3rys3cr3t"
    full_name = "Disable User"
    groups = []
    secure_client.create_user(
        login_name=login_name,
        password=password,
        full_name=full_name,
        groups=groups,
        credentials=credentials,
    )
    result = secure_client.disable_user(login_name=login_name, credentials=credentials)
    assert isinstance(result, users_pb2.DisableResp)


def test_get_user_details(secure_client, credentials):
    login_name = "details-user"
    password = "v3rys3cr3t"
    full_name = "Details User"
    groups = []
    secure_client.create_user(
        login_name=login_name,
        password=password,
        full_name=full_name,
        groups=groups,
        credentials=credentials,
    )
    result = next(
        secure_client.get_user_details(login_name=login_name, credentials=credentials)
    ).user_details
    assert result.login_name == login_name and result.full_name == full_name


def test_change_user_password(secure_client, credentials):
    login_name = "change-user-password"
    password = "changeme"
    new_password = "changedit"
    full_name = "Change User Password"
    groups = []
    secure_client.create_user(
        login_name=login_name,
        password=password,
        full_name=full_name,
        groups=groups,
        credentials=credentials,
    )
    result = secure_client.change_user_password(
        login_name=login_name,
        current_password=password,
        new_password=new_password,
        credentials=credentials,
    )
    assert isinstance(result, users_pb2.ChangePasswordResp)


def test_reset_user_password(secure_client, credentials):
    login_name = "reset-user-password"
    password = "resetme"
    new_password = "new_password"
    full_name = "Reset User Password"
    groups = []
    secure_client.create_user(
        login_name=login_name,
        password=password,
        full_name=full_name,
        groups=groups,
        credentials=credentials,
    )
    result = secure_client.reset_user_password(
        login_name=login_name, new_password=new_password, credentials=credentials
    )
    assert isinstance(result, users_pb2.ResetPasswordResp)
