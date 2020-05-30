name = input("Enter your name: ")
surname = input("Enter your surname: ")

greeting = name or f"Mr. {surname}"
print(greeting)

val = True and 18
print(val)

val = 18 and 0
print(val)

val = False or 17
print(val)

val = True or 17
print(val)
