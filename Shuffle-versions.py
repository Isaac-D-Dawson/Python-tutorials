def shuffled(l1, n):
    import random
    list_copy = [i for i in l1]
    random.shuffle(list_copy)
    if list_copy != l1:
        print(n)
        return list_copy
    else:
        n=+ 1
        return shuffled(l1, n)

testList = ["1", "2"]

print(testList)
print(shuffled(testList, 0))
print(testList)