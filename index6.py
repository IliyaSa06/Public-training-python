numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Alex", "Bob", "Charlie", "David", "Eve", "Fred"]
stuff = [1 , 7 , "Mahdi" , 10 , "Python"]




stuff[3] = 2


numbers.extend(names)
numbers.append(55)
numbers.insert(3, 15)
names.sort()
names.reverse()
copy_numbers = numbers.copy()
print(numbers)
print(copy_numbers)

print(names)

names.remove("Bob")
# names.clear()
print(names.index("David"))
print(names.count("David"))

print(names)