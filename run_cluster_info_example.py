from eventstore_grpc import EventStoreDBClient
from eventstore_grpc.options import base_options

conn_str = "esdb://localhost:2111,localhost:2112,localhost:2113?tls&rootCertificate=./certs/ca/ca.crt"
client = EventStoreDBClient(conn_str)

# In case you need authentication for a specific user...
credentials = None
default_user = {"username": "admin", "password": "changeit"}
credentials = base_options.as_credentials(**default_user)

# Each client's method passes **kwargs down to the grpc method.
if credentials:
    cluster_info = client.get_cluster_info(credentials=credentials)
else:
    cluster_info = client.get_cluster_info()

print(cluster_info)
