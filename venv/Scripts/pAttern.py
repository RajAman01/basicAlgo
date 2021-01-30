for i in range(4):
    print("*"*i)
n = 5
for i in range(0,n):
    for j in range(0,n-1):
        print(end=" ")
    n = n-1
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
d = 6
for i in range(d,0,-1):
    for j in range(d-1,0,-1):
        print(end="")
    d = d-1
    for j in range(d,0,-1):
        print("* ",end='')
    print("\r")