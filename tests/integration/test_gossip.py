from eventstore_grpc.proto import gossip_pb2

def test_get_cluster_info(secure_client):
    result = secure_client.get_cluster_info()
    assert isinstance(result, gossip_pb2.ClusterInfo)
