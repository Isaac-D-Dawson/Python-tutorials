#numbers

#arithmatic operators in python are
# + add
# - subtract
# * multiply
# / divide
# // divide and round to nearest whole number
# % modulo, get the remainder of two numbers.
# ** tot e power of (Can also be used to root numbers)


#python handles numbers in two ways
#integers: which are whole numbers
aInteger = 3
#floats: which are decimals or fractions
aFloat = 3.14
#Python will automatically determine whether
# a number is an integer or a float and will
# save the type of variable accordingly.

#using a = sign followed by an arithamtic operator will
# perform the operation and then overwrite the variable with the new calue
num = 1
num =+ 1
#This is handy for incrementing variables, or
# performing a large number of repetative changes

#the abs() function removes the sign from infront of a number
# (Makes negatives positive and positives remain positive)
num = -5
print(abs(num))
#note that you can also force a number to be negative by adding a - to the result.

#the round() function rounds it's input. giving it an input tells is where to round to.
num = 3.14159
print(round(num))
print(round(num, 2))
#note that by default round() will round off everything after the point.

#Comparison operations return a true or false(A boolean) depending on their output
#Pythons comparison operators are
# < less than
# > greater than
# == equal to
# <= less than or equal to
# >= greater than or equal to
# != Not equal to

#keep in mind that numerical operators will not handle strings.
num = "35"
#is a string.
num = int(num)
#converts that string into an integer. always
# convert inputs to te right type when they enter the program.
#the term for this in python is "Casting".