list1 = [1, 1, 1, 5, 5, 6, 7, 8, 9, 8, 5, 9, 6, 8, 5, 2]
x = list(dict.fromkeys(list1))
temp = []
for i in x:
    print(i)
    temp.append(list1.count(i))
temp.sort()
print(temp)