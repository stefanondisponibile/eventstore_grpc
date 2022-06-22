from eventstore_grpc.client import (
    Gossip,
    Operations,
    Projections,
    Streams,
    Users,
    Persistent,
)

# This options looks cool, but a bit hacky, and it would lack editor support.
# You could add this class as a metaclass=MixinMeta to the main EventStore client.
# https://stackoverflow.com/questions/28204130/how-can-i-conditionally-add-in-a-mixin-to-the-current-class-on-instantiation
class MixinMeta(type):
    def __call__(cls, *args, **kwargs):
        mx = []
        mx.append(Gossip)
        mx.append(Operations)
        mx.append(Persistent)
        mx.append(Projections)
        mx.append(Streams)
        if kwargs.get("tls"):
            mx.append(Users)
        mx.append(cls)
        cls = type(cls.__name__, tuple(mx), dict(cls.__dict__))
        return type.__call__(cls, *args, **kwargs)