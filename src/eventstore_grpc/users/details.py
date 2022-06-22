"""
Details about a user.
"""

from typing import Iterable
from eventstore_grpc.proto import users_pb2, users_pb2_grpc


def details(
    stub: users_pb2_grpc.UsersStub, login_name: str, **kwargs
) -> Iterable[users_pb2.DetailsResp]:
    """Gets details about a user."""
    request = users_pb2.DetailsReq()
    options = users_pb2.DetailsReq.Options()
    options.login_name = login_name
    request.options.CopyFrom(options)
    response = stub.Details(request, **kwargs)
    return response
