M = 21
N = 1
for i in range(N):
    pattern = ".|."
    for i in range(N):
        if i < (N-1)/2:
            print((pattern * (2+i+1)).center(M, "_"))
        elif i == (N-1)/2:
            print(("WELCOME".center(M, "_")))
        else:
            print((pattern *(2*(N-1-i))).center(M, "_"))