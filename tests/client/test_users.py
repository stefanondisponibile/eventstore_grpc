import pytest

from eventstore_grpc.client import users
from eventstore_grpc.core.transport import Transport


@pytest.fixture
def client(transport: Transport) -> users.Users:
    return users.Users(transport=transport)


@pytest.mark.integration
@pytest.mark.parametrize(
    "request_params",
    [
        {
            "login_name": "created-user-1",
            "password": "created-user-1-password",
            "full_name": "created-user-1-full_name",
        },
        {
            "login_name": "created-user-2",
            "password": "created-user-2-password",
            "full_name": "created-user-2-full_name",
            "groups": ["created-user-1-group-1", "created-user-1-group-2"],
        },
    ],
)
def test_create_users(client: users.Users, request_params: dict) -> None:
    result = client.create_user(**request_params)
    assert isinstance(result, users.users_pb2.CreateResp)
    client.delete_user(login_name=request_params["login_name"])


@pytest.mark.integration
@pytest.mark.parametrize(
    "create_params",
    [
        {
            "login_name": "updated-user-1",
            "password": "updated-user-1-password",
            "full_name": "updated-user-1-full_name",
        },
        {
            "login_name": "updated-user-2",
            "password": "updated-user-2-password",
            "full_name": "updated-user-2-full_name",
            "groups": ["updated-user-2-group-1", "updated-user-2-group-2"],
        },
    ],
)
def test_update_user(client: users.Users, create_params: dict) -> None:
    client.create_user(**create_params)
    update_params = {}
    for k in create_params:
        if isinstance(create_params[k], str) and k != "login_name":
            update_params[k] = create_params[k] + "-UPDATED"
        elif isinstance(create_params[k], list):
            update_params[k] = [elm + "-UPDATED" for elm in create_params[k]]
        else:
            update_params[k] = create_params[k]
    result = client.update_user(**update_params)
    assert isinstance(result, users.users_pb2.UpdateResp)
    client.delete_user(login_name=create_params["login_name"])


@pytest.mark.integration
def test_update_with_no_updates(client: users.Users) -> None:
    with pytest.raises(ValueError):
        client.update_user()


@pytest.mark.integration
def test_delete_user(client: users.Users) -> None:
    login_name = "deleted-user-1"
    client.create_user(
        login_name=login_name,
        password="deleted-user-1-password",
        full_name="deleted-user-1-full_name",
    )
    result = client.delete_user(login_name=login_name)
    assert isinstance(result, users.users_pb2.DeleteResp)


@pytest.mark.integration
def test_enable_user(client: users.Users) -> None:
    login_name = "enabled-user-1"
    client.create_user(
        login_name=login_name,
        password=login_name + "-password",
        full_name=login_name + "-full_name",
    )
    result = client.enable_user(login_name=login_name)
    assert isinstance(result, users.users_pb2.EnableResp)
    client.delete_user(login_name=login_name)


@pytest.mark.integration
def test_disable_user(client: users.Users) -> None:
    login_name = "disabled-user-1"
    client.create_user(
        login_name=login_name,
        password=login_name + "-password",
        full_name=login_name + "-full_name",
    )
    result = client.disable_user(login_name=login_name)
    assert isinstance(result, users.users_pb2.DisableResp)
    client.delete_user(login_name=login_name)


@pytest.mark.integration
def test_get_user_details(client: users.Users) -> None:
    login_name = "detailed-user-1"
    full_name = login_name + "-full_name"
    n_groups = 2
    groups = [login_name + f"-group-{i + 1}" for i in range(n_groups)]
    client.create_user(
        login_name=login_name,
        password=login_name + "-password",
        full_name=full_name,
        groups=groups,
    )
    result = client.get_user_details(login_name=login_name)
    user_details = result.user_details
    assert user_details.login_name == login_name
    assert user_details.full_name == full_name
    assert user_details.disabled == False
    client.delete_user(login_name=login_name)


@pytest.mark.integration
def test_change_user_password(client: users.Users) -> None:
    login_name = "changepassword-user-1"
    password = login_name + "-password"
    full_name = login_name + "-full_name"
    n_groups = 2
    groups = [login_name + f"-group-{i + 1}" for i in range(n_groups)]
    client.create_user(
        login_name=login_name,
        password=password,
        full_name=full_name,
        groups=groups,
    )
    new_password = "new-password"
    result = client.change_user_password(
        login_name=login_name, current_password=password, new_password=new_password
    )
    assert isinstance(result, users.users_pb2.ChangePasswordResp)
    client.delete_user(login_name=login_name)


@pytest.mark.integration
def test_reset_user_password(client: users.Users) -> None:
    login_name = "resetpassword-user-1"
    password = login_name + "-password"
    full_name = login_name + "-full_name"
    n_groups = 2
    groups = [login_name + f"-group-{i + 1}" for i in range(n_groups)]
    client.create_user(
        login_name=login_name, password=password, full_name=full_name, groups=groups
    )
    new_password = password + "-NEW"
    result = client.reset_user_password(
        login_name=login_name, new_password=new_password
    )
    assert isinstance(result, users.users_pb2.ResetPasswordResp)
    client.delete_user(login_name=login_name)
