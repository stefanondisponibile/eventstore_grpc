"""Restart projections."""

from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc, shared_pb2


def restart_projections_subsystem(
    stub: projections_pb2_grpc.ProjectionsStub, **kwargs
) -> shared_pb2.Empty:
    """Restart projections subsystem."""
    return stub.RestartSubsystem(shared_pb2.Empty(), **kwargs)
