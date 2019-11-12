#Functions.py 11.11.2019

#functions are defined using the "def" keyword and the ":" symbol. EG:
def testfunction():
    print("Hello! I'm a test function!")
testfunction()
#Note that the function must end with (), even if it doesnt take arguments.
# The contents of the function will not be run until the function is called.
#Functions MUST be defined in order to work. if a function is called but not defined
# it will fail. There are exceptions to this under specific circumstances.
#Neglecting to include the brackets when a function is called simply returns
#  the functions name and memory location. This is useful for comparing functions by memory.
#Printing a function will display the content of a function

#The "pass" keyword is a way of specifying a blank function with no code.
def blank_func():
    pass
blank_func()
#This function won't do anything.
# If it did not contain the keyword "pass" the code would return an error.

#The return keyword allows the function output or "Return" a value to the program,
# rather than printing it to the terminal.
def hello_func():
    return "Hello World! it's nice to meet you today."

print(hello_func())
#Here print() prints the return value, rather than the contents of the function

#You can define internal variables for use in functions by placing them
# inside the brackets of the define call.
def multiply(a, b):
    return(a*b)

print(multiply(2, 4))
#Here the variables a and b store the inputs for the function. these are
# internal to the function, and can't be accessed from the outside.

#You can assing default placeholders to use if no input is provided for a
# function by setting the internal variable equal to the default value,
def func_greet(greeting, name="you"):
    return "{}, {}.".format(greeting, name)

print(func_greet("It's very nice to see you", "Isaac"))
print(func_greet("I hope you enjoy your stay"))
#Note that here the first string includes the given name, while
# the second string returns the default "you", rather than providing an error.
#it will prioritiese the inserted arguments over the defaults.
#Keep in mind, arguments with defaults should be places last, otherwsie the code will error.
# The term for a default argument is a "Keyword"

#Using a single or double asterisk specifies that the number of possible arguments is unknown.
# This allows you to pass in positional or kewrod values with know how many of each you'll need.
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

positional = ["dave", "strider"]
value_keywords = {"fees": "£350", "hand": "left"}
student_info(*positional, **value_keywords)
#If the astersisk(s) are also used in the actual inputs, it will unpack
# lists or dictionaries automatically.

#
def func_func():
    """this is a docstring"""
    pass

