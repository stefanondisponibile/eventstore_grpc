from distutils.filelist import translate_pattern
import json
import uuid

import pytest
from eventstore_grpc import constants
from eventstore_grpc.client import streams
from eventstore_grpc.core.transport import Transport
from eventstore_grpc.event_data import JSONEventData
from eventstore_grpc.streams.append import WrongExpectedVersionError


@pytest.mark.integration
@pytest.mark.parametrize(
    "expected_version", (0, constants.ANY, constants.NO_STREAM, constants.STREAM_EXISTS)
)
def test_append_to_stream(transport: Transport, expected_version: int | str) -> None:
    client = streams.Streams(transport=transport)
    stream = "some-stream"
    data = {"data-key": "data-value"}
    event = JSONEventData(type="some-event", data=data)
    if expected_version == constants.STREAM_EXISTS:
        client.append_to_stream(
            stream=stream, expected_version=constants.ANY, events=event
        )
    if expected_version == 0:
        with pytest.raises(WrongExpectedVersionError):
            client.append_to_stream(
                stream=stream,
                expected_version=expected_version,
                events=event,
            )
    else:
        result = client.append_to_stream(
            stream=stream,
            expected_version=expected_version,
            events=event,
        )
        assert isinstance(result, streams.streams_pb2.AppendResp)
        assert isinstance(result.success, streams.streams_pb2.AppendResp.Success)
        assert isinstance(result.success.current_revision, int)
        client.delete_stream(stream=stream, expected_version=constants.ANY)


@pytest.mark.integration
@pytest.mark.parametrize(
    "from_revision,direction",
    [
        (constants.START, constants.FORWARDS),
        (constants.END, constants.BACKWARDS),
        (0, constants.FORWARDS),
        (None, constants.FORWARDS),
    ],
)
def test_read_from_stream(
    transport: Transport, from_revision: int | str, direction: str
) -> None:
    client = streams.Streams(transport=transport)
    stream = "some-stream"
    event_type = "some-event-type"
    event_data = {"some": "data"}
    event_metadata = {"some": "metadata"}
    event = JSONEventData(type=event_type, data=event_data, metadata=event_metadata)
    client.append_to_stream(stream=stream, expected_version=constants.ANY, events=event)
    options = {
        "from_revision": from_revision,
        "direction": direction,
    }
    resp = client.read_from_stream(stream=stream, options=options)
    for event in resp:
        assert isinstance(event, streams.streams_pb2.ReadResp)
        assert json.loads(event.event.event.custom_metadata) == event_metadata
        assert json.loads(event.event.event.data) == event_data
    client.delete_stream(stream=stream, expected_version=constants.ANY)


@pytest.mark.integration
@pytest.mark.parametrize(
    "expected_version", (0, constants.ANY, constants.STREAM_EXISTS, constants.NO_STREAM)
)
def test_delete_stream(transport: Transport, expected_version: int | str) -> None:
    client = streams.Streams(transport=transport)
    stream = str(uuid.uuid1())
    event_type = "some-event-type"
    event_data = {"some": "data"}
    event = JSONEventData(type=event_type, data=event_data)
    if expected_version != constants.NO_STREAM:
        client.append_to_stream(
            stream=stream, expected_version=constants.ANY, events=event
        )
    if isinstance(expected_version, int) or expected_version == constants.NO_STREAM:
        with pytest.raises(Exception):
            client.delete_stream(stream=stream, expected_version=expected_version)
    else:
        response = client.delete_stream(stream=stream, expected_version=expected_version)
        assert isinstance(response, streams.streams_pb2.DeleteResp)


@pytest.mark.integration
@pytest.mark.parametrize(
    "expected_version",
    [
        constants.ANY,
        constants.STREAM_EXISTS,
        constants.NO_STREAM,
    ],
)
def test_tombstone_stream(transport: Transport, expected_version: str) -> None:
    client = streams.Streams(transport=transport)
    stream = str(uuid.uuid1())
    event_type = "some-event-type"
    event_data = {"some": "data"}
    event = JSONEventData(type=event_type, data=event_data)
    if expected_version != constants.NO_STREAM:
        client.append_to_stream(
            stream=stream, expected_version=constants.ANY, events=event
        )
    response = client.tombstone_stream(stream=stream, expected_version=expected_version)
    assert isinstance(response, streams.streams_pb2.TombstoneResp)


@pytest.mark.integration
@pytest.mark.parametrize(
    "count,from_position,direction",
    [
        (1, constants.START, constants.FORWARDS),
        (2, constants.END, constants.BACKWARDS),
        (3, {"commit_position": 0, "prepare_position": 0}, constants.FORWARDS),
    ],
)
def test_read_from_all(
    transport: Transport,
    count: int,
    from_position: int | dict[str, int],
    direction: str,
) -> None:
    client = streams.Streams(transport=transport)
    events = list(
        client.read_from_all(
            count=count,
            from_position=from_position,
            direction=direction,
        )
    )
    assert len(events) == count
    assert all(isinstance(event, streams.streams_pb2.ReadResp) for event in events)


@pytest.mark.integration
def test_read_from_all_when_invalid_position(transport: Transport) -> None:
    client = streams.Streams(transport=transport)
    with pytest.raises(ValueError):
        client.read_from_all(from_position=1234567890)


@pytest.mark.integration
def test_read_from_all_with_invalid_direction(transport: Transport) -> None:
    client = streams.Streams(transport=transport)
    with pytest.raises(ValueError):
        client.read_from_all(direction="WRONG")
