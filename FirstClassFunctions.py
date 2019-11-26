#First Class functions  18.11.2019

#First class functions are instances where functions are treated as objects. They can be
# stored in variables, passed to other functions, and generally treated like any other object.
#A higher order function is a function that can accept or return other functions.
#example:
def square(x):
    return x*x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100])
print(squares)

#Example
def html_tag(tag):
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")
        #print("{0}{1}{2}".format(f"<{tag}>", f"{msg}", f"</{tag}>"))
    return wrap_text

print_h1 = html_tag("h1")
print_h1("test headline!")
print_h1("Followup Headline!")

print_p = html_tag("p")
print_p("The actual news story")
#This code generates a few functions, takes a few inputs, and wraps the text input with the provided tag.
# note we're storting variables in functions. this is reffered to as a closure, go read that dic,