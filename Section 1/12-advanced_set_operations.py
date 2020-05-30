art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

# Art friends that are not in science friends
art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)

# Science friends that are not in art friends
science_but_not_art = science_friends.difference(art_friends)
print(science_but_not_art)

# Members not in both
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

# Members in both sets
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

# All memebers
all_friends = art_friends.union(science_friends)
print(all_friends)