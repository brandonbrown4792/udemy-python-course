friends = ["Rolf", "Bob", "Anne"]

print(friends[0])
print(friends[1])
print(len(friends))

new_friends = [
    ["Rolf", 24],
    ["Bob", 30],
    ["Anne", 27],
    ["Charlie", 25],
    ["Jen", 25],
    ["Adam", 29]
]
print(friends[0][0])

friends.append("Jen")
print(friends)

new_friends.remove(["Anne", 27])
print(new_friends)
