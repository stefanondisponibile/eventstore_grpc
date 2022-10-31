import uuid
from unittest import mock

import pytest

from eventstore_grpc import subscriptions


@pytest.fixture
def subscriptions_manager() -> subscriptions.SubscriptionsManager:
    return subscriptions.SubscriptionsManager(mock.MagicMock())


def test_subscribe(subscriptions_manager: subscriptions.SubscriptionsManager) -> None:
    with pytest.raises(NotImplementedError):
        subscriptions_manager.subscribe()


def test_subscription_ids(
    subscriptions_manager: subscriptions.SubscriptionsManager,
) -> None:
    registry = {"some_id": ..., "some-other-id": ...}
    subscriptions_manager._registry = registry
    assert subscriptions_manager.subscription_ids == list(registry.keys())


def test_register_without_id(
    subscriptions_manager: subscriptions.SubscriptionsManager,
) -> None:
    expected_id = "fake-id"
    uuid.uuid4 = mock.MagicMock(return_value=expected_id)
    assert subscriptions_manager._registry == {}
    subscriptions_manager.register(...)
    assert subscriptions_manager.subscription_ids == [expected_id]


def test_register_with_existing_id(
    subscriptions_manager: subscriptions.SubscriptionsManager,
) -> None:
    subscriptions_manager.register(...)
    with pytest.raises(ValueError):
        subscriptions_manager.register(..., subscriptions_manager.subscription_ids[0])


def test_unsubscribe_when_wrong_stream_name(
    subscriptions_manager: subscriptions.SubscriptionsManager,
) -> None:
    subscriptions_manager.register(...)
    assert subscriptions_manager.unsubscribe(stream_name="non-existent") is None
