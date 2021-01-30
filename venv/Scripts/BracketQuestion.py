str = "{{{{}{}{}}}}}"
def findBracket(str):
    open = 0
    close = 0
    for i in range(len(str)):
        if (str[i] == "{"):
            open += 1
        else:
            close += 1
    if (open < close):
        print(close - open)
    else:
        print(open - close)
if __name__ == "__main__":
    findBracket(str)