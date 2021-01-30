D= "aaa bbb ccc ddd eee fff ggg hhh iii jjj"
temp1 = ""
temp2 =""
list = []
for i in range(len(D)):
    if(D[i] == " "):
        i+=1
        temp1 = D[i:i+3]
        temp2 = D[i+4:i+7]
    list.append(temp2)
    list.append(temp1)
print(list)