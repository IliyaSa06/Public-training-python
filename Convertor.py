print("Simple Unit Converter Program")
print("-----------------------------")

# 1. Convert kilograms to grams
kg = float(input("Enter weight in kilograms: "))
grams = kg * 1000
print(f"{kg} kg is equal to {grams} grams")

# 2. Convert pounds to kilograms
pounds = float(input("\nEnter weight in pounds: "))
kg_from_pounds = pounds * 0.45
print(f"{pounds} pounds is equal to {kg_from_pounds} kg")

# 3. Convert kilometers to meters and centimeters
km = float(input("\nEnter distance in kilometers: "))
meters = km * 1000
cm = km * 100000
print(f"{km} kilometers is equal to:")
print(f"- {meters} meters")
print(f"- {cm} centimeters")

print("\nProgram ended!")