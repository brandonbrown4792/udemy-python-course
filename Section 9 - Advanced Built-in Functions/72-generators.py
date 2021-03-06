def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


# Store generator in variable
g = hundred_numbers()

# Ask for next number in generator
print(next(g))
print(next(g))
print(next(g))

# This can turn a generator into a list
# This includes all items in generator
print(list(g))
