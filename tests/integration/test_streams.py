import json
import uuid
import eventstore_grpc


def test_append_to_stream(client):
    event_id = uuid.uuid4()
    stream = "some-new-stream"
    expected_version = eventstore_grpc.constants.NO_STREAM
    event = eventstore_grpc.JSONEventData(
        type="some-event",
        data={"foo": "bar"},
        metadata={"is_test": True},
        event_id=event_id,
    )
    result = client.append_to_stream(
        stream=stream, expected_version=expected_version, events=event
    )
    assert result.HasField("success")
    assert result.success.current_revision == 0


def test_read_from_stream(client):
    event_1_id = str(uuid.uuid4())
    event_2_id = str(uuid.uuid4())
    stream = "some-stream-to-read-from"
    expected_version = eventstore_grpc.constants.NO_STREAM
    event_1 = eventstore_grpc.JSONEventData(
        type="first-event",
        data={"foo": "bar"},
        metadata={"is_test": True},
        event_id=event_1_id,
    )
    event_2 = eventstore_grpc.JSONEventData(
        type="second-event",
        data={"foo": "bar"},
        metadata={"is_test": True},
        event_id=event_2_id,
    )
    events = [event_1, event_2]
    client.append_to_stream(
        stream=stream, expected_version=expected_version, events=events
    )
    result = client.read_from_stream(
        stream=stream,
        count=2,
        from_revision=eventstore_grpc.constants.START,
        options={"direction": eventstore_grpc.constants.FORWARDS},
    )
    for i, elm in enumerate(result):
        assert events[i].event_id == elm.event.event.id.string
        assert events[i].type == elm.event.event.metadata["type"]
        assert events[i].data == json.loads(elm.event.event.data)
        assert events[i].metadata == json.loads(elm.event.event.custom_metadata)
