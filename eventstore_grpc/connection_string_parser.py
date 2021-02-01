"""
Connection String.

https://github.com/grpc/grpc/blob/master/doc/naming.md
https://uri.thephpleague.com/uri/4.0/components/overview/
esdb+discover://pippo1.pluto:2113,pippo2.pluto:2113,pippo3.pluto:2113?Tls=true
"""

from typing import Tuple, Dict, List, Optional
import urllib

from eventstore_grpc import options


class ConnectionStringError(ValueError):
    pass


def parse(
    conn_str: str,
) -> Tuple[options.ConnectionTypeOptions, options.ChannelCredentialOptions]:
    mode, nodes, params = split_parts(conn_str)
    nodes = parse_nodes(nodes)
    params = parse_search_params(params)
    throw_on_append_failure = True
    if is_dns_discover(mode):
        settings = options.DNSClusterOptions(
            discover=nodes[0],
            max_discover_attempts=params.get("maxDiscoverAttempts", 10),
            discovery_interval=params.get("discoveryInterval", 3),
            gossip_timeout=params.get("gossipTimeout", 30),
            node_preference=params.get("nodePreference", "RANDOM"),
            throw_on_append_failure=throw_on_append_failure,
        )
    else:
        if len(nodes) == 1:
            settings = options.SingleNodeOptions(
                throw_on_append_failure=throw_on_append_failure,
                endpoint=nodes[0],
            )
        else:
            settings = options.GossipClusterOptions(
                throw_on_append_failure=True,
                max_discover_attempts=params.get("maxDiscoverAttempts", 10),
                discovery_interval=params.get("discoveryInterval", 3),
                gossip_timeout=params.get("gossipTimeout", 30),
                node_preference=params.get("nodePreference", "RANDOM"),
                endpoints=nodes,
            )
    insecure = "tls" not in params
    root_certificate = params.get("rootCertificate")
    if root_certificate is not None:
        with open(urllib.parse.unquote(root_certificate), "rb") as f:
            root_certificate = f.read()

    return settings, options.ChannelCredentialOptions(
        insecure=insecure,
        root_certificate=root_certificate,
    )


def split_parts(conn_str: str) -> Tuple[str, ...]:
    """Split the connection string in its main parts.

    The connection string can be divided in three main parts:
    * mode
    * node(s) (authorities + paths)
    * options

    Args:
        conn_str: The connection string.

    Returns:
        The following tuple: (mode, node(s), options)
    """
    parts = conn_str.split("?")
    if len(parts) == 2 and parts[1]:
        mode_and_nodes, options = parts
    elif len(parts) > 2:
        raise ConnectionStringError()
    else:
        options = None
        mode_and_nodes = parts[0]
    parts = mode_and_nodes.split("://")
    if len(parts) == 2 and all(parts):
        mode, nodes = parts
    elif len(parts) > 2:
        raise ConnectionStringError()
    else:
        mode = None
        nodes = parts[0]
    return mode, nodes, options


def parse_nodes(nodes: str) -> List[Dict[str, str]]:
    """Parse a nodes string to extract the different nodes.

    Args:
        nodes: different node uris can be specified by
            comma-separating them.

    Returns:
        A list of target dictionaries. Each target dictionary contains
        "host" and "port" keys mapping to their respective values.
    """
    nodes = nodes.split(",")
    targets = []
    for i, node in enumerate(nodes):
        host_and_port = node.split(":")
        if len(host_and_port) == 2:
            host, port = host_and_port
        elif len(host_and_port) > 2:
            raise ConnectionStringError()
        else:
            port = None
            host = host_and_port[0]
        username = None
        password = None
        if "@" in host:
            # Identity is not supported.
            username, password = parse_credentials(host)
        targets.append(
            {"host": host, "port": port, "username": username, "password": password}
        )
    return targets


def is_dns_discover(mode: str) -> bool:
    if mode == "esdb":
        return False
    elif mode == "esdb+discover":
        return True


def parse_credentials(host: str) -> Tuple[Optional[str], Optional[str]]:
    parts = host.split("@")
    if len(parts) == 2:
        username, password = parts[0].split(":")
        username = urllib.parse.unquote(username)
        password = urllib.parse.unquote(password)
        return username, password
    return None, None


def parse_search_params(options_str: Optional[str]):
    options = {}

    if options_str is None:
        return options

    for pair in options_str.split("&"):
        pair_values = pair.split("=")
        if len(pair_values) == 2:
            key = pair_values[0]
            value = pair_values[1]
        else:
            key = "".join(pair_values)
            value = None
        options[key] = value
    return options
