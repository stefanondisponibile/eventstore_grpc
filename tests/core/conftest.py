import pytest
from typing import Callable, Union, Optional
from eventstore_grpc.core import settings


@pytest.fixture
def build_connection_string() -> Callable:
    def fn(
        nodes: Union[int, list[str]] = 1,
        node_scheme: Optional[Union[str, list[str]]] = None,
        discovery: bool = False,
        port: Optional[Union[int, list[int]]] = 4242,
        tls: bool = False,
        keep_alive: Optional[settings.KeepAlive] = None,
    ):
        cs = "esdb"
        if discovery:
            cs += "+discover"
        cs += "://"
        if not isinstance(port, list):
            port = [port]
        if not isinstance(node_scheme, list):
            node_scheme = [node_scheme]

        if not isinstance(nodes, list):
            nodes = [f"node{i + 1}.com" for i in range(nodes)]

        for i in range(len(nodes)):
            if node_scheme[i] is not None:
                cs += node_scheme[i] + "://"
            cs += nodes[i]
            if port[i] is not None:
                cs += ":" + str(port[i])
            if i < len(nodes) - 1:
                cs += ","

        if tls or keep_alive is not None:
            cs += "?"

        if tls:
            cs += "tls=true"

        if keep_alive:
            if not cs.endswith("?"):
                cs += "&"
            cs += f"keepAliveTimeout={keep_alive.timeout}"
            cs += f"keepAliveInterval={keep_alive.interval}"
        return cs

    return fn
