str = "dfragfbngfbjfajvfdigfnvfd"


def checkStr(str):
    for i in range(len(str) - 1):
        if str[i] == "a" and str[i + 1] == "a":
            return True


result = checkStr(str)
if (result == True):
    print("True")
else:
    print("False")
