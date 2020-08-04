def add(x, y = 3):
  total = x + y
  return total

print(add(3))
print(add(x = 3))
print(add(3, 4))
print(add(x = 5, y = 3))
print(add(2, y = 7))

# Not valid
# print(add(x = 3, 2))

# Not valid
# print(add(y = 2))

print(1, 2, 3, 4, 5)

# Print has default value for separator as ' ' (space)
print(1, 2, 3, 4, 5, sep = ' - ')