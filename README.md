# [EventStoreDB](https://www.eventstore.com/) Client.

> ⚠️ Still under development ⚠️

## How to use.

```python
from eventstore_grpc import EventStoreDBClient
from eventstore_grpc.options import base_options

conn_str = "esdb://localhost:2111,localhost:2112,localhost:2113?tls&rootCertificate=./certs/ca/ca.crt"
client = EventStoreDBClient(conn_str)

# In case you needed authentication for a specific user...
credentials = None
default_user = {"username": "admin", "password": "changeit"}
credentials = base_options.as_credentials(**default_user)

# Each client's method passes **kwargs down to the grpc method.
if credentials:
    cluster_info = client.get_cluster_info(credentials=credentials)
else:
    cluster_info = client.get_cluster_info()

print(cluster_info)
```

## Development.
You will probably need an EventStoreDB (cluster) to work with.
The most easy way is (probably) docker-compose:

```bash
docker-compose -f eventstore.master.docker-compose.yaml up -d
```

You may want to have a look at the logs...
```bash
docker-compose -f eventstore.master.docker-compose.yaml logs --tail 10 -f
```

...or shut everything down...
```bash
docker-compose -f eventstore.master.docker-compose.yaml down --volumes  # omit the --volumes flag to keep 'em.
```


Running the container will populate the `./certs` directory with the certificates needed for communication.

The `./certs/ca/ca.crt` is the certificate that the gRPC client needs, so make sure to pass it as a `rootCertificate=<your-path>` connection string option (or you may want to install the certificate in your system as an alternative).

## TODOs:
- [X] Implement `$all` stream operations 👷.
- [X] Implement `projections` operations 👷‍♀️.
- [ ] Implement `persistent/subscription` operations 👷🏿.
- [ ] Consider using [`src` code structure](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure) 🤔.
- [ ] Write [`setup.py`](./setup.py) 🙄.
- [ ] Write tests 🧪.
- [ ] Docs, CI/CD, pre-commit, etc... 💡.