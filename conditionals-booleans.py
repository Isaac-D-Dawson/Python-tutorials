#Conditionals and Booleans, 05.11.2019

#the if statement can be used to control the flow of code. 
# it allows you to decide if a section of code should be run, based on a conditional.
#the conditional will return a Boolean value, either TRUE or FALSE.
#If the statment is true, the code will be run.
#if the statement is false, it wont.
# the code that is run is indicated using whitepace. EG:
if False:
    print("This statement is: False!")
print("Don't think about it "*4)
#Note that the indented code did not run because the statement evaluated to False.
#However, the code undreneath still ran.

#Comparison operators.
# ==    equal to
# !=    not equal
# >     greater than
# <     less than
# >=    greater than or equal to
# <=    less than or equal to
# is    onject identity
# Is handles


#else allows for finer descision making, letting you decide
# which of two or more sections of code should be run. EG:
records = True
if records == False:
    print("False, I'll go false")
else:
    print("True, I'll go true")
print("I'll admit, I did cheat. I've heard that one before.")
#In this exampple, the bottom section of code is run, while the top is ignored.
#all code after the statement is still run.
#note the the Else has a common baseline with the If.
# this is how python handles blocks, and should be stuck to to avoid errors.

# The elif statement allows you to directly include an if statement in an else statement, without having to nest many if's inside eachother.
gel_type = "None"
if gel_type == "Bouncy":
    print("Repulsion Gel")
elif gel_type == "Slipery":
    print("Propulsion Gel")
else:
    print("Conversion Gel")
#Note that you can still use conventional else statements with
# elifs, and that they behave as expected.
#Also note that the else will run it's code regardless of the input.

# Boolean Operators:
# and   if both inputs are true, return true
# or    if either input is true, return true
# not   if input is false, return true.

#The and operator requires both inputs to be true.
employee = True
still_alive = True
if employee == True and still_alive == True:
    print("Continue testing")
#Here, "continue testing" is printed, as both variables are equal to true.

#The or operator returns true if either statement is true
astronaut = False
olympian = True
if astronaut == True or olympian == True:
    print("with you're help we're going to change the world!")
#Here the string is returned becasue one of the values, olympian, is true.

#The not operator inverts the current output.
employee = False
if not employee:
    print("Welcome, and Remember: Testing is the future!")
#Here, employee is false, but the code still runs.
# if the value was true, this code would NOT have run.

#is checks object identity, and thus if the two objects are the same in memory.
carolyn = ["Employee", "537"]
glados = ["Employee", "537"]
print(id(carolyn))
print(id(glados))
print(carolyn == glados) #Returns true, they are equal.
print(carolyn is glados) #returns false, they are not the same
print(carolyn is carolyn) # returns true, They are the same.
print(id(carolyn)) # returns the memory id of this variable
print(id(glados))  # returns the memory id of this variable

#Note that "is" can behave oddly depending on how pytohon optimises the data. EG:
# Floats, integers, and strings are internally optimised,
# and thus two identical variables will return the same ID".
#is effectively compares the IDs. eg:
# print(carolyn is glados)
#is the same as
#print(id(carolyn) ==  is(glados))
# but is easier to type.

