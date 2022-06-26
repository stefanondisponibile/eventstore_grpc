from eventstore_grpc.core import settings


class TestKeepAlive:
    def test_keep_alive_init(self) -> None:
        ka = settings.KeepAlive()
        assert ka.interval == 10_000
        assert ka.timeout == 10_000
        ka.interval = 5_000
        ka.timeout = 42
        assert ka.interval == 5_000
        assert ka.timeout == 42
