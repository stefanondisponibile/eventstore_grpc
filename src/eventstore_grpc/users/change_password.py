"""
Change user's password.
"""

from eventstore_grpc.proto import users_pb2, users_pb2_grpc


def change_password(
    stub: users_pb2_grpc.UsersStub,
    login_name: str,
    current_password: str,
    new_password: str,
    **kwargs,
) -> users_pb2.ChangePasswordResp:
    """Changes user's password."""
    request = users_pb2.ChangePasswordReq()
    options = users_pb2.ChangePasswordReq.Options()
    options.login_name = login_name
    options.current_password = current_password
    options.new_password = new_password
    request.options.CopyFrom(options)
    response = stub.ChangePassword(request, **kwargs)
    return response
