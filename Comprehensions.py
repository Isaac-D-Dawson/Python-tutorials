#Comprehensions.py      26.11.2019

#my_list = [n for n in range(0,11, 2)]
my_list = [n for n in range(0,11) if n%2 == 0]

print(my_list)

my_new_list = [(letter, num) for letter in "a" for num in range(4)]
# my_new_list = [{letter: num} for letter in "a" for num in range(4)]
print(my_new_list)