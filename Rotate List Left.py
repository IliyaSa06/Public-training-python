lst = [1, 2, 3, 4, 5]
k = 2
for _ in range(k):
    temp = lst[0]
    for i in range(len(lst)-1):
        lst[i] = lst[i+1]
    lst[-1] = temp
print(lst)