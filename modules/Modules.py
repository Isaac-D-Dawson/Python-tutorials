#Modules.py   20.11.2019

#examples?

#import my_tools                                #imports everywthing in the module
#import my_tools, test                          #imports the module, but lets you set the name for it.
#from my_tools import find_index()              #imports only that one function from the module. beware dependancies.
#when importing, all code in the imported target is run, which both set sup defenitions, and provides "imported" text.
#from my_tools import find_index as fi, test    #imports the find_index function, but now uses fi to call function.
# The function is not called as a method of the module anymore.
import my_tools

shopping = ["milk", "Eggs", "Butter", "Bread"]

print(my_tools.find_index(shopping, "bautter"))
#If "my_tools" is redefined using the "as" keyword then it should be replaced here as well.
# If you replace the module name using as be consistent with it.

#The term modules is used to reffer to any file in python.
# Trying to import a file inside of another file is fine.
# trying to call a file inside of itself is a bad idea.
# Note that the import call ignores file extensions.

#Folders in python are called packages, and you can indicate to install modules from said packages.

print(my_tools.test)
