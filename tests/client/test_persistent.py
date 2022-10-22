import pytest
from eventstore_grpc.core import Transport
from eventstore_grpc.client import persistent
from eventstore_grpc.client import streams
from eventstore_grpc.constants import ANY
from eventstore_grpc.event_data import JSONEventData
import uuid
import time


@pytest.mark.integration
def test_create_persistent_subscription(transport: Transport) -> None:
    client = persistent.Persistent(transport=transport)
    stream_name = str(uuid.uuid1())
    group_name = str(uuid.uuid1())
    streams_client = streams.Streams(transport=transport)
    streams_client.append_to_stream(
        stream=stream_name,
        expected_version=ANY,
        events=JSONEventData(
            type="create_persistent_subscription_tested",
            data={"testing": "create_persistent_subscription"},
        ),
    )
    response = client.create_persistent_subscription(
        stream=stream_name, group_name=group_name
    )
    assert isinstance(response, persistent.persistent_pb2.CreateResp)
    response = client.delete_persistent_subscription(
        stream=stream_name, group=group_name
    )
    response = streams_client.delete_stream(stream=stream_name, expected_version=ANY)


@pytest.mark.integration
def test_update_persistent_subscription(transport: Transport) -> None:
    stream_name = str(uuid.uuid1())
    group_name = str(uuid.uuid1())
    streams_client = streams.Streams(transport=transport)
    streams_client.append_to_stream(
        stream=stream_name,
        expected_version=ANY,
        events=JSONEventData(type="some-event", data={"some": "data"}),
    )
    client = persistent.Persistent(transport=transport)
    client.create_persistent_subscription(stream=stream_name, group_name=group_name)
    response = client.update_persistent_subscription(
        group_name=group_name, stream=stream_name
    )
    assert isinstance(response, persistent.persistent_pb2.UpdateResp)
    client.delete_persistent_subscription(stream=stream_name, group=group_name)
    streams_client.delete_stream(stream=stream_name, expected_version=ANY)


@pytest.mark.integration
def test_delete_persistent_subscription(transport: Transport) -> None:
    stream_name = str(uuid.uuid1())
    group_name = str(uuid.uuid1())
    streams_client = streams.Streams(transport=transport)
    streams_client.append_to_stream(
        stream=stream_name,
        expected_version=ANY,
        events=JSONEventData(type="some-event", data={"some": "data"}),
    )
    client = persistent.Persistent(transport=transport)
    client.create_persistent_subscription(stream=stream_name, group_name=group_name)
    response = client.delete_persistent_subscription(stream=stream_name, group=group_name)
    assert isinstance(response, persistent.persistent_pb2.DeleteResp)
    streams_client.delete_stream(stream=stream_name, expected_version=ANY)
