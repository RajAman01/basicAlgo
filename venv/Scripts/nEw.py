str = "This Is my book for 13? /er 56? we will we will"
li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","/","?","-"]
d = str.split(" ")
c = len(d)
print(d)
for i in d:
    for j in range(len(i)):
        if i[j] in li:
            c -=1
            break
print(c)
