from eventstore_grpc.subscriptions import requests_stream
from unittest import mock


def test_collect() -> None:
    rs = requests_stream.RequestsStream()
    expected_task = mock.MagicMock()
    rs.collect(expected_task)
    actual_task = rs._tasks.get_nowait()
    assert actual_task is expected_task


def test_update() -> None:
    rs = requests_stream.RequestsStream()
    rs._stop.set()
    assert rs.update(...) is rs
