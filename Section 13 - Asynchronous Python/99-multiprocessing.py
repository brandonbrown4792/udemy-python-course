import time
from multiprocessing import Process


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


process = Process(target=complex_calculation)
# process2 = Process(target=ask_user)  This causes an error because the process does not have access to the terminal
process2 = Process(target=complex_calculation)  # This works because the process does not need the terminal

# Doing this runs both processes in different cores, so they can run at the same time (unlike complex operation threading)
# User multiprocessing when you need two things to run at the same time
process.start()
process2.start()

start = time.time()

process.join()
process2.join()

print(f'Two process total time: {time.time() - start}')
