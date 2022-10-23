from unittest import mock
from eventstore_grpc.options import base_options
import pytest
import grpc


def test_should_initialize_base_options_correctly(credentials: dict[str, str]) -> None:
    requires_leader = True
    bo = base_options.BaseOptions(
        credentials=credentials, requires_leader=requires_leader
    )
    assert bo.credentials is credentials
    assert bo.requires_leader is requires_leader
    expected_token = "YWRtaW46Y2hhbmdlaXQ="  # admin:changeit
    assert bo.metadata == [
        ("authorization", f"Bearer {expected_token}"),
        ("requires-leader", "true"),
    ]


def test_as_metadata(credentials: dict[str, str]) -> None:
    expected_token = "YWRtaW46Y2hhbmdlaXQ="  # admin:changeit
    requires_leader = True
    metadata = base_options.as_metadata(
        credentials=credentials, requires_leader=requires_leader
    )
    assert metadata[0] == ("authorization", f"Bearer {expected_token}")
    assert metadata[1] == ("requires-leader", "true")


class TestEventStoreDBMetadataPlugin:
    def test_initialization(self, username: str, password: str) -> None:
        requires_leader = True
        plugin = base_options.EventStoreDBMetadataPlugin(
            username=username,
            password=password,
            requires_leader=requires_leader,
        )
        assert plugin._username is username
        assert plugin._password is password
        assert plugin._requires_leader is requires_leader
        assert plugin._metadata is None

    def test_token_compilation(self, username: str, password: str) -> None:
        token_metadata = base_options.EventStoreDBMetadataPlugin._compile_token(
            username=username, password=password
        )
        expected_token = "YWRtaW46Y2hhbmdlaXQ="  # admin:changeit
        assert token_metadata == ("authorization", f"Basic {expected_token}")

    def test_token_compilation_when_incomplete_credentials(self, username: str) -> None:
        assert (
            base_options.EventStoreDBMetadataPlugin._compile_token(
                username=username, password=None
            )
            is None
        )

    @pytest.mark.parametrize(
        "requires_leader,expected", ((True, "true"), (False, "false"), (None, None))
    )
    def test_compile_requires_leader(
        self, requires_leader: bool, expected: str
    ) -> None:
        assert base_options.EventStoreDBMetadataPlugin._compile_requires_leader(
            requires_leader
        ) == (("requires-leader", expected) if expected is not None else expected)

    def test_compile(self, username: str, password: str) -> None:
        requires_leader = True
        plugin = base_options.EventStoreDBMetadataPlugin(
            username=username, password=password, requires_leader=requires_leader
        )
        plugin.compile()
        expected_token = "YWRtaW46Y2hhbmdlaXQ="  # admin:changeit
        assert plugin._metadata == (
            ("authorization", f"Basic {expected_token}"),
            ("requires-leader", "true"),
        )

    def test_call(self, username: str, password: str) -> None:
        requires_leader = False
        plugin = base_options.EventStoreDBMetadataPlugin(
            username=username, password=password, requires_leader=requires_leader
        )
        fake_context = mock.MagicMock()
        fake_callback = mock.MagicMock()
        plugin(fake_context, fake_callback)
        expected_token = "YWRtaW46Y2hhbmdlaXQ="  # admin:changeit
        assert plugin._metadata == (
            ("authorization", f"Basic {expected_token}"),
            ("requires-leader", "false"),
        )
        fake_callback.assert_called_once_with(plugin._metadata, None)


def test_as_credentials(username: str, password: str) -> None:
    credentials = base_options.as_credentials(username=username, password=password)
    assert isinstance(credentials, grpc.CallCredentials)
