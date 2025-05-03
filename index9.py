# prices = [15, 40, 32]
#
# result = 0
# for price in prices:
#     result += price
# print(f"Result is {result}")


# for x in range(3):
#     for y in range(4):
#         print(f"{x},{y}")


stuffs = [[1 , 2 , 3], ["Python", "Iliya"], [10,5]]

for stuff in stuffs:
    for item in stuff:
        print(f"{item} ", end='')
    print()