cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

# Using break
# for status in cars:
#     if status == "faulty": 
#         print("Stopping the production line!")
#         break
#     print(f"This car is {status}.")
#     print("Shipping new car to customer!")

# Using continue
for status in cars:
    if status == "faulty":
        print("Faulty car, skipping...")
        continue
    print(f"This car is {status}")
    print("Shipping new car to customer!")