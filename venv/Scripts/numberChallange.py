d = 50
c = bin(d)
e = hex(d)
print((e).upper())
def binary(d):
    if d > 1:
        binary(d//2)
        print(d//2,"hi")
        print(d%2,end="")
binary(d)