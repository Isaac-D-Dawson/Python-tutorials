#Lists, tuples, and Sets.

#A list is a list of data, stored in a variable. the data can be accessed by calling the relevant index.
shopping = ["Apples", "Milk", "Cat food", "Toilet paper"]
print(shopping)
#keep in mind the indexes start at zero.
# the last number isthe length of the list minus one.
#Calling a negative index starts from one at the oposite end of the list.
#acessing a non-existent index returns an error.
#Ranges will return the result of the range.
# Eg, 1:4 will return the contents of slots one, two, and three.


#The .append() method, will add its inputs to whichever list it's called on.
shopping.append("Earl Grey, Hot",)
print(shopping)
#note that append will change the list it's called on, and cannot take more than one input.

# the .insert() method takes two arguments; The location to insert something, and the thing to insert
shopping.insert(1, "Cornflakes")
print(shopping)
#note that the .insert method will not overwrite other items in the array.
# You can also inert an entire array using insert, though the new array will have a single index.

#the .extend() method adds multiple values to our list.
extraShopping = ["Roasted peanuts", "Bread", "Giraffe bread"]
shopping.extend(extraShopping)
print(shopping)
#Note, that like .append(), .extend() will not overwrite anything in the original array.

#the .remove method removes the content provided from the array.
shopping.remove("Giraffe bread")
print(shopping)
#note that this will remove only the
# first instance it encounters that match it's search paramiters
#EG:
numbers = [1, 2, 3, 2, 1]
numbers.remove(2)
print(numbers)

#the .pop() method removes the last item on the list
shopping = ["eggs", "bacon", "carrots"]
shopping.pop()
print(shopping)
#note that you can save the popped item to a new variable
shopping = ["eggs", "bacon", "carrots"]
oldShopping = shopping.pop()
print(oldShopping)

#the .reverse() method takes a lsit an reverses it
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)
#Note that.reverse will overwrite the original with the reversed copy.

#the .sort() metjod sorts a list
numbers = [1, 3, 2, 6, 3, 4, 99]
words =  ["apples", "John", "Bernard", "lawrence", "Terry", "T3r3z1", "zygote"]
numbers.sort()
words.sort()
print(numbers)
print(words)
#Note that .sort() will overwrite the original list.

#continued on 22.10.2019

#The sorted() function works similarly to .sort(), however it does not overwrite the original.
numbers = [1, 4, 2, 2, 0, 99, 3]
print(sorted(numbers))
print(numbers)
#it will NOT overwrite the original. Remember,
# the function doesn't overwrite, the method does.

#The min() function returns the smallest value in a list.
numbers = [1, 2, 3, 4, 5]
print(min(numbers))
#returns one. note that it will return the smallest value in the list, not just the first one.
# if called on a string it will return a value equivilent to the first item in a sorted array.
# If called on a list with both strings AND numbers, it will fail. Do NOT do this.

#The max() function returns the largest value in a list,
numbers = [1, 2, 3, 4, 5]
print(max(numbers))
#This will return 5. Again, it is not returning the LAST time, but the LARGEST, item.
#As with min(), this can be called on a list containing strings.
# if called on a lsit of strings, it will return the last item of a sorted list.
# if called on a lsit with both strings AND numbers, it will fail. Do NOT do this,

#The sum() function will sum all the items in a list.
numbers = [1, 2, 3 , 4, 5]
print(sum(numbers))
#This returns 15. If called on a list that contains strings it will fail.

#The .index() method will find an item in a list and return the index of it.
items = ["pencil-case", "calculator", "Book", "Book", "Penguin"]
print(items.index("calculator"))
#this returns the index of the item you searched for.
#if there are multipe duplicate items in a list it will only
# return the index of the firs item it finds that matches.

#



#test instance for reversing an array
array1 = [1, 2, 3]
array2 = []

array2.append(array1.pop())
array2.append(array1.pop())
array2.append(array1.pop())

print(array2)

#obscure test case for insert.
numbers1 = [1, 2, 6, 7, 8]
numbers2 = [3, 4, 5]
numbers1.insert(2, numbers2[2])
numbers1.insert(2, numbers2[1])
numbers1.insert(2, numbers2[0])

print(numbers1)

#test for min()
testList = ["William-Carter", "Alfred", "johnathon", "bill", "Billy"]
print(min(testList))
print(sorted(testList))