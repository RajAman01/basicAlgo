def SecondLargest(list):
    for j in range(0, len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list[-2]


list = [4, 8, 6, 2, 4, 3, 9, 8, 4, 2]
print(SecondLargest(list))
