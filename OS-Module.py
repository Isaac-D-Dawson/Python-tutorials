#OS-module.py   03.12.2019

import os
#Internal module that haandles python-Operating system interactions.

print(os.getcwd())
#Gets current "Working" directory.
os.chdir("C:/Users/New User/Documents")
print(os.getcwd())
#Note that it will not take certian slashes unless it is passed in as raw.
os.chdir(r"C:\Users\New User\Documents")
print(os.getcwd())

#print(os.listdir())
#print(os.listdir("C:/Users/New User/Documents/GitHub/Python-tutorials"))
##Lists files&folders in target dir, if no dir specified, taret current working dir.

#Same thing, ordered nicer.
for i in os.listdir():
    print(i)

for i in os.listdir("C:/Users/New User/Documents/GitHub/Python-tutorials"):
    print(i)

#os.mkdir("TestDir")
# #Makes a directory with the pased input at the current location
#os.makedirs("OtherTestDir/Nestedir")
# #creates several dirs to create the entered filepath.

#os.rmdir()
# #Removes target directory, or current directory if no target specified.
#os.removedirs()
# #deletes everything in the filepath.
# #I AM NOT TESTING THESE OKAY?

# os.rename()
# # renames files&folders in target directory. takes in the original file name and the new filename.

# print(os.stat("Hi.txt"))
# #Returns data from a file. accepts .attribute modifiers.

# os.walk()
# #Returns a tuple of the directory its in, all subdirectories, and all files. traverses a set filepath.
# #useful for searching directories.

# os.environ()
# #Returns all envrionment variables.

# os.path.join()
# #Joins two filespaths seamlessly, without a missing or duplicated /

# os.path.basename()
# #Returns the base file-name from a path.
# os.path.dirname()
# #returns the path, without the base name.
# os.path.split()
# # returns the base name and the path seperately.
# os.pathexists()
# #Returns True or False depending on whether the path exists or not.
# os.path.isdir()
# #returns true if target is a dir.
# os.path.isfile()
# #returns true if target is a file.
# os.path.splitext()
# #Spits the path and the file the file, and the file extension.
