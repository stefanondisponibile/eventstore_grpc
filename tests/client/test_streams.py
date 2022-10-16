import json
import uuid

import pytest
from eventstore_grpc import constants
from eventstore_grpc.client import streams
from eventstore_grpc.core.transport import Transport
from eventstore_grpc.event_data import JSONEventData


@pytest.mark.integration
def test_append_to_stream(transport: Transport) -> None:
    client = streams.Streams(transport=transport)
    stream = "some-stream"
    expected_version = constants.ANY
    data = {"data-key": "data-value"}
    event = JSONEventData(type="some-event", data=data)
    result = client.append_to_stream(
        stream=stream,
        expected_version=expected_version,
        events=event,
    )
    assert isinstance(result, streams.streams_pb2.AppendResp)
    assert isinstance(result.success, streams.streams_pb2.AppendResp.Success)
    assert isinstance(result.success.current_revision, int)
    client.delete_stream(stream=stream, expected_version=constants.ANY)


def test_read_from_stream(transport: Transport) -> None:
    client = streams.Streams(transport=transport)
    stream = "some-stream"
    event_type = "some-event-type"
    event_data = {"some": "data"}
    event_metadata = {"some": "metadata"}
    event = JSONEventData(type=event_type, data=event_data, metadata=event_metadata)
    client.append_to_stream(stream=stream, expected_version=constants.ANY, events=event)
    resp = client.read_from_stream(stream=stream)
    for event in resp:
        assert isinstance(event, streams.streams_pb2.ReadResp)
        assert json.loads(event.event.event.custom_metadata) == event_metadata
        assert json.loads(event.event.event.data) == event_data
    client.delete_stream(stream=stream, expected_version=constants.ANY)


def test_tombstone_stream(transport: Transport) -> None:
    client = streams.Streams(transport=transport)
    stream = f"tombstone-stream-{uuid.uuid1()}"
    event_type = "some-event-type"
    event_data = {"some": "data"}
    event = JSONEventData(type=event_type, data=event_data)
    client.append_to_stream(stream=stream, expected_version=constants.ANY, events=event)
    response = client.tombstone_stream(stream=stream, expected_version=constants.ANY)
    assert isinstance(response, streams.streams_pb2.TombstoneResp)

@pytest.mark.integration
@pytest.mark.parametrize("count", [1,2])
def test_read_from_all(transport: Transport, count: int) -> None:
    client = streams.Streams(transport=transport)
    events = list(client.read_from_all(from_position=constants.START, count=count))
    assert len(events) == count
    assert all(isinstance(event, streams.streams_pb2.ReadResp) for event in events)
