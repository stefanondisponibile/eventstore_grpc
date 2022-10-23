import pytest
from eventstore_grpc.client import operations
from eventstore_grpc.core.transport import Transport
from eventstore_grpc.proto import shared_pb2
from eventstore_grpc.client.operations import operations as ops
from unittest import mock
import uuid


@pytest.fixture
def client(transport: Transport) -> operations.Operations:
    return operations.Operations(transport=transport)


@pytest.mark.integration
@pytest.mark.operations
def test_merge_indexes(client: operations.Operations) -> None:
    ops.merge_indexes = mock.MagicMock(return_value=shared_pb2.Empty())
    response = client.merge_indexes()
    assert isinstance(response, shared_pb2.Empty)
    ops.merge_indexes.assert_called_once()


@pytest.mark.integration
@pytest.mark.operations
def test_resign_node(client: operations.Operations) -> None:
    ops.resign_node = mock.MagicMock(return_value=shared_pb2.Empty())
    response = client.resign_node()
    assert isinstance(response, shared_pb2.Empty)
    ops.resign_node.assert_called_once()


@pytest.mark.integration
@pytest.mark.operations
def test_restart_persistent_subscriptions(client: operations.Operations) -> None:
    ops.restart_persistent_subscriptions = mock.MagicMock(
        return_value=shared_pb2.Empty()
    )
    response = client.restart_persistent_subscriptions()
    assert isinstance(response, shared_pb2.Empty)
    ops.restart_persistent_subscriptions.assert_called_once()


@pytest.mark.integration
@pytest.mark.operations
@pytest.mark.parametrize("priority", (100,))
def test_set_node_priority(client: operations.Operations, priority: int) -> None:
    ops.set_node_priority = mock.MagicMock(return_value=shared_pb2.Empty())
    response = client.set_node_priority(priority=priority)
    assert isinstance(response, shared_pb2.Empty)
    ops.set_node_priority.assert_called_once()


@pytest.mark.integration
@pytest.mark.operations
@pytest.mark.parametrize("thread_count,start_from_chunk", [(1, 1)])
def test_start_and_stop_scavenge(
    client: operations.Operations, thread_count: int, start_from_chunk: int
) -> None:
    fake_start_response = operations.operations_pb2.ScavengeResp()
    fake_start_response.scavenge_id = str(uuid.uuid1())
    fake_start_response.scavenge_result = (
        operations.operations_pb2.ScavengeResp.ScavengeResult.Started
    )
    ops.start_scavenge = mock.MagicMock(return_value=fake_start_response)
    response = client.start_scavenge(
        thread_count=thread_count, start_from_chunk=start_from_chunk
    )
    scavenge_id = response.scavenge_id
    assert isinstance(response, operations.operations_pb2.ScavengeResp)
    assert isinstance(scavenge_id, str)
    ops.start_scavenge.assert_called_once()
    assert ops.start_scavenge.call_args.kwargs == {
        "thread_count": thread_count,
        "start_from_chunk": start_from_chunk,
    }
    fake_stop_response = operations.operations_pb2.ScavengeResp()
    fake_stop_response.CopyFrom(fake_start_response)
    fake_stop_response.scavenge_result = (
        operations.operations_pb2.ScavengeResp.ScavengeResult.Stopped
    )
    ops.stop_scavenge = mock.MagicMock(return_value=fake_stop_response)
    response = client.stop_scavenge(scavenge_id=scavenge_id)
    assert isinstance(response, operations.operations_pb2.ScavengeResp)
    assert (
        response.scavenge_result
        == operations.operations_pb2.ScavengeResp.ScavengeResult.Stopped
    )
    ops.stop_scavenge.assert_called_once()
    assert ops.stop_scavenge.call_args.kwargs == {"scavenge_id": scavenge_id}


@pytest.mark.integration
@pytest.mark.operations
def test_shutdown(client: operations.Operations) -> None:
    ops.shutdown = mock.MagicMock(return_value=shared_pb2.Empty())
    response = client.shutdown()
    assert isinstance(response, shared_pb2.Empty)
    ops.shutdown.assert_called_once()
