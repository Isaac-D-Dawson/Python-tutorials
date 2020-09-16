#Memoiseation.p 19.11.2019

#memoiseation is a way to optimise memory-excessive or slow programs by
# chachine answers from expensive function calls.
#emaple
import time

ef_cache = {}

def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]
    else:
        print(f"computing {num}...")
        time.sleep(1)
        result = num*num
        ef_cache[num] = result
        return result

numbers = [4, 10, 10, 4]

for i in numbers:
    print(expensive_func(i))

#Anything generated by expensive_func is cached in "ef_cache" and is withdrawn, saving time in exchange for memory.