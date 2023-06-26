"""
Users Mixins.
"""

from typing import List, Optional

from eventstore_grpc import users
from eventstore_grpc.core import ClientBase
from eventstore_grpc.proto import users_pb2, users_pb2_grpc


class Users(ClientBase):
    """Handles Users Operations."""

    def create_user(
        self,
        login_name: str,
        password: str,
        full_name: str,
        groups: Optional[List[str]] = None,
        **kwargs,
    ) -> users_pb2.CreateResp:
        """Creates a new user."""
        stub = users_pb2_grpc.UsersStub(self.channel)
        if groups is None:
            groups = []
        result = users.create(
            stub,
            login_name=login_name,
            password=password,
            full_name=full_name,
            groups=groups,
            **kwargs,
        )
        return result

    def update_user(
        self,
        login_name: Optional[str] = None,
        password: Optional[str] = None,
        full_name: Optional[str] = None,
        groups: Optional[List[str]] = None,
        **kwargs,
    ) -> users_pb2.UpdateResp:
        """Updates an existing user information."""
        stub = users_pb2_grpc.UsersStub(self.channel)
        updates: dict[str, str | list[str]] = {}
        if login_name is not None:
            updates["login_name"] = login_name
        if password is not None:
            updates["password"] = password
        if full_name is not None:
            updates["full_name"] = full_name
        if groups is not None:
            updates["groups"] = groups
        if not updates:
            raise ValueError("No updates.")
        result = users.update(stub, **updates, **kwargs)  # type: ignore
        return result

    def delete_user(self, login_name: str, **kwargs) -> users_pb2.DeleteResp:
        """Deletes a user."""
        stub = users_pb2_grpc.UsersStub(self.channel)
        result = users.delete(stub, login_name=login_name, **kwargs)
        return result

    def enable_user(self, login_name: str, **kwargs) -> users_pb2.EnableResp:
        """Enables a user."""
        stub = users_pb2_grpc.UsersStub(self.channel)
        result = users.enable(stub, login_name=login_name, **kwargs)
        return result

    def disable_user(self, login_name: str, **kwargs) -> users_pb2.DisableResp:
        """Disables a user."""
        stub = users_pb2_grpc.UsersStub(self.channel)
        result = users.disable(stub, login_name=login_name, **kwargs)
        return result

    def get_user_details(self, login_name: str, **kwargs) -> users_pb2.DetailsResp:
        """Gets details about a user."""
        stub = users_pb2_grpc.UsersStub(self.channel)
        result = users.details(stub, login_name=login_name, **kwargs)
        return next(result)  # type: ignore

    def change_user_password(
        self, login_name: str, current_password: str, new_password: str, **kwargs
    ) -> users_pb2.ChangePasswordResp:
        """Changes a user's password."""
        stub = users_pb2_grpc.UsersStub(self.channel)
        result = users.change_password(
            stub,
            login_name=login_name,
            current_password=current_password,
            new_password=new_password,
            **kwargs,
        )
        return result

    def reset_user_password(
        self, login_name: str, new_password: str, **kwargs
    ) -> users_pb2.ResetPasswordResp:
        """Resets a user's password."""
        stub = users_pb2_grpc.UsersStub(self.channel)
        result = users.reset_password(
            stub, login_name=login_name, new_password=new_password, **kwargs
        )
        return result
