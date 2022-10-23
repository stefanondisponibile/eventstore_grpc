# EventStoreDB GRPC Client.

[![codecov](https://codecov.io/gh/stefanondisponibile/eventstore_grpc/branch/develop/graph/badge.svg?token=O86CZ83P50)](https://codecov.io/gh/stefanondisponibile/eventstore_grpc)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Use this client to interact with [EventStoreDB](https://developers.eventstore.com/) via GRPC.

## Quickstart

1. Start an eventstore instance (without authentication):

```bash
docker-compose up
```

2. Run some code:

```python
import logging

from eventstore_grpc.client import EventStore
from google.protobuf.json_format import MessageToDict

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    es = EventStore(
        hosts="localhost:2113",
        discover=True,
        tls=True,
        username="admin",
        password="changeit",
        tls_ca_file="certs/ca/ca.crt",
    )
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

```

## Development

`#TODO`

### Tests

To run the test locally start EventStore DB with `docker compose up`, then just run `pytest`.

## Coverage

![](https://codecov.io/gh/stefanondisponibile/eventstore_grpc/branch/develop/graphs/sunburst.svg?token=O86CZ83P50)
