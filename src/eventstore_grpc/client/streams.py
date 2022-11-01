"""
Streams Mixins.
"""

from typing import Dict, List, Union

from eventstore_grpc import constants, event_data
from eventstore_grpc.core import ClientBase
from eventstore_grpc.proto import streams_pb2, streams_pb2_grpc
from eventstore_grpc.streams import append, delete, read, tombstone


class Streams(ClientBase):
    """Handles streams operations."""

    def append_to_stream(
        self,
        stream: str,
        events: Union[event_data.EventData, List[event_data.EventData]],
        expected_version: Union[str, int] = constants.ANY,
        user_credentials: append.UserCredentials = None,
        **kwargs
    ) -> streams_pb2.AppendResp:
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
        options: dict = None,
        **kwargs
    ):
        """Reads events from a stream."""
        options = options or {}
        if options.get("from_revision") is None:
            options["from_revision"] = from_revision
        stub = streams_pb2_grpc.StreamsStub(self.channel)
        result = read.read_from_stream(
            stub, stream=stream, count=count, options=options, **kwargs
        )
        return result

    def read_from_all(
        self,
        from_position: Union[Dict[str, int], str] = constants.START,
        count: int = None,
        direction: str = None,
        **kwargs
    ):
        stub = streams_pb2_grpc.StreamsStub(self.channel)
        result = read.read_from_all(
            stub,
            from_position=from_position,
            count=count,
            direction=direction,
            **kwargs
        )
        return result

    def delete_stream(
        self, stream: str, expected_version: Union[int, str] = constants.ANY, **kwargs
    ):
        """Deletes a stream."""
        stub = streams_pb2_grpc.StreamsStub(self.channel)
        result = delete.delete_stream(
            stub, stream=stream, expected_version=expected_version, **kwargs
        )
        return result

    def tombstone_stream(
        self, stream: str, expected_version: Union[int, str], **kwargs
    ):
        """Tombstones a stream."""
        stub = streams_pb2_grpc.StreamsStub(self.channel)
        result = tombstone.tombstone_stream(
            stub, stream=stream, expected_version=expected_version, **kwargs
        )
        return result
