# Quickstart

If you want to test the client you will need some EventStoreDB instance to interact with.
You can have a look at [this quickstart](https://developers.eventstore.com/server/v20.10/installation.html#quick-start), but if you're short on time and you have `docker compose` installed on your machine, here's your shortcut:

```bash
curl -o docker-compose-eventstore-3nodes.yaml https://raw.githubusercontent.com/stefanondisponibile/eventstore_grpc/master/docker-compose.yaml && \
docker compose -f docker-compose-eventstore-3nodes.yaml up -d && \
docker compose logs
```

This downloads [a docker compose file](https://github.com/stefanondisponibile/eventstore_grpc/blob/master/docker-compose.yaml) to setup an EventStoreDB instance with 3 nodes.

If you cloned the `eventstore_grpc` repository you can skip the `curl` part and use the `docker-compose.yaml` file directly.

!!! note
    The docker compose file generates SSL certificates and puts them in a `certs` folder on your local directory. You can delete that directory, but since it was generated by a docker container you will need to be `root`.
    For example, if you want to clean everything up when you're done, you can run the following:

    ```bash
    docker compose down -v && sudo rm -rf ./certs docker-compose-eventstore-3nodes.yaml
    ```

If you want, you can explore the EventStoreDB [Admin UI](https://developers.eventstore.com/server/v5/admin-ui.html#dashboard) pointing your browser to [https://localhost:2111](https://localhost:2111).

## Creating a client

Our EventStoreDB instance is running 3 nodes at the followings `hosts`:

* `localhost:2111`
* `localhost:2112`
* `localhost:2113`

We want to use `tls` for secure connections, we're going to read the certificates from the folder that was created with _docker compose_ (`./certs/ca/ca.crt`) and we're going to use the default [_admin_ credentials](https://developers.eventstore.com/server/v21.10/installation.html#default-access) (`admin`, `changeit`).

```python linenums="1"
from eventstore_grpc import EventStore

es = EventStore(
    hosts=["localhost:2111", "localhost:2112", "localhost:2113"],
    tls=True,
    tls_ca_file="certs/ca/ca.crt",
    username="admin",
    password="changeit",
)
```

## Getting information about the cluster

Now that we have a client, we can get some information about it:

```python linenums="1"
cluster_info = es.gossip.get_cluster_info()
print(cluster_info)
```

This should tell you something like this:

```proto
members {
  instance_id {
    structured {
      most_significant_bits: 766833313904807028
      least_significant_bits: -7167183254000776328
    }
  }
  time_stamp: 16882865214981958
  state: Follower
  is_alive: true
  http_end_point {
    address: "127.0.0.1"
    port: 2113
  }
}
members {
  instance_id {
    structured {
      most_significant_bits: -1389199217038570244
      least_significant_bits: -6286225797498614732
    }
  }
  time_stamp: 16882865215001644
  state: Leader
  is_alive: true
  http_end_point {
    address: "127.0.0.1"
    port: 2112
  }
}
members {
  instance_id {
    structured {
      most_significant_bits: 4006561881348851895
      least_significant_bits: -7528605218151893547
    }
  }
  time_stamp: 16882865213735606
  state: Follower
  is_alive: true
  http_end_point {
    address: "127.0.0.1"
    port: 2111
  }
}
```

The `gossip.get_cluster_info` endpoint returns [a `ClusterInfo` _protobuf_ message](https://github.com/EventStore/EventStore/blob/b3305db0628ec6a2a48bbf15ad5238a9de5f993d/src/Protos/Grpc/gossip.proto#L11-L13), so you can use it directly. For example, you can check if all your nodes are _alive_:

```python linenums="1"
assert all(member.is_alive for member in cluster_info.members)
```

Or you can check each node's state (e.g. to understand if one's a [_Leader_ or _Follower_](https://developers.eventstore.com/server/v21.10/cluster.html#node-roles)):

```python linenums="1"
from eventstore_grpc.proto.gossip_pb2 import MemberInfo

for member in cluster_info.members:
    state_name = MemberInfo.VNodeState.Name(member.state)
    http_end_point = f"{member.http_end_point.address}:{member.http_end_point.port}"
    print(f"Node {http_end_point} is {state_name}")
```

!!! note
    Here we're importing `MemberInfo` from `eventstore_grpc.proto.gossip_pb2` to resolve the name of each `member`'s `state` `enum` value.

    [Here](https://github.com/EventStore/EventStore/tree/master/src/Protos/Grpc) you can find the complete reference to EventStoreDB's protobuf definitions.
    You can import any of the compiled protos from `eventstore_grpc.proto`.

## Creating events

To produce and consume _events_ we use [EventData](../reference/eventstore_grpc/event_data/) objects.
Each event will have a unique _id_, a _type_, some _data_ to represent the event itself. Additionally, you can store some _metadata_ along side if you want to add some "context" to the event that you're story with information that's not part of the event itself, like correlations ids, timestamps, access information.

!!! note
    [`EventData`](../reference/eventstore_grpc/event_data/) is roughly equivalent to what [EventData represents in other EventStoreDB grpc clients](https://developers.eventstore.com/clients/grpc/appending-events.html#working-with-eventdata).

You can create your own custom types of [`EventData`](../reference/eventstore_grpc/event_data/), but it's common to use `JSON` format to store event payloads, which is convenient also to use some of the built-in features of EventStoreDB such as projections. This library provides a [`JSONEventData`](../reference/eventstore_grpc/event_data/#eventstore_grpc.event_data.JSONEventData) class that you can use to create Events with a JSON payload:

```python linenums="1"
from eventstore_grpc import JSONEventData

event_1 = JSONEventData(type="some_event_occurred", data={"foo": "bar"})
event_2 = JSONEventData(type="some_other_event_occurred", data={"baz": 42}, event_id="40db443a-6244-472b-87c1-e8e87c8a3abf")
event_3 = JSONEventData(type="something-happened", data=None, metadata={"some": "custom-metadata"})
```

!!! note
    In `event_1` we didn't provide any `event_id`. The `JSONEventData` object will create a `uuid.uuid4` id automatically in such cases. Bear in mind that the `event_id` must be a valid [Uuid](https://en.wikipedia.org/wiki/Universally_unique_identifier).


## Publishing events

In EventStoreDB when you *publish* some *event* you will *append* it to some *stream*.
You can think of a _stream_ as an ordered collection of events.

All you have to do to append some events to a stream is creating the events and deciding a name for your stream:

```python linenums="1"
stream_name = "some-stream"
```

We can append a list of events:

```python linenums="1"
response = es.streams.append_to_stream(stream=stream_name, events=[event_1, event_2])
print(response)
```

```proto
success {
  current_revision: 1
  position {
    commit_position: 6914
    prepare_position: 6914
  }
}
```

Or one at a time:

```python linenums="1"
response = es.streams.append_to_stream(stream=stream_name, events=event_3)
print(response)
```

```proto
success {
  current_revision: 2
  position {
    commit_position: 7053
    prepare_position: 7053
  }
}
```


## Reading events

We have different options to read events from a stream, but for this quickstart let's keep it simple and say that we want to read all the events that we just published (i.e from the _start_ of our `some-stream` _stream_).


```python linenums="1"
events = es.streams.read_from_stream(stream_name)
for event in events:
  print(event)
```

```proto
event {
  event {
    id {
      string: "8c253ce9-02ec-42d8-b7df-7607c2dc91d3"
    }
    stream_identifier {
      stream_name: "some-stream"
    }
    prepare_position: 18446744073709551615
    commit_position: 18446744073709551615
    metadata {
      key: "type"
      value: "some_event_occurred"
    }
    metadata {
      key: "created"
      value: "16882945222373749"
    }
    metadata {
      key: "content-type"
      value: "application/json"
    }
    custom_metadata: "{}"
    data: "{\"foo\": \"bar\"}"
  }
  no_position {
  }
}

event {
  event {
    id {
      string: "40db443a-6244-472b-87c1-e8e87c8a3abf"
    }
    stream_identifier {
      stream_name: "some-stream"
    }
    stream_revision: 1
    prepare_position: 18446744073709551615
    commit_position: 18446744073709551615
    metadata {
      key: "type"
      value: "some_other_event_occurred"
    }
    metadata {
      key: "created"
      value: "16882945222374129"
    }
    metadata {
      key: "content-type"
      value: "application/json"
    }
    custom_metadata: "{}"
    data: "{\"baz\": 42}"
  }
  no_position {
  }
}

event {
  event {
    id {
      string: "db4a5a73-f4ce-4760-974d-97ad5091789c"
    }
    stream_identifier {
      stream_name: "some-stream"
    }
    stream_revision: 2
    prepare_position: 18446744073709551615
    commit_position: 18446744073709551615
    metadata {
      key: "type"
      value: "something-happened"
    }
    metadata {
      key: "created"
      value: "16882945889580381"
    }
    metadata {
      key: "content-type"
      value: "application/json"
    }
    custom_metadata: "{\"some\": \"custom-metadata\"}"
    data: "null"
  }
  no_position {
  }
}
```

## Going further

So far you've learned how to:

* connect to EventStoreDB
* getting information about the nodes of the cluster
* creating some events
* appending events to some stream
* reading from the stream

There's much more you can do with EventStoreDB and we're constantly trying to improve our documentation. We will add some sections to cover intermediate/advanced use cases.

For now, please use the [API reference](../reference/eventstore_grpc/client/event_store/).