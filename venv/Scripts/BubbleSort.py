def BubbleSort(List):
    temp = 0
    for i in range(0, len(List) - 1): #To traverse List
        for j in range(len(List) - 1):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
                temp +=1
    return temp


List = [7, 1, 3, 2, 4, 5, 6]
print(BubbleSort(List))
