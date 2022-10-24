from eventstore_grpc.streams import append
from eventstore_grpc.proto import streams_pb2, shared_pb2
import pytest
from eventstore_grpc.constants import ANY, STREAM_EXISTS, NO_STREAM


@pytest.mark.parametrize(
    "wrong_expected_version,expected",
    (
        (streams_pb2.AppendResp.WrongExpectedVersion(expected_revision=42), 42),
        (
            streams_pb2.AppendResp.WrongExpectedVersion(
                expected_any=shared_pb2.Empty()
            ),
            ANY,
        ),
        (
            streams_pb2.AppendResp.WrongExpectedVersion(
                expected_stream_exists=shared_pb2.Empty()
            ),
            STREAM_EXISTS,
        ),
        (
            streams_pb2.AppendResp.WrongExpectedVersion(
                expected_no_stream=shared_pb2.Empty()
            ),
            NO_STREAM,
        ),
    ),
)
def test_handle_wrong_expected_version(
    wrong_expected_version: streams_pb2.AppendResp.WrongExpectedVersion,
    expected: int | str,
) -> None:
    message = streams_pb2.AppendResp()
    message.wrong_expected_version.CopyFrom(wrong_expected_version)
    with pytest.raises(append.WrongExpectedVersionError) as err:
        append.handle_wrong_expected_version(message=message)
    assert err.value.expected == expected
