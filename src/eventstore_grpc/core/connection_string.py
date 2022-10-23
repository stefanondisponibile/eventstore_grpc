"""Connection string functions."""

# esdb+discover://admin:changeit@localhost:2111,localhost:2112,localhost:2113?tls=true&tlsVerifyCert=false&nodePreference=LEADER

def parse(connection_string: str) -> dict:  # pragma: nocover
    """Parses a connection string."""
    raise NotImplementedError()  # pragma: nocover
