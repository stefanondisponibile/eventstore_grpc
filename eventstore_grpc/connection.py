"""
Connection String.
esdb+discover://foo.bar:2113,foo2.bar2:2113,foo3.bar3:2113?Tls=true
"""

from typing import Tuple, Dict, List, Optional
import urllib
import re
import grpc
from eventstore_grpc import options, discovery


class ConnectionStringError(ValueError):
    pass


class ConnectionConfiguration:
    """A Connection Configuration."""

    def __init__(
        self,
        node_options: options.ConnectionTypeOptions,
        channel_credential_options: options.ChannelCredentialOptions,
    ):
        """Initializes the ConnectionConfiguration."""
        self._connection_type_options = node_options
        self._channel_credential_options = channel_credential_options

    @property
    def credentials(self):
        if self._channel_credential_options.insecure:
            return None
        else:
            return grpc.ssl_channel_credentials(
                root_certificates=self._channel_credential_options.root_certificate,
                private_key=self._channel_credential_options.private_key,
            )

    @property
    def endpoints(self):
        if isinstance(self._connection_type_options, options.SingleNodeOptions):
            endpoints = [self._connection_type_options.endpoint]
        elif isinstance(self._connection_type_options, options.DNSClusterOptions):
            endpoints = [self._connection_type_options.discover]
        elif isinstance(self._connection_type_options, options.GossipClusterOptions):
            endpoints = self._connection_type_options.endpoints
        else:
            endpoints = []
        return [f"{elm['host']}:{elm['port']}" for elm in endpoints]

    @property
    def endpoint(self):
        if isinstance(
            self._connection_type_options,
            (options.DNSClusterOptions, options.GossipClusterOptions),
        ):
            return discovery.discover_endpoint(
                self.endpoints,
                self.credentials,
                node_preference=self._connection_type_options.node_preference,
            )
        else:
            return self.endpoints[0]
    
    @property
    def cluster_members(self):
        members = None
        for candidate in self.endpoints:
            try:
                members = discovery.list_cluster_members(candidate, self.credentials)
            except:
                continue
        return members

    @property
    def leader(self):
        leaders = [elm for elm in self.cluster_members if elm.get("state") == 8]
        if not leaders:
            return None
        leader = leaders[0]
        address = leader["http_end_point"]["address"]
        port = leader["http_end_point"]["port"]
        return f"{address}:{port}"

    @property
    def channel(self):
        if self._channel_credential_options.insecure:
            return grpc.insecure_channel(self.endpoint)
        else:
            credentials = self.credentials
            return grpc.secure_channel(self.endpoint, credentials)

    @classmethod
    def from_connection_string(cls, connection_string: str):
        return cls(*parse(connection_string))


class Connection:
    """A Connection Object."""

    def __init__(self, configuration: ConnectionConfiguration):
        """Initializes the Connection object."""
        self._configuration = configuration

    @property
    def channel(self):
        return self._configuration.channel

    @classmethod
    def from_connection_string(cls, connection_string: str):
        return cls(ConnectionConfiguration.from_connection_string(connection_string))


def parse(
    conn_str: str,
) -> Tuple[options.ConnectionTypeOptions, options.ChannelCredentialOptions]:
    """Parses a connection string."""
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
        host_and_port = re.split(r":(?=\d+)", node)
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
            credentials, host = host.split("@")
            username, password = credentials.split(":")
        if port is not None and "/" in port:
            raise ConnectionStringError(f"Path are not supported: {node}")
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
