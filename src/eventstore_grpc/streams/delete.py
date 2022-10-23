"""
Streams Delete requests.
"""

from typing import Union
from eventstore_grpc.proto import streams_pb2, streams_pb2_grpc, shared_pb2
from eventstore_grpc import constants


def delete_stream(
    stub: streams_pb2_grpc.StreamsStub,
    stream: str,
    expected_version: Union[str, int],
    **kwargs
) -> streams_pb2.DeleteResp:
    """Deletes a stream."""
    request = streams_pb2.DeleteReq()
    options = streams_pb2.DeleteReq.Options()
    stream_identifier = shared_pb2.StreamIdentifier()
    stream_identifier.stream_name = stream.encode()
    if expected_version == constants.NO_STREAM:
        options.no_stream.CopyFrom(shared_pb2.Empty())
    elif expected_version == constants.ANY:
        options.any.CopyFrom(shared_pb2.Empty())
    elif expected_version == constants.STREAM_EXISTS:
        options.stream_exists.CopyFrom(shared_pb2.Empty())
    elif isinstance(expected_version, int):
        options.stream_exists = expected_version
    options.stream_identifier.CopyFrom(stream_identifier)
    request.options.CopyFrom(options)
    response = stub.Delete(request, **kwargs)
    return response
