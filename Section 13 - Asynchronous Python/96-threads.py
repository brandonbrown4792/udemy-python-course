import time
from threading import Thread  # Threads in Python are really only good for reducing waiting time (can't run two things at the same time)


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')  # Input is considered a blocking operation
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask user, {time.time() - start}')


def complex_calculation():
    start = time.time()
    [x ** 2 for x in range(20000000)]
    print(f'complex_operation, {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')


thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()

thread1.join()  # This makes the main thread wait for thread1 to finish
thread2.join()

print(f'Two thread total time: {time.time() - start}')


# Not a good use of threads because both threads are computationally expensive
# Python will switch between the two processes until both are finished
# Running this without threads is faster because you don't have to switch between the two threads
thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=complex_calculation)

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Two complex thread total time: {time.time() - start}')
