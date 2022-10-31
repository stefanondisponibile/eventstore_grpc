"""
Read Events from Streams.
"""

import sys
from typing import Dict, Iterator, Union

from eventstore_grpc import constants
from eventstore_grpc.proto import shared_pb2, streams_pb2, streams_pb2_grpc


def read_from_stream(
    stub: streams_pb2_grpc.StreamsStub,
    stream: str,
    count: int,
    options: Dict,  # TODO: use from_revision as a parameter.
    **kwargs,
) -> Iterator[streams_pb2.ReadResp]:
    """Reads events from an Event Stream.

    The simplest way to read a stream forwards is to supply a stream name, direction
    and revision to start from. This can either be a stream position or an unsigned
    64 big integer. This will return an iterable yielding events from the stream.

    There are a number of additional arguments you can provide when reading a stream:

    * `max_count`: passing in the max count allows you to limit the number of events
        that returned.
    * `resolve_link_to_pos`: when using projections to create new events you can set
        whether the generated events are pointers to existing events. Setting this
        value to true will tell EventStoreDB to returne the event as well as the event
        linking to it.
    * `configure_operation_options`: this argument is generic setting class for all
        operations that can be set on all operations executed against EventStoreDB. (??)
    * `user_credentials`: the credentials used to read the data can be supplied. To be
        used by the subscription as follows. This will override the default
        credentials set on the connection.

    ### Reading from a revision.
    As well as providing a `StreamPosition` you can also provide a stream revision
    in the form of an unsigned 64 big integer.

    ### Reading backwards.
    As well as being able to read a stream forwards, you can also go backwards. When
    reading backwards is the stream position will have to be set to the end if you
    want to read all the events.

    > Tip: You can use reading backwards to find the last position in the stream. Just
    > read backwards one event and get the position.

    ### Checking for stream presence.
    Reading a stream returns a ReadStreamResult containing a ReadState. This property
    can have the value StreamNotFound and Ok. It is important to check the value of
    this field before attempting to iterate an empty stream as it will throw an
    exception.
    """
    request = streams_pb2.ReadReq()
    req_options = streams_pb2.ReadReq.Options()
    identifier = shared_pb2.StreamIdentifier()
    identifier.stream_name = stream.encode()
    uuid_option = streams_pb2.ReadReq.Options.UUIDOption()
    uuid_option.string.CopyFrom(shared_pb2.Empty())
    stream_options = streams_pb2.ReadReq.Options.StreamOptions()
    stream_options.stream_identifier.CopyFrom(identifier)
    from_revision = options.get("from_revision")
    if from_revision == constants.START:
        stream_options.start.CopyFrom(shared_pb2.Empty())
    elif from_revision == constants.END:
        stream_options.end.CopyFrom(shared_pb2.Empty())
    elif isinstance(from_revision, int):
        stream_options.revision = from_revision
    req_options.stream.CopyFrom(stream_options)
    req_options.uuid_option.CopyFrom(uuid_option)
    resolve_links = options.get("resolve_link_to_s", False)
    req_options.resolve_links = resolve_links
    req_options.count = count or sys.maxsize
    req_options.no_filter.CopyFrom(shared_pb2.Empty())
    default_direction = "backwards" if from_revision == constants.END else "forwards"
    direction = options.get("direction", default_direction)
    if direction.lower() == "forwards":
        req_options.read_direction = streams_pb2.ReadReq.Options.ReadDirection.Forwards
    elif direction.lower() == "backwards":
        req_options.read_direction = streams_pb2.ReadReq.Options.ReadDirection.Backwards
    request.options.CopyFrom(req_options)
    response = stub.Read(request, **kwargs)
    return response


def read_from_all(
    stub: streams_pb2_grpc.StreamsStub,
    from_position: Union[Dict[str, int], str] = constants.START,
    count: int = None,
    direction: str = None,
    **kwargs,
):
    request = streams_pb2.ReadReq()
    options = streams_pb2.ReadReq.Options()
    uuid_option = streams_pb2.ReadReq.Options.UUIDOption()
    uuid_option.string.CopyFrom(shared_pb2.Empty())
    all_options = streams_pb2.ReadReq.Options.AllOptions()
    if isinstance(from_position, str):  # TODO: consider a better way of handling this.
        if from_position.upper() == constants.START:
            all_options.start.CopyFrom(shared_pb2.Empty())
        elif from_position.upper() == constants.END:
            all_options.end.CopyFrom(shared_pb2.Empty())
    elif isinstance(from_position, dict):
        pos = streams_pb2.ReadReq.Options.Position()
        pos.commit_position = from_position["commit_position"]
        pos.prepare_position = from_position["prepare_position"]
        all_options.position.CopyFrom(pos)
    else:
        raise ValueError(f"Invalid 'from_position': {from_position}")
    options.count = count or sys.maxsize
    options.all.CopyFrom(all_options)
    options.uuid_option.CopyFrom(uuid_option)
    options.no_filter.CopyFrom(shared_pb2.Empty())
    default_direction = (
        "backwards"
        if isinstance(from_position, str) and from_position.upper() == constants.END
        else "forwards"
    )
    direction = direction or default_direction
    if direction.lower() == "forwards":
        options.read_direction = streams_pb2.ReadReq.Options.ReadDirection.Forwards
    elif direction.lower() == "backwards":
        options.read_direction = streams_pb2.ReadReq.Options.ReadDirection.Backwards
    else:
        raise ValueError(f"Invalid direction: {direction}")
    request.options.CopyFrom(options)
    response = stub.Read(request, **kwargs)
    return response
