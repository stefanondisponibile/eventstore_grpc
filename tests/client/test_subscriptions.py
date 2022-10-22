import pytest
from eventstore_grpc.client import subscriptions, streams, persistent
from eventstore_grpc.core.transport import Transport
import uuid
from eventstore_grpc.constants import ANY
from eventstore_grpc.event_data import JSONEventData
import time
from unittest import mock


@pytest.fixture
def client(transport: Transport) -> subscriptions.Subscriptions:
    return subscriptions.Subscriptions(transport=transport)

@pytest.mark.integration
def test_subscribe_to_stream(client: subscriptions.Subscriptions) -> None:
    stream_name = str(uuid.uuid1())
    group_name = str(uuid.uuid1())
    streams_client = streams.Streams(transport=client._transport)
    event = JSONEventData(type=str(uuid.uuid1()), data={"foo": "bar"})
    streams_client.append_to_stream(
        stream=stream_name, expected_version=ANY, events=event
    )
    subscription_id = client.subscribe_to_stream(stream=stream_name)
    assert isinstance(subscription_id, str)
    client.unsubscribe(subscription_id=subscription_id)
    time.sleep(2)
    streams_client.delete_stream(stream=stream_name, expected_version=ANY)


@pytest.mark.integration
def test_subscribe_persistent(client: subscriptions.Subscriptions) -> None:
    stream_name = str(uuid.uuid1())
    group_name = str(uuid.uuid1())
    persistent_client = persistent.Persistent(transport=client._transport)
    persistent_client.create_persistent_subscription(
        stream=stream_name, group_name=group_name
    )
    subscription_id = client.subscribe_persistent(
        stream=stream_name, group_name=group_name
    )
    assert isinstance(subscription_id, str)
    time.sleep(2)
    client.unsubscribe(subscription_id=subscription_id)
    assert client._subscriptions_manager._registry == {}
    persistent_client.delete_persistent_subscription(
        stream=stream_name, group=group_name
    )


@pytest.mark.integration
def test_subscribe_to_all(client: subscriptions.Subscriptions) -> None:
    subscription_id = client.subscribe_to_all()
    assert isinstance(subscription_id, str)
    client.unsubscribe(subscription_id=subscription_id)


@pytest.mark.integration
def test_unsubscribe_all(client: subscriptions.Subscriptions) -> None:
    client.subscribe_to_all()
    client.unsubscribe_all()
    assert client._subscriptions_manager._registry == {}


def test_kill(client: subscriptions.Subscriptions) -> None:
    client.unsubscribe_all = mock.MagicMock()
    client.kill(None, None)
    client.unsubscribe_all.assert_called_once()
