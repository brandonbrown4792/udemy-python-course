friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

# Zip combines lists together which can then be transformed into another list or dictionary
# Zip ignores extra elements
long_timers = dict(zip(friends, time_since_seen))

print(long_timers)