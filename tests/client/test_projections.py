import time
from eventstore_grpc.core.transport import Transport
from eventstore_grpc.client import projections
import pytest
import textwrap
import uuid
from eventstore_grpc.proto import shared_pb2


@pytest.fixture
def projection_query() -> str:
    return textwrap.dedent(
        """
    fromAll()
        .when({
            $init() {
                return {
                    count: 0,
                };
            },
            $any(s, e) {
                s.count += 1;
            }
        })
        .outputState();
    """.strip()
    )


@pytest.fixture()
def client(transport: Transport) -> projections.Projections:
    return projections.Projections(transport=transport)


@pytest.mark.integration
def test_create_continuous_projection(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    response = client.create_continuous_projection(
        name=projection_name, query=projection_query
    )
    assert isinstance(response, projections.projections_pb2.CreateResp)
    client.disable_projection(name=projection_name)
    client.delete_projection(name=projection_name)


@pytest.mark.integration
def test_create_one_time_projection(
    client: projections.Projections, projection_query: str
) -> None:
    response = client.create_one_time_projection(query=projection_query)
    assert isinstance(response, projections.projections_pb2.CreateResp)


@pytest.mark.integration
def test_create_transient_projection(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    response = client.create_transient_projection(
        name=projection_name, query=projection_query
    )
    assert isinstance(response, projections.projections_pb2.CreateResp)
    client.disable_projection(name=projection_name)
    client.delete_projection(name=projection_name)


@pytest.mark.integration
def test_disable_projection(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    client.create_continuous_projection(name=projection_name, query=projection_query)
    response = client.disable_projection(name=projection_name)
    assert isinstance(response, projections.projections_pb2.DisableResp)
    client.delete_projection(name=projection_name)


@pytest.mark.integration
def test_enable_projection(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    client.create_continuous_projection(name=projection_name, query=projection_query)
    client.disable_projection(name=projection_name)
    response = client.enable_projection(name=projection_name)
    assert isinstance(response, projections.projections_pb2.EnableResp)


@pytest.mark.integration
def test_list_continuous_projections(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    client.create_continuous_projection(name=projection_name, query=projection_query)
    response = client.list_continuous_projections()
    pjs = list(response)
    assert any(pj.details.name == projection_name for pj in pjs)
    for pj in pjs:
        if pj.details.name:
            assert pj.details.mode == "Continuous"
    client.disable_projection(name=projection_name)
    client.delete_projection(name=projection_name)


@pytest.mark.integration
def test_list_one_time_projections(
    client: projections.Projections, projection_query: str
) -> None:
    client.create_one_time_projection(query=projection_query)
    response = client.list_one_time_projections()
    pjs = list(response)
    assert all(isinstance(pj, projections.projections_pb2.StatisticsResp) for pj in pjs)


@pytest.mark.integration
def test_list_transient_projections(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    client.create_transient_projection(name=projection_name, query=projection_query)
    response = client.list_transient_projections()
    pjs = list(response)
    assert any(pj.details.name == projection_name for pj in pjs)
    for pj in pjs:
        if pj.details.name:
            assert pj.details.mode == "Transient"
    client.disable_projection(name=projection_name)
    client.delete_projection(name=projection_name)


@pytest.mark.integration
def test_reset_projection(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    client.create_continuous_projection(name=projection_name, query=projection_query)
    response = client.reset_projection(name=projection_name)
    assert isinstance(response, projections.projections_pb2.ResetResp)


@pytest.mark.integration
def test_get_projection_result(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    client.create_continuous_projection(name=projection_name, query=projection_query)
    time.sleep(0.5)  # let the projection roll
    response = client.get_projection_result(name=projection_name)
    assert isinstance(response, projections.projections_pb2.ResultResp)
    assert response.result.struct_value.fields["count"].number_value > 0
    client.disable_projection(name=projection_name)
    client.delete_projection(name=projection_name)


@pytest.mark.integration
def test_get_projection_state(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    client.create_continuous_projection(name=projection_name, query=projection_query)
    time.sleep(0.5)  # let the projection roll
    response = client.get_projection_state(name=projection_name)
    assert isinstance(response, projections.projections_pb2.StateResp)
    assert response.state.struct_value.fields["count"].number_value > 0
    client.disable_projection(name=projection_name)
    client.delete_projection(name=projection_name)


@pytest.mark.integration
def test_get_projection_statistics(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    client.create_continuous_projection(name=projection_name, query=projection_query)
    time.sleep(0.5) # let the projection roll
    response = client.get_projection_statistics(name=projection_name)
    stats = list(response)
    assert all(
        isinstance(stat, projections.projections_pb2.StatisticsResp) for stat in stats
    )
    client.disable_projection(name=projection_name)
    client.delete_projection(name=projection_name)


@pytest.mark.integration
def test_update_projection(
    client: projections.Projections, projection_query: str
) -> None:
    projection_name = str(uuid.uuid1())
    client.create_continuous_projection(name=projection_name, query=projection_query)
    time.sleep(0.5) # let the projection roll
    response = client.update_projection(name=projection_name, query=projection_query)
    assert isinstance(response, projections.projections_pb2.UpdateResp)
    client.disable_projection(name=projection_name)
    client.delete_projection(name=projection_name)


@pytest.mark.integration
def test_restart_projections_subsystem(client: projections.Projections, projection_query: str) -> None:
    assert isinstance(client.restart_projections_subsystem(), shared_pb2.Empty) 
