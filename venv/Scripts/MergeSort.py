str = "efdfvb"
temp = 1
for i in range(len(str)-1):
    if(str[i] == " " and str[i+1] != " "):
        temp +=1
print(temp)
for i in range(len(str)):
    print(str[0:i])
    if (len(str[0:i])) == len(str):
        break
