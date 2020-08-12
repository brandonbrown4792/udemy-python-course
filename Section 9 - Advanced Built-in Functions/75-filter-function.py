friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']


# arg1: function that returns True/False
start_with_r = filter(lambda friend: friend.startswith('R'), friends)

# This is an identical generator comprehension. This will actually perform faster since you do not have to define another function
# You should use generator comprehension if possible
another_starts_with_r = (f for f in friends if f.startswith('R'))


# print(list(start_with_r))

# # This returns an empty list because the generator has already reached the end of it's "next" statements
# print(list(start_with_r))

for friend in start_with_r:
    print(friend)

for friend in another_starts_with_r:
    print(friend)


# Another way of doing it - more complicated
def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


another_start_with_r = my_custom_filter(
    lambda friend: friend.startswith('R'), friends)

for friend in another_start_with_r:
    print(friend)
