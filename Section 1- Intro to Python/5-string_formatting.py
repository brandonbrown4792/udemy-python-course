age = 28
print(f"You are {age}") #This is called an f-string

name = "Brandon"
greeting = f"How are you, {name}?"
print(greeting)

final_greeting = "How are you, {}?"
brandon_greeting = final_greeting.format(name)
print(brandon_greeting)

bob_greeting = final_greeting.format("Bob")
print(bob_greeting)

another_greeting = "How are you, {name}"
print(another_greeting.format(name = "Ashley"))

my_person = "Jessie"
last_greeting = "How are you, {person}"
print(last_greeting.format(person = my_person))