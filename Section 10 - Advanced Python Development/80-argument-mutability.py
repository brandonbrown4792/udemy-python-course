friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}


def see_friend(friends, name):
    print(id(friends))
    # Prints True / False if objects are the same address
    print(friends is friends_last_seen)
    friends[name] = 0


# Because dictionaries are mutable, we see the same address in all 3 prints
print(id(friends_last_seen))
print(id(friends_last_seen['Rolf']))

see_friend(friends_last_seen, 'Rolf')

# This address is changed because the contents of dictionaries are immutable
print(id(friends_last_seen['Rolf']))
print(id(friends_last_seen))

print()
print()

age = 20


def increase_age(current_age):
    current_age += 1


# This does not change the value of age because age is an integer and integers are immutable
# In this case, a new integer called current_age is created and updated
print(id(age))
print(age)
increase_age(age)
print(id(age))
print(age)


print()
print()

primes = [2, 3, 5]

# Lists are mutable, so the prime numbers are updated
print(id(primes))
print(primes)
primes += [7, 11]
print(id(primes))
print(primes)
