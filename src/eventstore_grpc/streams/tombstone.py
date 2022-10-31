"""
Tombstone stream.
"""

from typing import Union

from eventstore_grpc import constants
from eventstore_grpc.proto import shared_pb2, streams_pb2, streams_pb2_grpc


def tombstone_stream(
    stub: streams_pb2_grpc.StreamsStub,
    stream: str,
    expected_version: Union[int, str],
    **kwargs,
):
    """Tombstone."""
    request = streams_pb2.TombstoneReq()
    options = streams_pb2.TombstoneReq.Options()
    options.stream_identifier.CopyFrom(
        shared_pb2.StreamIdentifier(stream_name=stream.encode("UTF-8"))
    )
    if expected_version == constants.ANY:
        options.any.CopyFrom(shared_pb2.Empty())
    elif expected_version == constants.NO_STREAM:
        options.no_stream.CopyFrom(shared_pb2.Empty())
    elif expected_version == constants.STREAM_EXISTS:
        options.stream_exists.CopyFrom(shared_pb2.Empty())
    request.options.CopyFrom(options)
    response = stub.Tombstone(request, **kwargs)
    return response
