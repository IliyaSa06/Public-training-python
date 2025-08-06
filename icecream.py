# Ice cream prices
vanilla = 8000
chocolate = 10000
strawberry = 12000
coffee = 15000
pistachio = 17000

# Orders storage
order1 = 0
order2 = 0
order3 = 0

# Show menu
print("Our Ice Cream Menu:")
print("1- Vanilla (8000 Tomans)")
print("2- Chocolate (10000 Tomans)")
print("3- Strawberry (12000 Tomans)")
print("4- Coffee (15000 Tomans)")
print("5- Pistachio (17000 Tomans)")

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

# Apply 15% discount if total is more than 30,000 Tomans
if total > 30000:
    discount = total * 0.15
    final_total = total - discount
else:
    discount = 0
    final_total = total

# Print receipt
print("\n--- Final Receipt ---")
print("Customer 1:", order1, "Tomans")
print("Customer 2:", order2, "Tomans")
print("Customer 3:", order3, "Tomans")
print("\nSubtotal:", total, "Tomans")
if discount > 0:
    print("Discount (15%):", int(discount), "Tomans")
print("Total Amount:", int(final_total), "Tomans")