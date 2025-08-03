# Ice cream prices
vanilla = 10000
chocolate = 12000
strawberry = 15000
coffee = 18000
pistachio = 20000

# Orders storage
order1 = 0
order2 = 0
order3 = 0

# Show menu
print("Our Ice Cream Menu:")
print("1- Vanilla (10000 Tomans)")
print("2- Chocolate (12000 Tomans)")
print("3- Strawberry (15000 Tomans)")
print("4- Coffee (18000 Tomans)")
print("5- Pistachio (20000 Tomans)")

# Customer 1 orders
while True:
    choice = input("\nCustomer 1: Which ice cream do you want? (1-5) ")
    if choice == "1":
        order1 = vanilla
        print("Vanilla selected")
        break
    elif choice == "2":
        order1 = chocolate
        print("Chocolate selected")
        break
    elif choice == "3":
        order1 = strawberry
        print("Strawberry selected")
        break
    elif choice == "4":
        order1 = coffee
        print("Coffee selected")
        break
    elif choice == "5":
        order1 = pistachio
        print("Pistachio selected")
        break
    else:
        print("Please enter a number between 1-5!")

# Customer 2 orders
while True:
    choice = input("\nCustomer 2: Which ice cream do you want? (1-5) ")
    if choice == "1":
        order2 = vanilla
        print("Vanilla selected")
        break
    elif choice == "2":
        order2 = chocolate
        print("Chocolate selected")
        break
    elif choice == "3":
        order2 = strawberry
        print("Strawberry selected")
        break
    elif choice == "4":
        order2 = coffee
        print("Coffee selected")
        break
    elif choice == "5":
        order2 = pistachio
        print("Pistachio selected")
        break
    else:
        print("Please enter a number between 1-5!")

# Customer 3 orders
while True:
    choice = input("\nCustomer 3: Which ice cream do you want? (1-5) ")
    if choice == "1":
        order3 = vanilla
        print("Vanilla selected")
        break
    elif choice == "2":
        order3 = chocolate
        print("Chocolate selected")
        break
    elif choice == "3":
        order3 = strawberry
        print("Strawberry selected")
        break
    elif choice == "4":
        order3 = coffee
        print("Coffee selected")
        break
    elif choice == "5":
        order3 = pistachio
        print("Pistachio selected")
        break
    else:
        print("Please enter a number between 1-5!")

# Calculate total
total = order1 + order2 + order3

# Print receipt
print("\n--- Final Receipt ---")
print("Customer 1:", order1, "Tomans")
print("Customer 2:", order2, "Tomans")
print("Customer 3:", order3, "Tomans")
print("\nTotal Amount:", total, "Tomans")