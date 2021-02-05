"""
Requests Streaming Iterator.
"""

import threading
import queue as q
from typing import Union, Callable, Iterable, Optional
from eventstore_grpc import streams, persistent


class RequestsStream:
    """RequestStream."""
    _lock = threading.RLock()

    def __init__(self, handler: Optional[Callable] = None, queue: Optional[Iterable] = None, persistent: bool = False):
        self._handle_task = handler
        self._tasks = q.Queue()
        self._queue = q.Queue()
        if queue is not None:
            for request in queue:
                self._queue.put(request)
        self._results = []
        self._persistent = persistent

    def __iter__(self):
        return self

    def __next__(self):
        if self._queue.empty() and self._tasks.empty():
            raise StopIteration
        
        next_element = self._queue.get()
        self._queue.task_done()
        return next_element
    
    def handle_task(self, task):
        if self._handle_task is not None:
            with RequestsStream._lock:
                try:
                    result = self._handle_task(task)
                except Exception as err:
                    print(err)
                    if self._persistent:
                        if task.HasField("event"):
                            self._queue.put(persistent.nack_request(task))
                    result = None
                if self._persistent:
                    if task.HasField("event"):
                        self._queue.put(persistent.ack_request(task))
                self._results.append(result)


    def collect(self, task):
        """Adds a task to the tasks queue."""
        if task is not None:
            self._tasks.put(task)
        return self

    def update(self, task):
        self.collect(task)
        if not self._tasks.empty():
            task = self._tasks.get()
            self.handle_task(task)
        return self
