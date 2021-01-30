# Python program for checking
# of full prime
# function to check digits
def checkDigits(n):
    # check all digits are
    # prime or not
    while (n):
        dig = n % 10
        # check if digits are
        # prime or not
        if (dig != 2 and
                dig != 3 and dig != 5
                and dig != 7):
            return 0
        n = n / 10
    return 1
# To check if n is prime or not
def prime(n):
    if (n == 1):
        return 0
    # check for all factors
    i = 2
    while i * i <= n:
        if (n % i == 0):
            return 0
        i = i + 1
    return 1
# To check if n is Full Prime
def isFullPrime(n):
    # The order is important here
    # for efficiency.
    return (checkDigits(n) and prime(n))
# Driver code
n = int(input("Enter the Number to check mega Prime Number"))
if (isFullPrime(n)):
    print("Yes")
else:
    print("No")
# This code is contributed by rishabh_jain
