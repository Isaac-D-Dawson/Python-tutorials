#Dictionaries in Python.

#dictionaries are maps of key-value pairs, occasionally called hashmaps/ascociative arrays in other languages
#like a list, they store items in an indexed slot, except the index is defined by the programmer.

#example
student = {"name":"Dave", "age":14, "modus":"Hashmap", "courses":["Maths", "English", "Physical Education", "Biology"]}
print(student)
print(student["name"])
print(student["courses"][2])

# #the .get() method returns either the contents of the specified key or the value "None".
# #EG:
# print(student.get("specibus"))
# #Returns "None". This is useful if you don't want an invalid key to
# # return an error or crash the program.
# #Passing in a seconed value returns this value instead of "None"
# print(student.get("specibus", "Unspecified"))
# #Returns "Unspecified" as there is no Specibus value.
#This can be used as a kind of if statement.

#If you want to add a value tot the dictionary or UPDATE an exisiting value
# it is as simple as setting the dictionary with key to the value, EG:
student["specibus"] = "sword"
#The value of "sword" is now attached to the key "specibus".
print(student["specibus"])
#Note that for existing keys this will OVERWRITE the existing value. EG:
student["specibus"] = "1/2 sword"
print(student["specibus"])

#The .update() method similarly adds and overwrites keys and values to the table.
student.update({"name":"Dave Strider", "text_color":"Red", "moon":"Dense"})
print(student)
#The values for "text_color" and "moon" have been added, and the value for "name" has been updated.

# #the "del" keyword, similar to .pop() removes the target key and value from the specified dictionary. EG:
# del student["courses"] #pernamtly deletes
# #student.pop("courses") #can be retrieved
# print(student)
# #This has deleted the courses key, and the contents of it.
# #This is similar to .pop() , however it will not return the deleted value.
#Use .pop() if you want to use the delete segment again, otherwise use "del"

# #calling len() on a dictionary will return the number of keys in the dictionary
# print(len(student))
# #Here it returns 7, which is the current number of keys
# # (as of the time of writing this document).

# #The .values() method returns all the values of the dictionary, in order, without keys.
# print(student.values())

# #The .items() method returns the entire contents of the dictionary formatted in individual tuples.
# print(student.items())

#This loop iterates through the contents of the dictionary and prints the keys and values
for key in student.items():
    print(key)
#Note using enumerate() will simply number the output, and that using the previous .values() method will only display the values.