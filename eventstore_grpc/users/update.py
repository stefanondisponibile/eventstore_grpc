"""
Updates a User.
"""

from typing import List
from eventstore_grpc.proto import users_pb2, users_pb2_grpc


def update(
    stub: users_pb2_grpc.UsersStub,
    login_name: str = None,
    password: str = None,
    full_name: str = None,
    groups: List[str] = None,
    **kwargs

) -> users_pb2.UpdateResp:
    """Updates a user."""
    request = users_pb2.UpdateReq()
    options = users_pb2.UpdateReq.Options()
    if login_name is not None:
        options.login_name = login_name
    if password is not None:
        options.password = password
    if full_name is not None:
        options.full_name = full_name
    if groups is not None:
        for group in groups:
            options.groups.append(group)
    response = stub.Update(request, **kwargs)
    return response
