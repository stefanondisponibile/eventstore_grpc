"""
Enable users.
"""

from eventstore_grpc.proto import users_pb2, users_pb2_grpc


def enable(
    stub: users_pb2_grpc.UsersStub, login_name: str, **kwargs
) -> users_pb2.EnableResp:
    """Enables a user."""
    request = users_pb2.EnableReq()
    options = users_pb2.EnableReq.Options()
    options.login_name = login_name
    request.options.CopyFrom(options)
    response = stub.Enable(request, **kwargs)
    return response
