import pytest
from eventstore_grpc.core import Transport
from eventstore_grpc.client import persistent
from eventstore_grpc.client import streams
from eventstore_grpc.constants import (
    ANY,
    START,
    END,
    DISPATCH_TO_SINGLE,
    ROUND_ROBIN,
    PINNED,
)
from eventstore_grpc.event_data import JSONEventData
import uuid


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
def test_create_persistent_subscription_to_all(transport: Transport) -> None:
    client = persistent.Persistent(transport=transport)
    group_name = str(uuid.uuid1())
    response = client.create_persistent_subscription(group_name=group_name)
    assert isinstance(response, persistent.persistent_pb2.CreateResp)
    response = client.delete_persistent_subscription(group=group_name)


@pytest.mark.integration
@pytest.mark.parametrize(
    "from_revision,strategy",
    [
        (0, DISPATCH_TO_SINGLE),
        (0, ROUND_ROBIN),
        (START, PINNED),
    ],
)
def test_update_persistent_subscription(
    transport: Transport, from_revision: int | str, strategy: str
) -> None:
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
        group_name=group_name,
        stream=stream_name,
        resolve_link_to_s=True,
        from_revision=from_revision,
        strategy=strategy,
    )
    assert isinstance(response, persistent.persistent_pb2.UpdateResp)
    client.delete_persistent_subscription(stream=stream_name, group=group_name)
    streams_client.delete_stream(stream=stream_name, expected_version=ANY)


@pytest.mark.integration
def test_update_persistent_subscription_to_all(transport: Transport) -> None:
    group_name = str(uuid.uuid1())
    client = persistent.Persistent(transport=transport)
    client.create_persistent_subscription(group_name=group_name)
    response = client.update_persistent_subscription(
        group_name=group_name,
        resolve_link_to_s=True,
        from_revision=START,
        prepare_position=0,
        commit_position=0,
    )
    assert isinstance(response, persistent.persistent_pb2.UpdateResp)
    client.delete_persistent_subscription(group=group_name)


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
    response = client.delete_persistent_subscription(
        stream=stream_name, group=group_name
    )
    assert isinstance(response, persistent.persistent_pb2.DeleteResp)
    streams_client.delete_stream(stream=stream_name, expected_version=ANY)
