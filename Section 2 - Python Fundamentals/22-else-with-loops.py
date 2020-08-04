#Naive approach

# cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
# all_successful = True

# for status in cars:
#   if status == "faulty":
#     print("Stopping the production line!")
#     all_successful = False
#     break
#   print(f"This car is {status}.")
#   print("Shipping new car to customer!")

# if all_successful:
#   print("All cars built successfully. No faulty cars!")



#Better approach - else keywork runs if no break or error was encountered

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
  if status == "faulty":
    print("Stopping the production line!")
    break
  print(f"This car is {status}.")
  print("Shipping new car to customer!")
else:
  print("All cars built successfully. No faulty cars!")