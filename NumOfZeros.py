#NumOfZeros.py      04.02.2020

#Program 5

#Storing the factorial as a string for now.
ourFact = "36288000"
#using factorial of ten as an example for now

#spin up a quickl loop to count back from the end.
i=-1
while ourFact[i] == "0":
    i-=1
#Print the result
print(abs(i+1))