"""
Delete users.
"""

from eventstore_grpc.proto import users_pb2, users_pb2_grpc


def delete(
    stub: users_pb2_grpc.UsersStub, login_name: str, **kwargs
) -> users_pb2.DeleteResp:
    """Deletes a user."""
    request = users_pb2.DeleteReq()
    options = users_pb2.DeleteReq.Options()
    options.login_name = login_name
    request.options.CopyFrom(options)
    response = stub.Delete(request, **kwargs)
    return response
