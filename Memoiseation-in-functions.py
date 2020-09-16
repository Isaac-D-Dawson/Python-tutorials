#memoiseation in functions.py       09.03.2020


#basic cewxample of memoiseation.

#
def square_numbers(i):
    return i**2

#memoiseation wrapper:
sn_cache = {}
def sn_memo(j):
    if j in sn_cache:
        #print("Retrived from cache!")
        return sn_cache[j]
    else:
        k = square_numbers(j)
        sn_cache[j] = k
        return k

for i in range(0, 3):
    print(sn_memo(12))

