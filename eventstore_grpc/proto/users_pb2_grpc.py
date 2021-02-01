# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from eventstore_grpc.proto import users_pb2 as users__pb2


class UsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/event_store.client.users.Users/Create',
                request_serializer=users__pb2.CreateReq.SerializeToString,
                response_deserializer=users__pb2.CreateResp.FromString,
                )
        self.Update = channel.unary_unary(
                '/event_store.client.users.Users/Update',
                request_serializer=users__pb2.UpdateReq.SerializeToString,
                response_deserializer=users__pb2.UpdateResp.FromString,
                )
        self.Delete = channel.unary_unary(
                '/event_store.client.users.Users/Delete',
                request_serializer=users__pb2.DeleteReq.SerializeToString,
                response_deserializer=users__pb2.DeleteResp.FromString,
                )
        self.Disable = channel.unary_unary(
                '/event_store.client.users.Users/Disable',
                request_serializer=users__pb2.DisableReq.SerializeToString,
                response_deserializer=users__pb2.DisableResp.FromString,
                )
        self.Enable = channel.unary_unary(
                '/event_store.client.users.Users/Enable',
                request_serializer=users__pb2.EnableReq.SerializeToString,
                response_deserializer=users__pb2.EnableResp.FromString,
                )
        self.Details = channel.unary_stream(
                '/event_store.client.users.Users/Details',
                request_serializer=users__pb2.DetailsReq.SerializeToString,
                response_deserializer=users__pb2.DetailsResp.FromString,
                )
        self.ChangePassword = channel.unary_unary(
                '/event_store.client.users.Users/ChangePassword',
                request_serializer=users__pb2.ChangePasswordReq.SerializeToString,
                response_deserializer=users__pb2.ChangePasswordResp.FromString,
                )
        self.ResetPassword = channel.unary_unary(
                '/event_store.client.users.Users/ResetPassword',
                request_serializer=users__pb2.ResetPasswordReq.SerializeToString,
                response_deserializer=users__pb2.ResetPasswordResp.FromString,
                )


class UsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Enable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Details(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangePassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetPassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=users__pb2.CreateReq.FromString,
                    response_serializer=users__pb2.CreateResp.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=users__pb2.UpdateReq.FromString,
                    response_serializer=users__pb2.UpdateResp.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=users__pb2.DeleteReq.FromString,
                    response_serializer=users__pb2.DeleteResp.SerializeToString,
            ),
            'Disable': grpc.unary_unary_rpc_method_handler(
                    servicer.Disable,
                    request_deserializer=users__pb2.DisableReq.FromString,
                    response_serializer=users__pb2.DisableResp.SerializeToString,
            ),
            'Enable': grpc.unary_unary_rpc_method_handler(
                    servicer.Enable,
                    request_deserializer=users__pb2.EnableReq.FromString,
                    response_serializer=users__pb2.EnableResp.SerializeToString,
            ),
            'Details': grpc.unary_stream_rpc_method_handler(
                    servicer.Details,
                    request_deserializer=users__pb2.DetailsReq.FromString,
                    response_serializer=users__pb2.DetailsResp.SerializeToString,
            ),
            'ChangePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangePassword,
                    request_deserializer=users__pb2.ChangePasswordReq.FromString,
                    response_serializer=users__pb2.ChangePasswordResp.SerializeToString,
            ),
            'ResetPassword': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetPassword,
                    request_deserializer=users__pb2.ResetPasswordReq.FromString,
                    response_serializer=users__pb2.ResetPasswordResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'event_store.client.users.Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.users.Users/Create',
            users__pb2.CreateReq.SerializeToString,
            users__pb2.CreateResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.users.Users/Update',
            users__pb2.UpdateReq.SerializeToString,
            users__pb2.UpdateResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.users.Users/Delete',
            users__pb2.DeleteReq.SerializeToString,
            users__pb2.DeleteResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.users.Users/Disable',
            users__pb2.DisableReq.SerializeToString,
            users__pb2.DisableResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Enable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.users.Users/Enable',
            users__pb2.EnableReq.SerializeToString,
            users__pb2.EnableResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Details(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/event_store.client.users.Users/Details',
            users__pb2.DetailsReq.SerializeToString,
            users__pb2.DetailsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.users.Users/ChangePassword',
            users__pb2.ChangePasswordReq.SerializeToString,
            users__pb2.ChangePasswordResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetPassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/event_store.client.users.Users/ResetPassword',
            users__pb2.ResetPasswordReq.SerializeToString,
            users__pb2.ResetPasswordResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
