import time


def countdown(n):
    while n > 0:
        yield n
        n -= 1


tasks = [countdown(10000), countdown(5000), countdown(20000)]

start = time.time()
while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        # print(x)
        tasks.append(task)
    except:
        # print('Task finished')
        pass

print(f'Multi-threading: {time.time() - start}')


# This is faster, however, it does everything one at a time.
tasks = [countdown(10000), countdown(5000), countdown(20000)]

start = time.time()
while tasks:
    task = tasks[0]
    try:
        x = next(task)
        # print(x)
    except:
        tasks.remove(task)
        # print('Task finished')

print(f'One at a time: {time.time() - start}')
