#NumberDifferent.py     04.02.2020

#Program 2

#Generate our list of numbers:
print("Enter a list of numbers:")
ourNumbersList = input().split(",")
#make a comparison set
ourNumbersSet = set()

#copy everything into the set
for i in ourNumbersList:
    ourNumbersSet.add(i)

#Main program logic:
#if the list is the same length as the set, they are no duplicates, as sets remove all duplicates.
if len(ourNumbersList) == len(ourNumbersSet):
    print("There are no duplicates in this list")
else:
    print("There are duplicates in thlis list")
