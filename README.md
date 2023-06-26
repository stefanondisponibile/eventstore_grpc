<div align="left">
    <img src="https://github.com/stefanondisponibile/eventstore_grpc/actions/workflows/test.yaml/badge.svg?event=push" style="text-align: right" />
    <a target="_blank" href="https://codecov.io/gh/stefanondisponibile/eventstore_grpc"><img src="https://codecov.io/gh/stefanondisponibile/eventstore_grpc/branch/develop/graph/badge.svg?token=O86CZ83P50" style="text-align: right" /></a>
    <a target="_blank" href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" style="text-align: right" /></a>
</div>
<br>

# EventStoreDB GRPC Client.

Use this client to interact with [EventStoreDB](https://developers.eventstore.com/) via GRPC.

[Documenation](https://stefanondisponibile.github.io/eventstore_grpc/).

## Quickstart

### Installation

```bash
pip install eventstore_grpc
```

Try it!

```bash
docker compose down \
  && docker compose up -d \
  && echo 'Wait for EventStoreDB to be ready...' \
  && sleep 10 \
  && poetry run python scripts/example.py \
  && docker compose down
```

See [the example](scripts/example.py).

### Tests

To run the test locally start EventStore DB with `docker compose up`, then just run `pytest`.

## Coverage

![](https://codecov.io/gh/stefanondisponibile/eventstore_grpc/branch/develop/graphs/sunburst.svg?token=O86CZ83P50)
