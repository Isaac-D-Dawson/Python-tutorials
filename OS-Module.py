#OS-module.py   03.12.2019

import os
#Internal module that haandles python-Operating system interactions.

print(os.getcwd())
#Gets current directory.
os.chdir("C:/Users/New User/Documents")
print(os.getcwd())
#Note that it will not take certian shalshes unless it is apssed in as raw.
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

