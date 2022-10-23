import pytest


@pytest.fixture
def username() -> str:
    return "admin"


@pytest.fixture
def password() -> str:
    return "changeit"


@pytest.fixture
def credentials(username: str, password: str) -> dict[str, str]:
    return {"username": username, "password": password}
