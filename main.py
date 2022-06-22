import logging

from eventstore_grpc.client import EventStore
from google.protobuf.json_format import MessageToDict

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    cs = "esdb://localhost:2113"
    es = EventStore.from_connection_string(cs)
    cluster_info = es.gossip.get_cluster_info()
    events = es.streams.read_from_all()
    for event in events:
        logging.info(MessageToDict(event))
    subscription_id = es.subscriptions.subscribe_to_all(
        handler=lambda x: print(f"Received new message: {x}")
    )
    logging.info(f"Persistent subscription id: {subscription_id}")
    result = es.persistent.create_persistent_subscription(
        stream="foo", group_name="bar"
    )
