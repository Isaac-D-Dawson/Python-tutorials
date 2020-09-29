#NumberToWord.py        11.02.2020

#CHANGELOG:
# V1.0:
# -Created basic program logic.
# BUGS:
# -Program was incapable of handling any number lower than twenty,
# V1.1:
# -Edited program logic:
# --Combined units and teenagers lists.
# --Revised teenager logic completely
# BUGS:
# -teenager problem now present with hundreds.
# V1.2:
# -Changed continue option to default to "Yes" instead of "No".
# -bugfixes
# V2.1:
# -Added memoiseation in preperation for program merge.
# BUGS:
# -Attempted to use a defenition system instead of several if statments. Results were inconclusive.
# ^consider patching next version. 

#initialise local variables:
units = "one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen".split(",")
tens = "ten,twenty,thirty,fourty,fifty,sixty,seventy,eighty,ninety".split(",")

#confirm repeat var:
cont = "y"
#Allocate I/O memory:
ourNum = 0
output = ""
#Create cache:
wtm_cache ={}

# #Create our test function?
# def numToWord(a, b):
#     global ourNum
#     global output
#     if ourNum in range(a, a*10):
#         output += f"{b[(ourNum//a)-1]} "
#         ourNum -= (ourNum//a)*a

while cont != "n":
    #main program loop

    #reset the output and iterator
    output = ""    
    #get user input
    ourNum = int(input())
    
    #Check if input is in cache
    if ourNum in wtm_cache:
        print(wtm_cache[ourNum])
    else:
        #Check if we've entered "0". We could do this last, but this minimizes breaks:
        if ourNum == 0:
            output = "zero"

        if ourNum in range(100, 1000):
            output += f"{units[(ourNum//100)-1]} "
            ourNum -= (ourNum//100)*100
            
        if output != "":
            output += "hundred "
            if ourNum > 0:
                output += "and "

        if ourNum in range(20, 100):
            output += f"{tens[(ourNum//10)-1]} "
            ourNum -= (ourNum//10)*10

        
        if ourNum in range(1, 20):
            output += f"{units[ourNum-1]}"
            ourNum = 0

        #cache our output
        wtm_cache[ourNum] = output

        #return output
        print(output)
        cont = (input("do you wish to continue?(y/n):").lower()+"y")[0]