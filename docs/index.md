# EventStore Python GRPC

Interact with [EventStore](https://developers.eventstore.com/) via GRPC.

## Installation

<div class="termy" data-termynal>
    <span data-ty="input">pip install eventstore_grpc</span>
    <span data-ty="progress">Installing...</span>
</div>

## Usage

```python linenums="1"
import uuid

from eventstore_grpc import EventStore, JSONEventData

# Initialize a client
es = EventStore(
    hosts=["localhost:2113", "localhost:2111", "localhost:2112"],
    discover=True,
    tls=True,
    username="admin",
    password="changeit",
    tls_ca_file="certs/ca/ca.crt",
)

# Subscribe to the "$all" stream and print all the events received
subscription_id = es.subscriptions.subscribe_to_all(
    handler=lambda x: print(f"!!! Received new event: {x}")
)

# Create "some-stream"
stream_name = "some-stream"
events = (
    JSONEventData(type="event-type-1", data={"some": "data"}),
    JSONEventData(
        type="event-type-2", data={"some": "data"}, metadata={"some": "metadata"}
    ),
    JSONEventData(
        type="event-type-1", data={"some": "data"}, event_id=uuid.uuid1()
    ),
)

# publish some events to "some-stream"
for i, event in enumerate(events):
    print(f"Appending event number {i + 1}")
    print(event)
    es.streams.append_to_stream(stream=stream_name, events=event)

# Unsubscribe from "$all"
es.subscriptions.unsubscribe_all()

```

## Reference

See the [reference](./reference/eventstore_grpc/client/event_store/) for more.
