"""
Reset user's passwords.
"""

from eventstore_grpc.proto import users_pb2, users_pb2_grpc


def reset_password(
    stub: users_pb2_grpc.UsersStub, login_name: str, new_password: str, **kwargs
) -> users_pb2.ResetPasswordResp:
    """Resets user's password."""
    request = users_pb2.ResetPasswordReq()
    options = users_pb2.ResetPasswordReq.Options()
    options.login_name = login_name
    options.new_password = new_password
    request.options.CopyFrom(options)
    response = stub.ResetPassword(request, **kwargs)
    return response
