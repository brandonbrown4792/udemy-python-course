friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friend_ages["Rolf"])

# This adds a key, value pair to the dictionary
friend_ages["Bob"] = 20
print(friend_ages)

# This updates a value for a key
# There can be no duplicate keys
friend_ages["Rolf"] = 25
print(friend_ages["Rolf"])

# Tuple of dictionaries
friends = (
  {"name": "Rolf Smith", "age": 24},
  {"name": "Adam Wool", "age": 30},
  {"name": "Anne Pun", "age": 27}
)
print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

# Converts list of tuples to dictionary
friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friend_ages = dict(friends)
print(friend_ages)