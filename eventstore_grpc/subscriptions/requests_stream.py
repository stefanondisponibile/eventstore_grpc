"""
Requests Streaming Iterator.
"""

import threading
import queue as q
from typing import Union, Callable, Iterable, Optional
from eventstore_grpc import streams, persistent
import time


class RequestsStream:
    """RequestStream."""

    _lock = threading.RLock()

    def __init__(
        self,
        handler: Optional[Callable] = None,
        queue: Optional[Iterable] = None,
        persistent: bool = False,
    ):
        self._handle_task = handler
        self._tasks = q.Queue()
        self._queue = q.Queue()
        if queue is not None:
            for request in queue:
                self._queue.put(request)
        self._results = []
        self._persistent = persistent
        self._stop = threading.Event()

    def __iter__(self):
        return self

    def __next__(self):
        next_element = None

        while next_element is None:
            try:
                next_element = self._queue.get_nowait()
            except Exception:
                if self._stop.is_set():
                    print("\033[38;5;196mStopping requests streaming.\033[0m")
                    raise StopIteration
        self._queue.task_done()
        print(f"\033[38;5;45m---- to server --->\033[0m")
        print(f"\033[38;5;45m{next_element}\033[0m")
        print("\033[38;5;45m<-------------------\033[0m")
        return next_element

    def handle_task(self, task):
        print("\033[38;5;79m<---- from server --\033[0m")
        print(f"\033[38;5;79m{task}\033[0m")
        print("\033[38;5;79m------------------->\033[0m")
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
                        ack_request = persistent.ack_request(task)
                        self._queue.put(ack_request)
                self._results.append(result)
    
    def stop(self):
        self._stop.set()

    def collect(self, task):
        """Adds a task to the tasks queue."""
        if task is not None:
            self._tasks.put(task)
        return self

    def update(self, task):
        if self._stop.is_set():
            return self

        self.handle_task(task)

        # self.collect(task)
        # if not self._tasks.empty():
        #     task = self._tasks.get(lock=False)
        #     self.handle_task(task)
        #     self._tasks.task_done()
        return self
