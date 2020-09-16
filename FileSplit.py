#FulePlit.py    03.20.2020

#Program #3

print("Enter filename")
fileName = input()

#start with getting the file extension:
print("File extionsion is:")
print(fileName.split(".")[-1])

with open(fileName, "r") as targ:
    print("File contents:")
    print(targ.read())