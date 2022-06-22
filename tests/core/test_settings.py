from eventstore_grpc.core.settings import Node


class TestNode:
    def test_get_url(self) -> None:
        n = Node(host="foo.com", port=8080, scheme="http")
        assert n.get_url() == "http://foo.com:8080"
