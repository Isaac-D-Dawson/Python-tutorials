# #Lists, tuples, and Sets.

# #A list is a list of data, stored in a variable. the data can be accessed by calling the relevant index.
# shopping = ["Apples", "Milk", "Cat food", "Toilet paper"]
# print(shopping)
# #keep in mind the indexes start at zero.
# # the last number isthe length of the list minus one.
# #Calling a negative index starts from one at the oposite end of the list.
# #acessing a non-existent index returns an error.
# #Ranges will return the result of the range.
# # Eg, 1:4 will return the contents of slots one, two, and three.


# #The .append() method, will add its inputs to whichever list it's called on.
# shopping.append("Earl Grey, Hot",)
# print(shopping)
# #note that append will change the list it's called on, and cannot take more than one input.

# # the .insert() method takes two arguments; The location to insert something, and the thing to insert
# shopping.insert(1, "Cornflakes")
# print(shopping)
# #note that the .insert method will not overwrite other items in the array.
# # You can also inert an entire array using insert, though the new array will have a single index.

# #the .extend() method adds multiple values to our list.
# extraShopping = ["Roasted peanuts", "Bread", "Giraffe bread"]
# shopping.extend(extraShopping)
# print(shopping)
# #Note, that like .append(), .extend() will not overwrite anything in the original array.

# #the .remove method removes the content provided from the array.
# shopping.remove("Giraffe bread")
# print(shopping)
# #note that this will remove only the
# # first instance it encounters that match it's search paramiters
# #EG:
# numbers = [1, 2, 3, 2, 1]
# numbers.remove(2)
# print(numbers)

# #the .pop() method removes the last item on the list
# shopping = ["eggs", "bacon", "carrots"]
# shopping.pop()
# print(shopping)
# #note that you can save the popped item to a new variable
# shopping = ["eggs", "bacon", "carrots"]
# oldShopping = shopping.pop()
# print(oldShopping)

# #the .reverse() method takes a lsit an reverses it
# numbers = [1, 2, 3]
# numbers.reverse()
# print(numbers)
# #Note that.reverse will overwrite the original with the reversed copy.

# #the .sort() metjod sorts a list
# numbers = [1, 3, 2, 6, 3, 4, 99]
# words =  ["apples", "John", "Bernard", "lawrence", "Terry", "T3r3z1", "zygote"]
# numbers.sort()
# words.sort()
# print(numbers)
# print(words)
# #Note that .sort() will overwrite the original list.

# #continued on 22.10.2019

# #The sorted() function works similarly to .sort(), however it does not overwrite the original.
# numbers = [1, 4, 2, 2, 0, 99, 3]
# print(sorted(numbers))
# print(numbers)
# #it will NOT overwrite the original. Remember,
# # the function doesn't overwrite, the method does.

# #The min() function returns the smallest value in a list.
# numbers = [1, 2, 3, 4, 5]
# print(min(numbers))
# #returns one. note that it will return the smallest value in the list, not just the first one.
# # if called on a string it will return a value equivilent to the first item in a sorted array.
# # If called on a list with both strings AND numbers, it will fail. Do NOT do this.

# #The max() function returns the largest value in a list,
# numbers = [1, 2, 3, 4, 5]
# print(max(numbers))
# #This will return 5. Again, it is not returning the LAST time, but the LARGEST, item.
# #As with min(), this can be called on a list containing strings.
# # if called on a lsit of strings, it will return the last item of a sorted list.
# # if called on a lsit with both strings AND numbers, it will fail. Do NOT do this,

# #The sum() function will sum all the items in a list.
# numbers = [1, 2, 3 , 4, 5]
# print(sum(numbers))
# #This returns 15. If called on a list that contains strings it will fail.

# #The .index() method will find an item in a list and return the index of it.
# items = ["pencil-case", "calculator", "Book", "Book", "Penguin"]
# print(items.index("calculator"))
# #this returns the index of the item you searched for.
# #if there are multipe duplicate items in a list it will only
# # return the index of the firs item it finds that matches.
# # If it can't find the item at all it will return an arror.

# # the "in" operator returns a boolean value for if the item is/is not in the list.
# items = ["pencil-case", "calculator", "Book", "Book", "Penguin"]
# print("Penguin" in items)
# #This is useful if you do not know if something is in a list, but do not want it to return an error.
# # if the list you're searching for does not exist, it will return an error.

# #the "for" loop is used to iterate through things. a very basic example of it would be:
# items = ["pencil-case", "calculator", "Book", "Book", "Penguin"]
# for item in items:
#     print(item)
# #Which will print each item in the list, in order.
# #note that print() returns the item followed by a newline.
# # also note that, in python, the indentation is important.
# # Here it specifies that the code below is a subest of the code above,
# # the "print()" is a part of the for loop.
# # the "item' in this example is a temporary variable for this one edge case.

# #The enumerate() function returns the index of the items as
# # the for loop iterates through the list.
# for item in enumerate(items):
#     print(item)
# #Note that it returns the index value, so the first item will be the 0th index, etc.
# # Note that calling Enumerate() on a list directly returns the hardware address of the list.
# #enumerate() can also be passed a starting value.
# for item in enumerate(items, start=1):
#     print(item)
# #Note that this does not affect the index the function reads from,
# # Just the values shown.

#continued on 29.10.2019

# #The .join() method takes two inputs; a string, and a list.
# # It then formats the list, inserting the string between each list item. EG:
# backpack = ["pencil-case", "calculator", "Book", "Book", "Penguin"]
# backpack_str = ", ".join(backpack)
# print(backpack_str)
# #Returns "pencil-case, calculator, Book, Book, Penguin"

# #The oposite of this is the .split() method.
# # This method takes in two strings, and seperates the items
# # in the string in FRONT of it everywhere the string bEHIND it occurs.
# #EG: 
# backpack_list = backpack_str.split(", ")
# print (backpack_list)
# #returns "['pencil-case', 'calculator', 'Book', 'Book', 'Penguin']",
# # the original array.

# #tuples are like lists, but they cannot be changed.
# # lists are "muteable", they can be changed,
# # tuples are "immuteable", they cannot be changed
# #EG:
# my_backpack = ['pencil-case', 'calculator', 'Book', 'Book', 'Penguin', "peanuts"]
# my_backpack_2 = my_backpack

# print (my_backpack)
# print (my_backpack_2)
# my_backpack.pop()

# print (my_backpack)
# print (my_backpack_2)
# #Note that the change to the first list also changed the second list.
# #This can be fixed by making the second list a tuple.
# my_backpack = ['pencil-case', 'calculator', 'Book', 'Book', 'Penguin', "peanuts"]
# my_backpack_2 = tuple(my_backpack)

# print (my_backpack)
# print (my_backpack_2)
# #my_backpack_2.pop() Throws an error
# my_backpack[-1] = "Severe lack of Peanuts"

# print (my_backpack)
# print (my_backpack_2)
# #As you can see, Tuples can't be changed.
# #Trying to change a tuple throws an error.
# #The tuple() method creates a tuple from an existing list.
#Also note that when printed, tuples display the same () edges.

#Sets

# #sets are like lists except they:
# #-do not have index's and attached operations
# #-remove duplicate items.
# #
# #This means they are very useful for determining if an item is in a list.
# #
# #sets use Curly Braces "{}". The contents of a set are stored in a random order.
# my_backpack = {'pencil-case', 'calculator', 'Book', 'Book', 'Penguin', "peanuts"}

# # print(my_backpack)
# # #This code will return the contents of "my_backpack", but in a random order.
# # print("Book" in my_backpack)
# #This will return "True" as there is at least one "Book" item in the set.

# #Sets can also compare differences more efficiently than lists,
# #This uses the .intersection method.
# left_pocket = {"Chopsticks", "Penguin", "I.D. ", "Fidget toy"}
# right_pocket = {"I.D. ", "Sweets", "Chopsticks", "Pen"}

# print(left_pocket.intersection(right_pocket))
# #This returns "{'I.D. ', 'Chopsticks'}" as a set.
# # These are items consistent between both sets.
# #Keep in mind that as long as the two parameters are both sets

# #The .difference() method also compares two sets.
# # This lists all items present in the first set that ARE NOT present in te second set.
# # EG:
# print(left_pocket.difference(right_pocket))
# #returns "{'Penguin', 'Fidget toy'}"
# #Which are present in the first set, but not in the second.

# #The .union() method returns a set containing everything in
# # both provided sets(With duplicates removed)
# print(left_pocket.union(right_pocket))
# #Note that since the result is a set, duplicate items WILL be REMOVED

# #Note that sets cannot be created empty, attmepting to do so will create an empty dictionary.
# empty_set = {} #makes a dictionary.
# #instead ou have to create a new, empty set object:
# empty_set = set{}
# #This will create a set with no content.



# #Test case for playing with enumerate() and indexes
#items  = ["pencil-case", "calculator", "Book", "Book", "Penguin"]
# #for index, item in enumerate(items, start=0):
#    print (index, item)


# for index, item in enumerate(items, start=1):
#     print(item)
# # Are you satisfied? Are you Happy? I had to cheat to work this out, and even then it took me five combinations to hit the syntax that worked.
#So tell me. Are. You. Satisfied?

# test_string = "string!"
# for letter in enumerate(test_string, start=1):
#     print(letter)

#for item in items:
#    print(str(items.index(item)) + " "+ item)

# #test instance for reversing an array
# array1 = [1, 2, 3]
# array2 = []

# array2.append(array1.pop())
# array2.append(array1.pop())
# array2.append(array1.pop())

# print(array2)

# #obscure test case for insert.
# numbers1 = [1, 2, 6, 7, 8]
# numbers2 = [3, 4, 5]
# numbers1.insert(2, numbers2[2])
# numbers1.insert(2, numbers2[1])
# numbers1.insert(2, numbers2[0])

# print(numbers1)

# #test for min()
# testList = ["William-Carter", "Alfred", "johnathon", "bill", "Billy"]
# print(min(testList))
# print(sorted(testList))