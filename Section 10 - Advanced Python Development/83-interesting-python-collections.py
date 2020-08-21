"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

# Counts the amount of entries there are of a certain value
temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])


# defaultdict never raises a key error
# Instead it returns the value of the object when it was instantiated
coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'),
             ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

# # Old way of doing this:
# alma_maters = {}
# for coworker, place in coworkers:
#     if coworker not in alma_maters:
#         alma_maters[coworker] = []
#     alma_maters[coworker].append(place)

# Doing it with defaultdict
alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

# # This will remove the default factory which will cause a key error when trying to access keys that do not exist
# alma_maters.default_factory = None

print(alma_maters['Rolf'])
print(alma_maters['Anne'])

# Another example

my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

# This is called when trying to access a key that doesn't exist
coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers[0]])
print(coworker_companies['Rolf'])


# Ordered Dictionary
# Ordered by when they were inserted
o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)

o.move_to_end('Rolf')
print(o)
o.move_to_end('Jen', last=False)
print(o)
o.popitem()
print(o)


# Named Tuple
account = ('checking', 1850.90)

Account = namedtuple('Account', ['name', 'balance'])

tuple_account = Account('checking', 1850.90)
# Named tuples allow you to access properties in the tuple
print(tuple_account.name, tuple_account.balance)

account_named_tuple = Account._make(account)
print(account_named_tuple.name, account_named_tuple.balance)
print(account_named_tuple._asdict())


# Deque - double-ended queue
# Deques are thread safe (will look at this later)
friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')
print(friends)
friends.pop()
friends.popleft()
print(friends)
print(friends.pop())
print(friends.popleft())
print(friends)
