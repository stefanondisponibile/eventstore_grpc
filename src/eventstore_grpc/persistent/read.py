"""Persistent Subscriptions Operations."""

from typing import Optional

from eventstore_grpc.proto import persistent_pb2, shared_pb2


def options_request(
    stream: str, group_name: str, buffer_size: int = 10
) -> persistent_pb2.ReadReq:
    """Returns a persistent subscription options request."""
    request = persistent_pb2.ReadReq()
    options = persistent_pb2.ReadReq.Options()
    identifier = shared_pb2.StreamIdentifier()
    identifier.stream_name = stream.encode()
    uuid_option = persistent_pb2.ReadReq.Options.UUIDOption()
    uuid_option.string.CopyFrom(shared_pb2.Empty())
    options.stream_identifier.CopyFrom(identifier)
    options.group_name = group_name
    options.buffer_size = buffer_size
    options.uuid_option.CopyFrom(uuid_option)
    request.options.CopyFrom(options)
    return request


def ack_request(read_resp: persistent_pb2.ReadResp):
    if not read_resp.HasField("event"):
        raise ValueError(f"Invalid ReadResp: {read_resp}")  # pragma: nocover
    request = persistent_pb2.ReadReq()
    ack = persistent_pb2.ReadReq.Ack()
    ack.ids.append(read_resp.event.event.id)
    request.ack.CopyFrom(ack)
    return request


def nack_request(
    read_resp: persistent_pb2.ReadResp,
    action: Optional[int] = None,
    reason: Optional[str] = None,
):
    if not read_resp.HasField("event"):
        raise ValueError(f"Invalid ReadResp: {read_resp}")  # pragma: nocover
    request = persistent_pb2.ReadReq()
    nack = persistent_pb2.ReadReq.Nack()
    nack.ids.append(read_resp.event.event.id)
    reason = reason or "Unknown"
    nack.action = action or persistent_pb2.ReadReq.Nack.Action.Unknown
    nack.reason = reason
    request.nack.CopyFrom(nack)
    return request
