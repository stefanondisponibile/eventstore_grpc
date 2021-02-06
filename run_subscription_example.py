"""Runs a subscription example."""

from eventstore_grpc import EventStoreDBClient, JSONEventData
from eventstore_grpc.options import base_options
import time
import json
from google.protobuf import json_format
import random
import base64

conn_str = "esdb://localhost:2111,localhost:2112,localhost:2113?tls&rootCertificate=./certs/ca/ca.crt&nodePreference=LEADER"
client = EventStoreDBClient(conn_str)

# In case you need authentication for a specific user...
credentials = None
default_user = {"username": "admin", "password": "changeit"}
credentials = base_options.as_credentials(**default_user, requires_leader=True)

client.delete_stream("some-stream", expected_version="ANY")

# Write some events...
n_events = 20
events = [JSONEventData(f"Event-{i + 1}", {"idx": i + 1}) for i in range(n_events)]
stream_name = "some-stream"
result = client.append_to_stream(stream_name, expected_version="ANY", events=events)

client._initialize_subscriptions_manager()

class EventsCounter:
    def __init__(self):
        self.events_processed = 0
    
    @property
    def events_processed(self):
        return self._events_processed
    
    @events_processed.setter
    def events_processed(self, value: int):
        self._events_processed = value

events_counter = EventsCounter()

def handler(*args, **kwargs):
    events_processed = events_counter.events_processed
    # time.sleep(random.randint(1,5))
    event = args[0]
    fmt_event = json_format.MessageToDict(event)
    stream_identifier = base64.b64decode(fmt_event["event"]["event"]["streamIdentifier"]["streamName"]).decode("ascii")
    events_counter.events_processed = events_processed + 1
    print(f"\033[38;5;121m---> HANDLING NEW INCOMING EVENT FROM STREAM {stream_identifier.upper()}... [{events_counter.events_processed} event(s) processed so far]\033[0m")
    print(f"\033[38;5;230m{fmt_event}\033[0m")
    print("\033[38;5;167m<--- DONE HANDLING NEW INCOMING EVENT...\033[0m")
    print()


# client.subscribe_to_stream(stream=stream_name, handler=handler, credentials=credentials)

other_stream = "other-stream"

# client.subscribe_to_stream(stream=other_stream, handler=handler, credentials=credentials)

def all_handler(task):
    print(f"\033[38;5;226m$all handler is handling event '{task.event.event.id.string}'...\033[0m")

# client.subscribe_to_all(credentials=credentials, handler=all_handler)

def persistent_handler(task):
    print(f"\033[38;5;226m####################\033[0m")
    if task.HasField("subscription_confirmation"):
        print(f"\033[38;5;226mSubscription confirmation handler was triggered.\033[0m")
    else:  
        print(f"\033[38;5;226mPersistent handler triggered on event '{task.event.event.id.string}'...\033[0m")
    print(f"\033[38;5;226m####################\033[0m")

try:
    client.create_persistent_subscription(stream="some-stream", group_name="some-group", credentials=credentials)
except Exception as err:
    print(err.code())
# time.sleep(3)

client.subscribe_persistent(stream="some-stream", group_name="some-group", handler=persistent_handler, buffer_size=200, credentials=credentials)

for i in range(n_events):
    # time.sleep(2)
    event = JSONEventData(f"Stream-Event-{i + 1}", {"idx": i + 1, "type": "streaming"})
    stream = random.choice([stream_name, other_stream])
    # print(f"\033[38;5;219mAppending new event to stream {stream}: {event}\033[0m")
    # client.append_to_stream(stream, expected_version="ANY", events=event)

while True:
    try:
        time.sleep(1)
        if not client._subscriptions_manager._registry:
            client.unsubscribe_all()
            client.channel.close()
            break
    except KeyboardInterrupt:
        client.close()
        break
