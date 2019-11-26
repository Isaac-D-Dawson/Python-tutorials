#Decorators.py 12.11.2019

#First class functions and closures will be used here. gp read up on them.

#First class functions: Allows functions to be treated like objects- as arguments in functions, returned from functions, assigned to variable.
#Closures return an inner function local to the scope in which they were created.

#Example:
def outer_func(msg):
    
    def inner_func():
        print(msg)
    return inner_func

hi_func = outer_func("Hi!")
lo_func = outer_func("Bye :(")
my_funcs = [hi_func, lo_func]
my_funcs[0]()
my_funcs[1]()

#See how the functions are useable as variables, and subsequently callable from them.
#Note that the inner function rembers the outerfunction even though it's closed?
#keep in mind these will be elaborated on more cearly in a seperate document.


#Decorator functions
def decorator_func(origin_func):

    def wrapper_func0(*args, **kwargs):
        print("Our eulogy for today...")
        return origin_func(*args, **kwargs)
    return wrapper_func0

def funcy_funk():
    print("Ashes to Ashes, and Funk to Funky...")

decorated_func = decorator_func(funcy_funk)

decorated_func()
#Adds contents 

@decorator_func
def display():
    print("We are gathered here today...")

display()
#Defining it with @decorator_func runs display through decorator whenever display is called.

@decorator_func
def display_info(name, age):
    print(f"Your name is {name} and you are {age} years old!")

display_info("John Eggbert", "14")

