"""
Disable users.
"""

from eventstore_grpc.proto import users_pb2, users_pb2_grpc


def disable(
    stub: users_pb2_grpc.UsersStub, login_name: str, **kwargs
) -> users_pb2.DisableResp:
    """Disables a user."""
    request = users_pb2.DisableReq()
    options = users_pb2.DisableReq.Options()
    options.login_name = login_name
    request.options.CopyFrom(options)
    response = stub.Disable(request, **kwargs)
    return response
