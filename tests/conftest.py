import pathlib
import pytest
import time
import grpc
from eventstore_grpc import gossip, as_credentials, EventStoreDBClient
from eventstore_grpc.proto import gossip_pb2_grpc

CERTS = pathlib.Path(__file__).parent / "certs"
pytest_plugins = ("docker_compose",)


def pytest_configure():
    CERTS.mkdir(parents=True, exist_ok=True)


def pytest_unconfigure():
    for elm in CERTS.iterdir():
        if elm.is_dir():
            for file in elm.iterdir():
                file.unlink()
            elm.rmdir()
        else:
            elm.unlink()
    CERTS.rmdir()


@pytest.fixture(scope="session", autouse=True)
def wait_for_ready(session_scoped_container_getter):
    target = "localhost:2112"  # Cluster nodes are at ports 2111, 2112.
    with open(CERTS / "ca" / "ca.crt", "rb") as f:
        root_certificates = f.read()
        credentials = grpc.ssl_channel_credentials(root_certificates=root_certificates)
    with grpc.secure_channel(target, credentials=credentials) as channel:
        stub = gossip_pb2_grpc.GossipStub(channel)
        count = 0
        while True:
            count += 1
            print("\033[38;5;220mTrying to reach cluster...\033[0m", end="\r")
            if count > 10:
                break
            try:
                result = gossip.read(stub)
            except:
                time.sleep(3)
                continue
            if all(member.is_alive for member in result.members):
                break
    time.sleep(10)
    print("\033[38;5;42mEventStore DB Cluster is up and running! ✨\033[0m")


@pytest.fixture
def secure_cluster_connection_string():
    rc = CERTS / "ca" / "ca.crt"
    print(f"rc => {rc}")
    return f"esdb://localhost:2111,localhost:2112?tls&rootCertificate={rc}"


@pytest.fixture
def insecure_single_connection_string():
    return "esdb://localhost:2113"


@pytest.fixture(params=["cluster"])
def connection_string(
    request, secure_cluster_connection_string, insecure_single_connection_string
):
    if request.param == "single":
        return insecure_single_connection_string
    elif request.param == "cluster":
        return secure_cluster_connection_string
    else:
        return None


@pytest.fixture
def credentials():
    return as_credentials(username="admin", password="changeit")


@pytest.fixture
def secure_client(secure_cluster_connection_string):
    return EventStoreDBClient(secure_cluster_connection_string)


@pytest.fixture
def insecure_client(insecure_single_connection_string):
    return EventStoreDBClient(insecure_single_connection_string)


@pytest.fixture
def client(connection_string):
    return EventStoreDBClient(connection_string)
