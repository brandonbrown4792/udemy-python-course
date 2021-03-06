from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    g.send(None)  # This is called priming the generator (runs until right before the yield)
    while True:
        greeting = yield
        g.send(greeting)


# # Alternatively, you can write the greet function as the following (no one likes to do this because it's confusing)
# def greet(g):
#     yield from g


greeter = greet(friend_upper())
greeter.send(None)  # Prime the greet generator
greeter.send('Hello')
print('Hello, world! Multi-tasking...')
greeter.send('Saluations')
