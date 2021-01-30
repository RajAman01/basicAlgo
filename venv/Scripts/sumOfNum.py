def GetSum(num):
    sum = 0
    while(num != 0):
        sum = sum + int(num%10)
        num = int(num/10)
    return sum
print (GetSum(45))