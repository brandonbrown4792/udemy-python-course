friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
    print(friend)


elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for _ in elements:  # Underscore indicates we do not want to use this variable
    print("Hello, world!")  # Prints 10 times

for index in range(10):
    # Prints "Hello world!" 10 times but includes index as 0..9
    print("Hello, world!")

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} made a {grade}")
