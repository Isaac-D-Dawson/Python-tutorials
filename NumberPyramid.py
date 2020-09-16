#NumberPyramid.py       04.02.2020

#Program 10

#make a list of numbers real quick:
numbers = [i for i in range(1, 10)]
#Quick test thing

#numbers = [i for i in range(1, 10)]
#numbers = "1,2,3,4,5,6,7,8".split()
#maye use the split trick for shorter strings, and rangers for anything with a double digit or greater?

#make the outer loop that cycles through everything in our list
for i in numbers:
    #set the out variable to be empty:
    out =""
    #make the inner loop that does it the [content] number of times.
    for j in range(1, i+1):
        out += str(i)
    #print output:
    print(out)