#Slicing lsits and strings.py       26.11.2019

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# my_test_list = []
# for i in range(0, 10):
#     my_test_list.append(i)

print(my_list[1:8])
#Alternative format for .range(). also not inclusive on the last value. See Loops.py.

#Note that slicing for strings the stop value is INCLUSIVE.
# Unless it's negative, then it is EXCLUSIVE,
my_string =  "Hello, is it me you're looking for?"
print(my_string[0: :1])