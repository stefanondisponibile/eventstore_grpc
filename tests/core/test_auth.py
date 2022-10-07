import base64
import importlib.resources

import grpc
from eventstore_grpc.core import auth


class TestEventStoreMetadataPlugin:
    def test_init(self) -> None:
        token = "base64-encoded-auth-token"
        assert auth.EventStoreDBMetadataPlugin(token=token)._token == token

    def test_call(self) -> None:
        token = "base64-encoded-auth-token"
        service_url = "some-url:123"
        method_name = "some_method"
        context = grpc.AuthMetadataContext()
        context.service_url = service_url
        context.method_name = method_name
        plugin = auth.EventStoreDBMetadataPlugin(token=token)
        metadata, error = plugin(
            context=context, callback=lambda metadata, error: (metadata, error)
        )
        assert error is None
        assert metadata[0][0] == "authorization"
        assert metadata[0][1] == f"Basic {token}"


class TestAuth:
    def test_init(self) -> None:
        username = "admin"
        password = "changeit"
        root_certificate = importlib.resources.path("tests.fixtures", "ca.crt")
        root_cert_content = importlib.resources.read_binary("tests.fixtures", "ca.crt")
        am = auth.Auth(
            username=username, password=password, root_certificate=root_certificate
        )
        assert am.username == username
        assert am.password == password
        assert base64.b64decode(am.token).decode("ascii") == f"{username}:{password}"
        assert (
            am.credentials._credentials._call_credentialses[0]._name.decode()
            == auth.EventStoreDBMetadataPlugin.__name__
        )
        assert (
            am.credentials._credentials._channel_credentials._pem_root_certificates
            == root_cert_content
        )

    def test_init_without_credentials(self) -> None:
        root_certificate = importlib.resources.path("tests.fixtures", "ca.crt")
        root_cert_content = importlib.resources.read_binary("tests.fixtures", "ca.crt")
        am = auth.Auth(root_certificate=root_certificate)
        assert am.username is None
        assert am.password is None
        assert am.credentials._credentials._pem_root_certificates == root_cert_content

    def test_init_without_root_cert(self) -> None:
        username = "admin"
        password = "changeit"
        am = auth.Auth(username=username, password=password)
        assert am.username == username
        assert am.password == password
        assert base64.b64decode(am.token).decode() == f"{username}:{password}"
        assert am.credentials is None
        assert (
            am._call_credentials._credentials._metadata_plugin._metadata_plugin._token
            == am.token
        )

    def test_get_channel_credentials(self) -> None:
        root_certificate = importlib.resources.path("tests.fixtures", "ca.crt")
        root_cert_content = importlib.resources.read_binary("tests.fixtures", "ca.crt")
        am = auth.Auth(root_certificate=root_certificate)
        crd = am._get_channel_credentials()
        assert crd._credentials._pem_root_certificates == root_cert_content

    def test_get_call_credentials(self) -> None:
        username = "admin"
        password = "changeit"
        am = auth.Auth(username=username, password=password)
        crd = am._get_call_credentials()
        assert crd._credentials._metadata_plugin._metadata_plugin._token == am.token

    def test_setting_username(self) -> None:
        am = auth.Auth(username="old-username", password="password")
        am.username = "new-username"
        assert am.username == "new-username"

    def test_setting_password(self) -> None:
        am = auth.Auth(username="username", password="old-password")
        am.password = "new-password"
        assert am.password == "new-password"

    def test_getting_credentials_when_no_credentials(self) -> None:
        am = auth.Auth()
        assert am.credentials is None
