#Loops.py   05.11.2019

#A for loop is often used to iterate though things, as it performs until it's set conditions are true.
# This makes it useful for performing tasks a set number of times, or for performing a task on each coponent of a list.
#EG:
gells = ["Repulsive", "Propulsive", "Converting", "Adhesive", "Reflective", "Cleansing"]
for gel in gells:
    print(gel)

#The break keyword will stop a loop and run the code outside of it.
for gel in gells:
    if gel == "Adhesive":
        print("Wait, That Gel was cut!")
        break
    print(gel)

#the continue keyword will skip to the next iteration of a loop.
for gel in gells:
    if gel == "Adhesive":
        print("Wait, That Gel was deadly-er!")
        continue
    print(gel)

# #it is possible to nest loops inside eachother,
# rooms = [1, 2, 3, 4]
# for room in rooms:
#     for letter in "abcd":
#         print(room, letter)
# #Which will print out 1 a, 1 b, 1 c...4 d.

# #The range() function is really useful for setting a loop to run a number of times
# #EG:
# for i in range(1, 13):
#     k = 4
#     print(f"{i}x{k}={i*k}")
# # iterates from 1 to 12. Note that you don't
# # need a starting value, and the stopping value is not inclusive.

# The range function provides an internal list of values up till the stopping value.
# if a second value is provided, it will use the first value as a starting
# point and the second as a stop point.
# if a third value is added, it will go in intervals of the third value.
#EG:
for i in range(1, 11, 2):
    print(i)
#Prints every second number in the range 1-11, not including 11.
#Note that placing a larger start value than the stop value, or
# using a negative interval, will fail without an error.
#HOWEVER, using a larger start value than the stop value AND
# using a negative interval at the time time WILL work,
# Counting down from the start intervl to the end interval +1.

#While loops function while a condition is true. if the condition becomes false, they stop
#EG:
x = 1
while x <=10:
    print(x)
    x+=1
