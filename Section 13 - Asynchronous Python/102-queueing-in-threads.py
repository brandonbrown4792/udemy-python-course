import time
import random
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue()  # Things to be printed out
counter_queue = queue.Queue()  # Amounts by which to increase counter


def increment_manager():
    global counter
    while True:
        increment = counter_queue.get()  # This waits until an item is available and then locks the queue
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f'New counter value is {counter}', '---------'))
        counter_queue.task_done()  # This unlocks the queue


Thread(target=increment_manager, daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
            time.sleep(random.random())
        job_queue.task_done()


Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    counter_queue.put(1)
    time.sleep(random.random())


worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    time.sleep(random.random())
    thread.start()


for thread in worker_threads:
    thread.join()

counter_queue.join()
job_queue.join()
