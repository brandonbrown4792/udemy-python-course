from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


# This tells python that we can await coroutings - this is the same as yield from g (passing values to other generators)
async def greet(g):
    print('Starting...')
    await g
    print('Ending...')


greeter = greet(friend_upper())
greeter.send(None)  # Prime the generator
greeter.send('Hello')

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)
