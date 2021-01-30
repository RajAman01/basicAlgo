def count(list1):
    x = list(dict.fromkeys(list1))
    for i in x:
        print("\n {} occure {} times".format(i, list1.count(i)))


list1 = [1, 1, 1, 5, 5, 6, 7, 8, 9, 8, 5, 9, 6, 8, 5, 2]
count(list1)
