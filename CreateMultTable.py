#CreateMultTable.py

#Program 11

#set up inputs:
print("Enter the number for the table you wish to make:")
number = int(input())

#Cycle through 1-12...
for i in range(1, 13):
    #...and print the table for i times our number.
    print(f"{number} x {i} = {number * i}")
