friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
    print("This runs too.")
else:
    print("Hello, stranger!")
    print("This runs also")

print("This runs anyway.")

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you")
