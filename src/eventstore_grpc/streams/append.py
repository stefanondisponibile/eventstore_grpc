"""
Append Events to Streams.
"""

import uuid
from typing import Union, List, Dict, Iterator
from eventstore_grpc import constants
from eventstore_grpc.proto import streams_pb2, streams_pb2_grpc, shared_pb2
from eventstore_grpc.event_data import EventData


def build_options(
    stream: str,
    expected_version: Union[str, int] = None,
) -> streams_pb2.AppendReq.Options:
    """Builds AppendReq Options."""
    options = streams_pb2.AppendReq.Options()
    stream_identifier = shared_pb2.StreamIdentifier()
    stream_identifier.streamName = stream.encode()
    if isinstance(expected_version, int):
        options.revision = expected_version
    elif expected_version == constants.NO_STREAM:
        options.no_stream.CopyFrom(shared_pb2.Empty())
    elif expected_version == constants.ANY:
        options.any.CopyFrom(shared_pb2.Empty())
    elif expected_version == constants.STREAM_EXISTS:
        options.stream_exists.CopyFrom(shared_pb2.Empty())
    options.stream_identifier.CopyFrom(stream_identifier)
    return options


def build_options_request(
    stream: str, expected_version: Union[str, int]
) -> streams_pb2.AppendReq:
    """Builds an Options message for AppendReq."""
    request = streams_pb2.AppendReq()
    options = build_options(stream, expected_version)
    request.options.CopyFrom(options)
    return request


def build_proposed_message_request(event: EventData):
    """Builds AppendReq Proposed Message."""
    request = streams_pb2.AppendReq()
    message = streams_pb2.AppendReq.ProposedMessage()
    message.id.string = str(getattr(event, "event_id", uuid.uuid4()))
    message.metadata["type"] = event.type
    message.metadata["content-type"] = event.data_content_type
    message.data = event.serialized_data
    message.custom_metadata = event.serialized_metadata
    request.proposed_message.CopyFrom(message)
    return request


def build_request_stream(
    stream: str,
    expected_version: Union[str, int],
    events: Union[EventData, List[EventData]],
) -> Iterator[streams_pb2.AppendReq]:
    """Builds the AppendReq stream."""
    if not isinstance(events, list):
        events = [events]
    options = build_options_request(stream, expected_version)
    proposed_messages = [build_proposed_message_request(elm) for elm in events]
    request_stream = [options, *proposed_messages]
    return iter(request_stream)


UserCredentials = Dict[str, str]


def append_to_stream(
    stub: streams_pb2_grpc.StreamsStub,
    stream: str,
    expected_version: Union[str, int],
    events: Union[EventData, List[EventData]],
    user_credentials: UserCredentials,
    **kwargs,
) -> streams_pb2.AppendResp:
    """Appends an Event to an Event Stream.

    Write one or more events to a stream, atomically. You do this by appending
    the events to the stream in one operation, or by using transations.

    Note that sending events to a non-existing stream, implicitly creates the stream.

    It is possible to make an optimistic concurrency check during the write by
    specifying the version at which you expect the stream to be.

    Identical write operations are idempotent if the optimistic concurrency check is
    not disabled.

    Args:
        stream: A string identifying the stream to which to append.
        expected_version: the version at which you expect the stream to be in order
            that an optimistic concurrency check can be performed. This should either
            be a positive integer or a string, with possible values being "NO_STREAM"
            or "EMPTY_STREAM", or "ANY" (to disable the check).
        events: event or list of events to append.
        user_credentials: specify the user on behalf whom write will be executed.
    """
    request_stream = build_request_stream(stream, expected_version, events)
    response = stub.Append(request_stream, **kwargs)

    if response.WhichOneof("result") == constants.WRONG_EXPECTED_VERSION:
        # Explicity raise an error in this case.
        handle_wrong_expected_version(response)

    return response


class WrongExpectedVersionError(Exception):
    """Occurs when an event is appended with the wrong expected version."""

    def __init__(self, expected, current, grpc_response):
        self.expected = expected
        self.current = current
        self.grpc_response = grpc_response
        self.msg = f"Current version ({current!s}) != Expected version ({expected!s})"
        super(Exception, self).__init__(self.msg)


def handle_wrong_expected_version(message: streams_pb2.AppendResp):
    """Handles append error."""
    expected_revision_option = message.wrong_expected_version.WhichOneof(
        "expected_revision_option"
    )
    expected = None
    if expected_revision_option == "expected_revision":
        expected = message.wrong_expected_version.expected_revision
    elif expected_revision_option == "expected_any":
        expected = constants.ANY
    elif expected_revision_option == "expected_stream_exists":
        expected = constants.STREAM_EXISTS
    elif expected_revision_option == "expected_no_stream":
        expected = constants.NO_STREAM
    current_revision_option = message.wrong_expected_version.WhichOneof(
        "current_revision_option"
    )
    current = None
    if current_revision_option == "current_revision":
        current = message.wrong_expected_version.current_revision
    elif current_revision_option == "current_no_stream":
        current = constants.NO_STREAM
    raise WrongExpectedVersionError(
        expected=expected, current=current, grpc_response=message
    )
