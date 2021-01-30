def is_leap(year):
    leap = bool
    leap = False
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
            print("True")
    else:
        leap = False
        print("False")

    # Write your logic here

    return leap


year = int(input())
print(is_leap(year))