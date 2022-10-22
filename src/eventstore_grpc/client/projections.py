"""
Projections Mixin.
"""

from typing import Iterable, Optional
from eventstore_grpc import projections
from eventstore_grpc.proto import projections_pb2, projections_pb2_grpc, shared_pb2
from eventstore_grpc.core import ClientBase


class Projections(ClientBase):
    """Handles Projections Operations."""

    def create_continuous_projection(
        self, name: str, query: str, track_emitted_streams: bool = False, **kwargs
    ) -> projections_pb2.CreateResp:
        """Creates a continuous projection."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.create_continuous_projection(
            stub,
            name=name,
            query=query,
            track_emitted_streams=track_emitted_streams,
            **kwargs
        )
        return result

    def create_one_time_projection(
        self, query: str, track_emitted_streams: bool = False, **kwargs
    ) -> projections_pb2.CreateResp:
        """Creates a one time projection."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.create_one_time_projection(
            stub, query=query, track_emitted_streams=track_emitted_streams, **kwargs
        )
        return result

    def create_transient_projection(
        self, name: str, query: str, **kwargs
    ) -> projections_pb2.CreateResp:
        """Creates a transient projection."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.create_transient_projection(
            stub, name=name, query=query, **kwargs
        )
        return result

    def delete_projection(
        self,
        name: str,
        delete_emitted_streams: bool = True,
        delete_state_stream: bool = True,
        delete_checkpoint_stream: bool = True,
        **kwargs
    ) -> projections_pb2.DeleteResp:
        """Deletes a projection."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.delete_projection(
            stub,
            name=name,
            delete_emitted_streams=delete_emitted_streams,
            delete_state_stream=delete_state_stream,
            delete_checkpoint_stream=delete_checkpoint_stream,
            **kwargs
        )
        return result

    def disable_projection(
        self, name: str, write_checkpoint: bool = True, **kwargs
    ) -> projections_pb2.DisableResp:
        """Disables a projection."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.disable_projection(
            stub, name=name, write_checkpoint=write_checkpoint, **kwargs
        )
        return result

    def enable_projection(self, name: str, **kwargs) -> projections_pb2.EnableResp:
        """Enables a projection."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.enable_projection(stub, name=name, **kwargs)
        return result

    def list_continuous_projections(
        self, **kwargs
    ) -> Iterable[projections_pb2.StatisticsResp]:
        """Lists continuous projections."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.list_continuous_projections(stub, **kwargs)
        return result

    def list_one_time_projections(
        self, **kwargs
    ) -> Iterable[projections_pb2.StatisticsResp]:
        """Lists one time projections."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.list_one_time_projections(stub, **kwargs)
        return result

    def list_transient_projections(
        self, **kwargs
    ) -> Iterable[projections_pb2.StatisticsResp]:
        """List transient projections."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.list_transient_projections(stub, **kwargs)
        return result

    def reset_projection(
        self, name: str, write_checkpoint: bool = True, **kwargs
    ) -> projections_pb2.ResetResp:
        """Resets a projection."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.reset_projection(
            stub, name=name, write_checkpoint=write_checkpoint, **kwargs
        )
        return result

    def restart_projections_subsystem(self, **kwargs) -> shared_pb2.Empty:
        """Restarts projections subsystem."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.restart_projections_subsystem(stub, **kwargs)
        return result

    def get_projection_result(
        self, name: str, from_partition: Optional[str] = None, **kwargs
    ) -> projections_pb2.ResultResp:
        """Gets a projection result."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.get_projection_result(
            stub, name=name, from_partition=from_partition, **kwargs
        )
        return result

    def get_projection_state(self, name: str, **kwargs) -> projections_pb2.StateResp:
        """Gets a projection's state."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.get_projection_state(stub, name=name, **kwargs)
        return result

    def get_projection_statistics(
        self, name: str, **kwargs
    ) -> Iterable[projections_pb2.StatisticsResp]:
        """Gets projection statistics."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.get_projection_statistics(stub, name=name, **kwargs)
        return result

    def update_projection(
        self,
        name: str,
        query: str,
        track_emitted_streams: Optional[bool] = None,
        **kwargs
    ) -> projections_pb2.UpdateResp:
        """Updates a projection."""
        stub = projections_pb2_grpc.ProjectionsStub(self.channel)
        result = projections.update_projection(
            stub,
            name=name,
            query=query,
            track_emitted_streams=track_emitted_streams,
            **kwargs
        )
        return result
