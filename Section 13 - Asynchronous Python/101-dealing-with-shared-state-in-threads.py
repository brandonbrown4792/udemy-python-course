# Atomic operations cannot be interrupted in the middle of its execution
# Print is a good example (cannot print only half a line)

import time
import random

from threading import Thread

counter = 0


def increment_counter():
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f'new counter value: {counter}')
    time.sleep(random.random())
    print('---------')


for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()
