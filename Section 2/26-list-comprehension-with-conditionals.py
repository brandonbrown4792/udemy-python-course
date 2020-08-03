ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 != 0]
print(odds)

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

present_friends = [
  name.title() 
  for name in guests 
  if name.lower() in friends_lower
]
print(present_friends)