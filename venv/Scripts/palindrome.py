str = "abcbcba"

def pal(str):
    temp = ""
    for i in range(len(str) - 1, 0, -1):
        temp += str[i]
    if (str == temp):
        return 1
    else:
        return -1


result = pal(str)
if result == 1:
    print("True")
else:
    print("False")
