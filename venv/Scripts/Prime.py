def checkPrime(n):
    if n < 1:
        for i in range(2, n):
            if (n % i == 0):
                print("Number is not prime")
            else:
                sum(n)
    else:
        print("Number is prime")


checkPrime(41)


def sum(n):
    numList = []
    while (n > 0):
        numList.append(int(n % 10))
        n = int(n / 10)
    print(numList)
    d = 1
    for i in range(len(numList)):
        if (numList[i] % d == 0):
            print("Number is not prime")
            d += 1
        else:
            print("Number is prime")
            d += 1
