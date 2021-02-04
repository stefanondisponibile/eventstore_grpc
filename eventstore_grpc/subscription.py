"""A Subscription Object."""

import logging
from typing import Callable, Iterable
import threading

log = logging.getLogger(__name__)

class Subscription(threading.Thread):
    """A Subscription Object
    
    This object spawns a new thread and run a custom callback against each of the
    elements yielded from the stream iterator.

    Attributes:
        _lock: a threading.RLock used to sync.
    """
    _lock = threading.RLock()

    def __init__(self, stream: Iterable, handler: Callable, **kwargs):
        """Initializes the subscription.
        
        Args:
            stream: an iterable.
            handler: the function that handles what's yielded from the iterable.
        """
        threading.Thread.__init__(self, **kwargs)

        self._stream = stream
        self._handler = handler
        self._unsubscribed = threading.Event()
        self.subscribed = True
    
    def run(self, *args, **kwargs):
        """Runs the thread activity."""
        log.debug(f"{self.name:^10} activity started.")
        for elm in self._stream():
            if not self.subscribed:
                log.debug(f"Stopping {self.name:^10}.")
                break
            with Subscription._lock:
                log.debug(f"Lock acquired by {self.name}.")
                self._handler(elm, current_thread=self, *args, **kwargs)
                log.debug(f"Lock released by {self.name}.")
