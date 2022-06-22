import dataclasses
from typing import Optional


@dataclasses.dataclass
class KeepAlive:
    """KeepAlive settings."""
    interval: int = 10_000  # ms
    timeout: int = 10_000  # ms


@dataclasses.dataclass
class Node:
    host: str
    port: int = 2113
    scheme: str = None
    username: Optional[str] = None
    password: Optional[str] = None

    def get_url(self) -> str:
        """Returns the url of the node as a string."""
        url = ""
        if self.scheme:
            url += self.scheme + "://"
        if self.username and self.password:
            url += f"{self.username}:{self.password}@"
        url += self.host
        if self.port is not None and f":{self.port}" not in url:
            url += ":" + str(self.port)
        return url
