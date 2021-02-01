"""
Streams Mixins.
"""

from typing import Union, List
from eventstore_grpc.streams import append, read, delete, tombstone
from eventstore_grpc import event_data, constants
from eventstore_grpc.proto import streams_pb2_grpc


class Streams:
    """Handles streams operations."""

    def append_to_stream(
        self,
        stream: str,
        expected_version: Union[str, int],
        events: Union[event_data.EventData, List[event_data.EventData]],
        user_credentials: append.UserCredentials = None,
        **kwargs
    ):
        """Appends new events to a stream."""
        stub = streams_pb2_grpc.StreamsStub(self.channel)
        result = append.append_to_stream(
            stub,
            stream=stream,
            expected_version=expected_version,
            events=events,
            user_credentials=user_credentials,
            **kwargs
        )
        return result

    def read_from_stream(
        self,
        stream: str,
        count: int = None,
        from_revision: Union[int, str] = constants.START,
        options: dict = {},
        **kwargs
    ):
        """Reads events from a stream."""
        options.update(
            {"from_revision": from_revision}
        )  # TODO: Also the functional api should use from_revision as a param. (and maybe all the options?)
        stub = streams_pb2_grpc.StreamsStub(self.channel)
        result = read.read_stream(stub, stream=stream, count=count, options=options, **kwargs)
        return result

    def delete_stream(
        self,
        stream: str,
        expected_version: Union[int, str],
        **kwargs
    ):
        """Deletes a stream."""
        stub = streams_pb2_grpc.StreamsStub(self.channel)
        result = delete.delete_stream(
            stub, stream=stream, expected_version=expected_version, **kwargs
        )
        return result

    def tombstone_stream(
        self,
        stream: str,
        expected_version: Union[int, str],
        **kwargs
    ):
        """Tombstones a stream."""
        stub = streams_pb2_grpc.StreamsStub(self.channel)
        result = tombstone.tombstone_stream(
            stub, stream=stream, expected_version=expected_version, **kwargs
        )
        return result
