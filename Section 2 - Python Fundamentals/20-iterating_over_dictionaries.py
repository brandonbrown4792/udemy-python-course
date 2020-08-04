friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name in friend_ages:
    print(name)  # Prints names (keys)

for age in friend_ages.values():
    print(age)  # Prints ages (values)

# The best way
for name, age in friend_ages.items():
    print(f"{name} is {age} years old")  # Prints name (key) and ages (value)
