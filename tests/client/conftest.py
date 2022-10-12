import pytest
from _pytest.fixtures import FixtureRequest
from eventstore_grpc.core.auth import Auth
from eventstore_grpc.core.transport import Transport


@pytest.fixture
def username() -> str:
    return "admin"


@pytest.fixture
def password() -> str:
    return "changeit"


@pytest.fixture
def root_certificate() -> str:
    return "certs/ca/ca.crt"


@pytest.fixture
def auth(username: str, password: str, root_certificate: str) -> Auth:
    return Auth(username=username, password=password, root_certificate=root_certificate)


@pytest.fixture(params=[(2111, 2112, 2113)])
def ports(request: FixtureRequest) -> tuple[int]:
    return request.param


@pytest.fixture
def hosts(ports: tuple[int]) -> list[str]:
    return [f"localhost:{port}" for port in ports]


@pytest.fixture
def tls() -> bool:
    return True


@pytest.fixture
def transport(hosts: list[str], auth: Auth, tls: bool) -> Transport:
    return Transport(hosts=hosts, auth=auth, tls=tls)
