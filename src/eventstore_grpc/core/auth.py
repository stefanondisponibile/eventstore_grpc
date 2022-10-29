"""https://developers.eventstore.com/clients/dotnet/5.0/security.html#authentication-and-authorization"""

import base64
import grpc


class EventStoreDBMetadataPlugin(grpc.AuthMetadataPlugin):
    def __init__(self, token: str) -> None:
        self._token = token

    def __call__(
        self,
        context: grpc.AuthMetadataContext,
        callback: grpc.AuthMetadataPluginCallback,
    ) -> grpc.AuthMetadataPluginCallback:
        metadata = [("authorization", f"Basic {self._token}")]
        return callback(metadata=tuple(metadata), error=None)


class Auth:
    """Manages authentication/authorization for the client."""

    def __init__(
        self, username: str = None, password: str = None, root_certificate: str = None
    ) -> None:
        """Initializes the AuthManager.

        Args:
            username: the username.
            password: the password.
            root_certificate: the path to the root certificate.
        """
        self._username = username
        self._password = password
        self._root_certificate = root_certificate
        self._channel_credentials = None
        self._call_credentials = None

        if root_certificate is not None:
            self._channel_credentials = self._get_channel_credentials()

        if self.token:
            self._call_credentials = self._get_call_credentials()

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = value
        if self._password:
            self._call_credentials = self._get_call_credentials()

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = value
        if self._username:
            self._call_credentials = self._get_call_credentials()

    @property
    def token(self) -> str:
        """Base64 encoded username:passsword."""
        if not self._username and not self._password:
            return None

        return base64.b64encode(
            f"{self._username}:{self._password}".encode("ascii")
        ).decode("ascii")

    @property
    def credentials(self) -> grpc.ChannelCredentials:
        if not self._channel_credentials and not self._call_credentials:
            return None
        elif self._channel_credentials and self._call_credentials:
            return grpc.composite_channel_credentials(
                self._channel_credentials, self._call_credentials
            )
        elif self._channel_credentials and not self._call_credentials:
            return self._channel_credentials
        return None

    def _get_channel_credentials(self) -> grpc.ChannelCredentials:
        with open(self._root_certificate, "rb") as f:
            rc = f.read()

        return grpc.ssl_channel_credentials(root_certificates=rc)

    def _get_call_credentials(self) -> grpc.CallCredentials:
        return grpc.metadata_call_credentials(
            EventStoreDBMetadataPlugin(token=self.token)
        )
