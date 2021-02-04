import logging
import time
import random
import sys
import threading
from eventstore_grpc.subscription import Subscription

logging.basicConfig(level=logging.DEBUG)

SLOW_DOWN = False
STOP_FIRST_THREAD = False

if "--stop-first-thread" in sys.argv:
    STOP_FIRST_THREAD = True

if "--slow-down" in sys.argv:
    SLOW_DOWN = True

def some_stream():
    counter = 0
    while True:
        if counter == 10:
            break
        counter += 1
        yield counter
        if SLOW_DOWN:
            time.sleep(random.randint(2,10))

class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
    
    def update(self, value: int):
        self.count = value
    
counter = Counter()

    
def some_handler(element, current_thread: threading.Thread = None, *args, **kwargs):
    """Handles the elment received from the stream."""
    current_value = counter.count
    if SLOW_DOWN:
        time.sleep(random.randint(1,5))
    counter.update(current_value + 1)
    print(f"\033[92mHandling iteration number {element:^3} \033[38;5;226m[{name:^20}]\033[92m-[\033[38;5;117m{counter.count:^4}\033[92m] [{id(counter)}]\033[0m")


number_of_streams = 10
stream_names = [f"thread_stream_{i}" for i in range(number_of_streams)]

subscriptions = {}

for stream_name in stream_names:
    subscription = Subscription(some_stream, some_handler, name=stream_name)
    if stream_name in subscriptions:
        registered_subscription = subscriptions[stream_name]
        registered_subscription.subscribed = False
    subscriptions[stream_name] = subscription
    subscriptions[stream_name].start()

if STOP_FIRST_THREAD:
    first_thread = "thread_stream_0"
    if SLOW_DOWN:
        time.sleep(random.randint(2,5))
    subscriptions[first_thread].subscribed = False
