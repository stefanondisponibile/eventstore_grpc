import dataclasses


@dataclasses.dataclass
class KeepAlive:
    """KeepAlive settings."""

    interval: int = 10_000  # ms
    timeout: int = 10_000  # ms

    def get_channel_options(self) -> tuple[tuple[str, int], tuple[str, int]]:
        """Get keepalive settings as GRPC channel options."""
        return (
            ("grpc.keepalive_time_ms", self.interval),
            ("grpc.keepalive_timeout_ms", self.timeout),
        )
