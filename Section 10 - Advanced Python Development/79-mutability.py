friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

# This points to the same dictionary
# Updating another_variable will update friends_last_seen
another_variable = friends_last_seen

# id shows address in memory
print(id(friends_last_seen))
print(id(another_variable))

another_variable['Rolf'] = 32

print(friends_last_seen['Rolf'])

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

# This will print a new address
print(id(friends_last_seen))

# Updating the object does not create a new object in memory (mutated)
friends_last_seen['Rolf'] = 0
print(id(friends_last_seen))

# Same thing happens with ints

my_int = 5
print(id(my_int))
my_int = my_int + 1
print(id(my_int))
my_int += 1
print(id(my_int))

# The following are immutabe: int, float, string, tuple

# However, lists are mutable
friends = ['Rolf', 'Jose']
print(id(friends))
friends.append('Jen')
print(id(friends))
