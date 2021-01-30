def sortestElement(arr):
    temp = arr[0]
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if (arr[j] > arr[j + 1]):
                temp = arr[j + 1]
    return temp


arr = [8, 9, 5, 3, 7, 2, 1, 0]
result = sortestElement(arr)
print(result)
