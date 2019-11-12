#Decorators.py 12.11.2019

#First class functions and closures will be used here. gp read up on them.

#First class functions: Allows functions to be treated like objects- as arguments in functions, returned from functions, assigned to variable.
#Closures return an inner function local to the scope in which they were created.

#Example:
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func("Hi!")
lo_func = outer_func("Bye :(")
my_funcs = [hi_func, lo_func]
my_funcs[0]()
my_funcs[1]()

#See how the functions are useable as variables, and subsequently callable from them.
#Note that the inner function rembers the outerfunction even though it's closed?
#keep in mind these will be elaborated on more cearly in as eperate document.



