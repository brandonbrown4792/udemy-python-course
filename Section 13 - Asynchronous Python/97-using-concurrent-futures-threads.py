import time
from concurrent.futures import ThreadPoolExecutor


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
print(f'Single thread totla time: {time.time() - start}')

start = time.time()

# Thread Pool makes our threading code easier to read
with ThreadPoolExecutor(max_workers=2) as pool:  # Creates a pool of threads for which we can submit tasks to.
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'Two thread total time: {time.time() - start}')
