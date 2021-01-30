def HalfSort(list):
    mid = len(list) // 2
    for i in range(mid):
        for j in range(0, mid):
            if (list[j] > list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
        for k in range(mid + 1, len(list) - 1):
            if (list[k] < list[k + 1]):
                list[k], list[k + 1] = list[k + 1], list[k]
    return list


list = [8, 9, 6, 17, 5, 4, 3, 2, 1]
print(HalfSort(list))
