#Reverse names.py

#program #1

print("Please enter first name")
firstName = input()
print("Please enter last name")
lastName = input()

print("Your first and last name, swapped")
print(f"{lastName} {firstName}")
fullName = f"{firstName} {lastName}"
fullList = [i for i in fullName]
revList=""

for i in range(fullList.index(fullList[-1]), -1, -1):
    revList += fullList[i]


print("Your first and last name, backwards")
print(f"{revList}")