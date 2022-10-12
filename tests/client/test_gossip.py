import pytest
from eventstore_grpc.client import gossip
from eventstore_grpc.core.transport import Transport


@pytest.mark.integration
def test_gossip(transport: Transport) -> None:
    client = gossip.Gossip(transport=transport)
    result = client.get_cluster_info()
    assert isinstance(result, gossip.ClusterInfo)
    assert len(result.members) == 3
