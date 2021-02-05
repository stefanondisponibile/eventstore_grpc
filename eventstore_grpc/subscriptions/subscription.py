"""A Subscription Object."""

import logging
from typing import Callable
from eventstore_grpc.subscriptions.requests_stream import RequestsStream
from eventstore_grpc.proto import persistent_pb2_grpc
import threading

log = logging.getLogger(__name__)

class Subscription(threading.Thread):
    """A Subscription Object
    
    This object spawns a new thread and runs a custom callback against each of the
    elements yielded from the stream iterator.

    Attributes:
        _lock: a threading.RLock used to sync.
    """
    _lock = threading.RLock()

    def __init__(self, requests_stream: RequestsStream, stub = None, name = None, **kwargs):
        """Initializes the subscription."""
        threading.Thread.__init__(self, name=name)

        self._requests_stream = requests_stream
        self._stub = stub
        self.subscribed = True
        self.call_options = kwargs

    def run(self, *args, **kwargs):
        """Runs the thread activity."""
        log.debug(f"{self.name:^10} activity started.")
        if not isinstance(self._stub, persistent_pb2_grpc.PersistentSubscriptionsStub):
            grpc_request = next(self._requests_stream)
        else:
            grpc_request = self._requests_stream
        self.responses_stream = self._stub.Read(grpc_request, **self.call_options)
        for response in self.responses_stream:
            self._requests_stream.update(response)
            if self._stub is not None and not self.subscribed:
                print(f"Cancel stream subscribtion to {self.name}")
                self.responses_stream.cancel()
                break
        return self._requests_stream._results
