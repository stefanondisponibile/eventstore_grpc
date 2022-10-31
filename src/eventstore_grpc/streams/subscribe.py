"""Non-persistent stream subscription operations."""

from typing import Dict, Iterable, Union

from eventstore_grpc import constants
from eventstore_grpc.proto import shared_pb2, streams_pb2, streams_pb2_grpc


def get_stream_subscription_request(
    stream: str,
    from_revision: Union[str, int] = constants.START,
    resolve_link_to_s: bool = False,
) -> streams_pb2.ReadReq:
    """Returns a streams_pb2.ReadReq configured for subscription operations for a generic stream."""
    request = streams_pb2.ReadReq()
    options = streams_pb2.ReadReq.Options()
    identifier = shared_pb2.StreamIdentifier()
    identifier.stream_name = stream.encode()
    uuid_option = streams_pb2.ReadReq.Options.UUIDOption()
    uuid_option.string.CopyFrom(shared_pb2.Empty())
    stream_options = streams_pb2.ReadReq.Options.StreamOptions()
    stream_options.stream_identifier.CopyFrom(identifier)
    if isinstance(from_revision, int):
        stream_options.revision = from_revision
    elif from_revision == constants.START:
        stream_options.start.CopyFrom(shared_pb2.Empty())
    elif from_revision == constants.END:
        stream_options.end.CopyFrom(shared_pb2.Empty())
    options.stream.CopyFrom(stream_options)
    options.resolve_links = resolve_link_to_s
    options.subscription.CopyFrom(streams_pb2.ReadReq.Options.SubscriptionOptions())
    options.uuid_option.CopyFrom(uuid_option)
    options.no_filter.CopyFrom(shared_pb2.Empty())
    request.options.CopyFrom(options)
    return request


def get_all_subscription_request(
    from_position: Union[Dict[str, int], str] = constants.START,
    resolve_link_to_s: bool = False,
    filters: Dict = None,
) -> streams_pb2.ReadReq:
    """Returns a streams_pb2.ReadReq configured for subscription operations for the "$all" stream."""
    request = streams_pb2.ReadReq()
    options = streams_pb2.ReadReq.Options()
    uuid_option = streams_pb2.ReadReq.Options.UUIDOption()
    uuid_option.string.CopyFrom(shared_pb2.Empty())
    all_options = streams_pb2.ReadReq.Options.AllOptions()
    if isinstance(from_position, dict):
        grpc_pos = streams_pb2.ReadReq.Options.Position()
        grpc_pos.commit_position = from_position["commit_position"]
        grpc_pos.prepare_position = from_position["prepare_position"]
        all_options.position.CopyFrom(grpc_pos)
    elif from_position == constants.START:
        all_options.start.CopyFrom(shared_pb2.Empty())
    elif from_position == constants.END:
        all_options.end.CopyFrom(shared_pb2.Empty())
    options.all.CopyFrom(all_options)
    options.resolve_links = resolve_link_to_s
    options.subscription.CopyFrom(streams_pb2.ReadReq.Options.SubscriptionOptions())
    options.uuid_option.CopyFrom(uuid_option)
    if filters is not None:
        expr = streams_pb2.ReadReq.Options.FilterOptions.Expression()
        if "prefixes" in filters:
            for elm in filters["prefixes"]:
                expr.prefix.append(elm)
        if "regex" in filters:
            expr.regex = filters["regex"]
        filter_options = streams_pb2.ReadReq.Options.FilterOptions()
        filter_on = filters.get("filter_on")
        if filter_on == "STREAM_NAME":
            filter_options.stream_identifier.CopyFrom(expr)
        elif filter_on == "EVENT_TYPE":
            filter_options.event_type.CopyFrom(expr)
        max_search_window = filters.get("max_search_window")
        if max_search_window is not None:
            if max_search_window <= 0:
                raise ValueError("CheckpointInterval must be greater than 0.")
            filter_options.max = max_search_window
        else:
            filter_options.count.CopyFrom(shared_pb2.Empty())
        checkpoint_interval = filters.get("checkpoint_interval")
        if checkpoint_interval is None or checkpoint_interval <= 0:
            raise ValueError("CheckpointInterval must be greater than 0.")
        filter_options.checkpointIntervalMultiplier = checkpoint_interval
        options.filter.CopyFrom(filter_options)
    else:
        options.no_filter.CopyFrom(shared_pb2.Empty())
    request.options.CopyFrom(options)
    return request


def subscribe_to_stream(
    stub: streams_pb2_grpc.StreamsStub,
    stream: str,
    from_revision: Union[str, int] = constants.START,
    resolve_link_to_s: bool = False,
    **kwargs,
) -> Iterable[streams_pb2.ReadResp]:
    """Subscribes to stream. Returns an object that can be iterated on to get events."""
    request = get_stream_subscription_request(
        stream=stream, from_revision=from_revision, resolve_link_to_s=resolve_link_to_s
    )
    response = stub.Read(request, **kwargs)
    return response


def subscribe_to_all(
    stub: streams_pb2_grpc.StreamsStub,
    from_position: Union[Dict[str, int], str] = constants.START,
    resolve_link_to_s: bool = False,
    filters: Dict = None,
    **kwargs,
) -> Iterable[streams_pb2.ReadResp]:
    """Subscribes to $all stream. Returns an object that can be iterated on to get events."""
    request = get_all_subscription_request(
        from_position=from_position,
        resolve_link_to_s=resolve_link_to_s,
        filters=filters,
    )
    response = stub.Read(request, **kwargs)
    return response
