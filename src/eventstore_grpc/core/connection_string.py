"""Connection string functions."""

# esdb+discover://admin:changeit@localhost:2111,localhost:2112,localhost:2113?tls=true&tlsVerifyCert=false&nodePreference=LEADER

# TODO: implement this function
def parse(connection_string: str) -> dict:
    """Parses a connection string."""
    res = {}
    scheme, _, hosts = connection_string.partition("://")
    res["discover"] = "+discover" in scheme
