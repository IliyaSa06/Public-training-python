numbers = [2, 3, 2, 5, 3, 7]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)