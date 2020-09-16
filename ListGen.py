#ListGenerator.py   03.02.2020

#Progrma #2

print("Please insert a string of values, seperated by commas")
ourList = input().split(",")
ourTuple = tuple([i for i in ourList])
print(ourList)
print(ourTuple)