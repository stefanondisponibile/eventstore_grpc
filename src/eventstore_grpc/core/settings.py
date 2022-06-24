import dataclasses


@dataclasses.dataclass
class KeepAlive:
    """KeepAlive settings."""
    interval: int = 10_000  # ms
    timeout: int = 10_000  # ms
