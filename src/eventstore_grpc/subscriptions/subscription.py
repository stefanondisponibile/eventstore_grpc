"""A Subscription Object."""

import logging
from typing import Callable
from eventstore_grpc.subscriptions.requests_stream import RequestsStream
from eventstore_grpc.proto import persistent_pb2_grpc
import threading
import grpc

log = logging.getLogger(__name__)


class Subscription(threading.Thread):
    """A Subscription Object

    This object spawns a new thread and runs a custom callback against each of the
    elements yielded from the stream iterator.

    Attributes:
        _lock: a threading.RLock used to sync.
    """

    _lock = threading.RLock()

    def __init__(
        self,
        requests_stream: RequestsStream,
        stub=None,
        manager=None,
        name=None,
        **kwargs,
    ):
        """Initializes the subscription."""
        threading.Thread.__init__(self, name=name)

        self._requests_stream = requests_stream
        self._responses_stream = None
        self._stub = stub
        self._unsubscribed = threading.Event()
        self._manager = manager
        self.call_options = kwargs

    @property
    def grpc_request(self):
        if not isinstance(self._stub, persistent_pb2_grpc.PersistentSubscriptionsStub):
            grpc_request = next(self._requests_stream)
        else:
            grpc_request = self._requests_stream
        return grpc_request

    def revoke(self):
        print(f"\033[38;5;190mRevoking subscribtion to {self.name}.\033[0m")
        print("\033[38;5;190mStopping stream.\033[0m")
        self._requests_stream.stop()
        self._unsubscribed.set()
        print("\033[38;5;190mSet unsubscribed event.\033[0m")
        if self._responses_stream is not None:
            print("\033[38;5;190mCancelling grpc request.\033[0m")
            self._responses_stream.cancel()
            print("\033[38;5;190mGRPC request cancelled.\033[0m")
        return self

    @property
    def revoked(self):
        return self._unsubscribed.is_set()

    @property
    def results(self):
        return self._requests_stream._results

    def run(self, *args, **kwargs):
        """Runs the thread activity."""
        log.debug(f"{self.name:^10} activity started.")
        self._responses_stream = self._stub.Read(self.grpc_request, **self.call_options)
        try:
            for response in self._responses_stream:
                if self.revoked:
                    return self.results
                self._requests_stream.update(response)
        except grpc.RpcError as err:
            if err.code() == grpc.StatusCode.CANCELLED:
                print(f"\033[38;5;196mGRPC request cancelled for {self.name}\033[0m")
            elif err.code() == grpc.StatusCode.UNKNOWN:
                print(
                    f"\033[38;5;209m[REVOKING SUBSCRIPTION {self.name}]: {err.code()} - {err.details()}\033[0m"
                )
                print(f"\033[38;5;209m{err}\033[0m")
                self.revoke()
                if self.name in self._manager._registry:
                    del self._manager._registry[self.name]
                    return self.results
            else:
                raise err
        return self.results
