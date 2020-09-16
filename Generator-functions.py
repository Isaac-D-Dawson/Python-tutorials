#generator-functions.py     03.03.2020

def square_numbers(nums):
    for i in nums:
        yield (int(i)**2)
myNums = square_numbers("1,2,3,4,5".split(","))

for i in myNums:
    print(i)
