import logging
import time
import uuid

from google.protobuf.json_format import MessageToDict

from eventstore_grpc.client.event_store import EventStore
from eventstore_grpc.event_data import JSONEventData

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    es = EventStore(
        hosts=["localhost:2113", "localhost:2111", "localhost:2112"],
        discover=True,
        tls=True,
        username="admin",
        password="changeit",
        tls_ca_file="certs/ca/ca.crt",
    )
    cluster_info = es.gossip.get_cluster_info()
    logging.info(f"Cluster Info:\n{cluster_info}")
    events = es.streams.read_from_all()
    logging.info("Logging some events from the $all stream:")
    for event in events:
        time.sleep(0.5)
        logging.info(MessageToDict(event))
    logging.info("Subscribing to the $all stream:")
    subscription_id = es.subscriptions.subscribe_to_all(
        handler=lambda x: print(f"Received new message: {x}")
    )
    logging.info(f"Persistent subscription id: {subscription_id}")
    stream_name = "some-stream"
    logging.info(f"Create a new '{stream_name}' stream and append events to it.")
    events = (
        JSONEventData(type="event-type-1", data={"some": "data"}),
        JSONEventData(
            type="event-type-2", data={"some": "data"}, metadata={"some": "metadata"}
        ),
        JSONEventData(
            type="event-type-1", data={"some": "data"}, event_id=uuid.uuid1()
        ),
    )
    for i, event in enumerate(events):
        logging.info(f"Appending event number {i + 1}")
        logging.info(event)
        es.streams.append_to_stream(stream=stream_name, events=event)
        time.sleep(1)

    group_name = "some-group"
    logging.info(
        f"Create a persistent subscription to the '{stream_name}' stream, with a group called '{group_name}'"
    )
    result = es.persistent.create_persistent_subscription(
        stream=stream_name, group_name=group_name
    )
    logging.info("Subscribing to the persistent subscription created.")

    def handler(event):
        print(f"Event received: {event}")

    subscription_id = es.subscriptions.subscribe_persistent(
        stream=stream_name, group_name=group_name, handler=handler
    )
    es.streams.append_to_stream(
        stream=stream_name,
        events=[
            JSONEventData(type="event-1-after-subscription", data={"some": "data"}),
            JSONEventData(type="event-2-after-subscription", data={"more": "data"}),
        ],
    )
    time_left = 10
    logging.info("Waiting some time...")
    while time_left:
        logging.info(time_left)
        time.sleep(1)
        time_left -= 1
    logging.info(f"Unsubscribing from {subscription_id}...")
    es.subscriptions.unsubscribe(subscription_id=subscription_id)
    es.subscriptions.unsubscribe_all()
    logging.info(f"Deleting the stream: {stream_name}")
    es.streams.delete_stream(stream=stream_name)
    logging.info(f"Deleting the persistent subscription ({group_name} - {stream_name})")
    es.persistent.delete_persistent_subscription(group=group_name, stream=stream_name)
