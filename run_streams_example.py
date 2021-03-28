from eventstore_grpc import EventStoreDBClient, JSONEventData, constants
from eventstore_grpc.options import base_options
from pprint import pprint
import uuid

conn_str = "esdb://localhost:2111,localhost:2112,localhost:2113?tls&rootCertificate=./tests/certs/ca/ca.crt"
client = EventStoreDBClient(conn_str)

# In case you need authentication for a specific user...
credentials = None
default_user = {"username": "admin", "password": "changeit"}
credentials = base_options.as_credentials(**default_user)

event_1_id = str(uuid.uuid4())
stream = f"some-stream-to-read-from-{uuid.uuid4()}"
expected_version = constants.ANY
event_1 = JSONEventData(
    type="first-event",
    data={"foo": "bar"},
    metadata={"is_test": True},
    event_id=event_1_id,
)
print("*** Event 1: ***")
pprint(event_1)

print(f"\nAppending event to stream (stream_name: {stream}).")
events = [event_1]
client.append_to_stream(
    stream=stream, expected_version=expected_version, events=events
)
result = client.read_from_stream(
    stream=stream,
    count=10,
    from_revision=constants.START,
    options={"direction": constants.FORWARDS},
)
print("\n*** Result ***")
for evnt in result:
    pprint(evnt)

print(f"*** Deleting stream (stream_name: {stream})... ***")
delete_result = client.delete_stream(stream=stream, expected_version=constants.ANY)
print("*** Delete Result ***")
pprint(delete_result)

print("\n*** Trying to read from the same stream again. ***")
result = client.read_from_stream(
    stream=stream,
    count=10,
    from_revision=constants.START,
    options={"direction": constants.FORWARDS},
)
pprint(next(result))
