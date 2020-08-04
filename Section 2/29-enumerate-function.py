friends = ["Rolf", "John", "Anna"]

# Enumerate returns the index and value for the enumerable
# start argument starts enumerator at specific value
for counter, friend in enumerate(friends, start = 1):
  print(counter)
  print(friends)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))