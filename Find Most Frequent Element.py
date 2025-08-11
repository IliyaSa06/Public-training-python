numbers = [1, 2, 2, 3, 3, 3, 4]
max_count = 0
most_common = None
for num in numbers:
    count = 0
    for n in numbers:
        if n == num:
            count += 1
    if count > max_count:
        max_count = count
        most_common = num
print(most_common)