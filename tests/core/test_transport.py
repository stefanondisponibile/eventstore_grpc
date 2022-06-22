from eventstore_grpc.core.transport import Transport
from typing import Callable


class TestTransport:
    def test_parse_nodes_correctly(self, build_connection_string: Callable) -> None:
        cs = build_connection_string()
        t = Transport.from_connection_string(cs)
        assert len(t.nodes) == 1
        assert t.nodes[0].host == "node1.com"

    def test_parse_tls_correctly(self, build_connection_string: Callable) -> None:
        cs = build_connection_string(tls=True)
        t = Transport.from_connection_string(cs)
        assert t.tls == True

    def test_parse_discover_correctly(self, build_connection_string: Callable) -> None:
        cs = build_connection_string(discovery=True)
        t = Transport.from_connection_string(cs)
        assert t.discover == True
