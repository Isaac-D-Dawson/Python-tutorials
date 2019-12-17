#File-Handling.py   16.12.2019

# #this way isn't recomended
# myFile = open("TestFile.txt", "r")
# print(myFile.name)
# myFile.close()  #make sure to explicitely close files when you're done using them.

# #a better way to do this is to use a context manager.
# with open("TestFile.txt", "r") as myFile:
#     print(myFile.name)
#     print(myFile.read())
#     #Using a context manager auto-closes when you exit the indented block or 
#     # when it returns an error.
# #since the file closed when we left the indent...
# print(myFile.closed)
# #...Returns True, because the file is closed.

#Opening a new context manager for the rest of our code
with open("TestFile.txt", "r") as myFile:
    #print(myFile.name)         #gets the file name
    #print(myFile.read())       #reads from the file
    #print(myFile.readline())   #reads only the current line(And cylces to the next)
    #print(myFile.readlines())  #returns all remaining lines as a list
    pass

# #Test code to test loops inside context managers.
# with open("TestFile.txt", "r") as myFile:
#     for line in myFile.readlines():
#         print(line, end="") #"end=''" is to remove the additional newlines.

# #Same as above, but nicer on the environment
# with open("TestFile.txt", "r") as myFile:
#     for line in myFile:
#         print(line, end="")
# Use this one, if needed/possible!

#continued 17.12.2019

    # print(myFile.read())#Returns an empty streing, as we've reached the end of the file.
#the ".read()" method takes in an arument of how many characters to read at a time.
# it is also smart enoug to pick up where it left off from

# with open("TestFile.txt", "r") as myFile:
#     readSize = 50
#     fileContents = myFile.read(readSize)

#     while len(fileContents) > 0:
#         print(fileContents, end="*\n")
#         fileContents =  myFile.read(readSize)
#         print(myFile.tell())

# print("hello", end="")
# print("world", end="")

with open("TestFile.txt", "r") as myFile:
    # print(myFile.read(10))
    # print(myFile.read(10))
    # myFile.seek(15)
    # print(myFile.tell())
    # print(myFile.read(10))
    # print(myFile.read())
    # print(myFile.read())
    # myFile.seek(0)
    # print(myFile.read())
    pass

#The ".tell()" method returns the current characther position of the document.
# This is useful for working out where you are.
#The ".seek()" method does the oposite. It takes a character position and navigates to it.
# keep in mind that it only works in absolute, not relative.

# with open("TestFile2.txt", "r+") as myFile:
    # myFile.read()
    # lastChar = myFile.tell()
    # myFile.seek(lastChar)
    # myFile.write(" Or Will they?!")

with open("TestFile.txt", "r") as readFrom:
    with open("TestFile2.txt", "w") as writeTo:
        writeTo.write(readFrom.read())
#Nesting of "with open()" statments is allowed. While they can be elft on a single line
# Keeping them seperate can be more readable.

with open("BakedBean2019Card.jpg", "rb") as readFrom:
    with open("BakedBean2020Card.jpg", "wb") as writeTo:
        chunkSize = 4096
        chunkData = readFrom.read(chunkSize)
        while len(chunkData) > 0:
            writeTo.write(chunkData)
            chunkData = readFrom.read(chunkSize)
        
