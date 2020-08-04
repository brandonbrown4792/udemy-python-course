# Lambda gives an alternate way to define functions
# If no name is assigned to the lambda function, python immediate destroys the function
divide = lambda x, y: x / y
print(divide(15, 3))

# Do not do this
print((lambda x, y: x / y)(15, 3))


def average(sequence):
  sequence: sum(sequence) / len(sequence)

# Lambda is probably not best here since a def is more readable
# average = lambda sequence: sum(sequence) / len(sequence)


students = [
  {"name": "Rolf", "grades": (67, 90, 95, 100)},
  {"name": "Bob", "grades": (56, 78, 80, 90)},
  {"name": "Jen", "grades": (98, 90, 95, 99)},
  {"name": "Anne", "grades": (100, 100, 95, 100)}
]

for student in students:
  print(average(student["grades"]))