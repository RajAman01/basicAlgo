def binSearch(arr, l, r, x):
    if (r >= l):
        mid = l + r // 2
        if (arr[mid] == x):
            return mid
        elif (arr[mid] > x):
            return binSearch(arr, mid + 1, r, x)
        else:
            return binSearch(arr, l, mid - 1, x)
    else:
        return -1


arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
l = 0
r = len(arr) - 1
x = 9
result = binSearch(arr, l, r, x)
if (result == -1):
    print("Not Found")
else:
    print("Found at", result)
