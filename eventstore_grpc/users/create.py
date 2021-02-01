"""
Create a User.
"""

from typing import List
from eventstore_grpc.proto import users_pb2, users_pb2_grpc


def create(
    stub: users_pb2_grpc.UsersStub,
    login_name: str,
    password: str,
    full_name: str,
    groups: List[str],
    **kwargs,
) -> users_pb2.CreateResp:
    """Creates a user."""
    request = users_pb2.CreateReq()
    options = users_pb2.CreateReq.Options()
    options.login_name = login_name
    options.password = password
    options.full_name = full_name
    for group in groups:
        options.groups.append(group)
    request.options.CopyFrom(options)
    response = stub.Create(request, **kwargs)
    return response
