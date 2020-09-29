#NumberToWord.py        11.02.2020


#initialise local variables:
units = "one,two,three,four,five,six,seven,eight,nine,ten".split(",")
teenagers = "ten,eleven,twelve,thriteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen".split(",")
tens = "twenty,thirty,fourty,fifty,sixty,seventy,eighty,ninety".split(",")

#confirm repeat var:
cont = "y"
#Allocate ouput and iterator memory:
output = ""
#since lists start at zero, make the smallest amount possible -1
iterate = -1

while cont == "y":
    #main program loop

    #reset the output and iterator
    output = ""
    iterate = -1
    
    #get user input
    ourNum = int(input())
    
    #Check if we've entered "0". We could do this last, but this minimizes breaks:
    if ourNum == 0:
        output = "zero"

    #Start with millions:
    #As long as we have more than a million
    while ourNum >= 1000000:
        #Sub off a million...
        ourNum -= 1000000
        #And add one to our iterator
        iterate += 1
    #Then return an output:
    #if iterate is still -1, then the above loop didn't run, and we don't need to print the result
    if iterate > -1:
        output += f"{units[iterate]} million "
        #Set iterate backt ot he default so it doesn't trip the next set
        iterate = -1
    

    #Repeat for Thousands:
    #As long as we have more than a hundred thousand
    while ourNum >= 100000:
        #Sub off a hundred-thousand...
        ourNum -= 100000
        #And add one to our iterator
        iterate += 1
    #Then return an output:
    if iterate > -1:
        output += f"{units[iterate]} hundred-thousand "
        iterate = -1

    #more than twenty-thousand
    while ourNum >= 20000:
        #Sub off...
        ourNum -= 20000
        #Add one
        iterate += 1
    #Return output:
    if iterate > -1:
        #use the tens list here, as we're dealing with, well ten thousand.
        #Quickly strip off any thousands the earlier code tacked on
        output = output.rstrip("-thousand ")
        output += f"{tens[iterate]}-thousand "
        iterate = -1
        #We stopped at twenty thousand here because this is the first time we had to deal with teens.
    
    #more than ten-thousand
    if ourNum > 10000:
        while ourNum >= 1000:
            #Only sub off a single thousand this time
            ourNum -= 1000
            #Add one
            iterate += 1
        #Return output:
        if iterate > -1:
            #use the teenagers list here, as we're dealing with, well nineteen to ten thousand.
            #Quickly strip off any thousands the earlier code tacked on
            output = output.rstrip("-thousand ")
            #subtract off nine to make sure we aren't trying to call the eighteenth slot rather
            # than the eighth, for example.
            output += f"{teenagers[iterate-9]}-thousand "
            iterate = -1
        #I might re-do this upper section later by merging the units and the teens? but the
        # first goal is to make it work at all.

    #More than a thousand
    while ourNum >= 1000:
        #sub off
        ourNum -= 1000
        #Add one
        iterate +=1
    #return output
    if iterate > -1:
        #Back to the units list
        #Quickly strip off any thousands the earlier code tacked on
        output = output.rstrip("-thousand ")
        output += f"{units[iterate]}-thousand "
        iterate = -1

    #More than a hundred
    while ourNum >= 100:
        #sub off
        ourNum -= 100
        #Add one
        iterate +=1
    #return output
    if iterate > -1:
        #Back to the units list
        #Quickly strip off any thousands the earlier code tacked on
        output += f"{units[iterate]}-hundred "
        iterate = -1

    #More than twenty
    while ourNum >= 20:
        #sub off
        ourNum -= 10
        #Add one
        iterate +=1
    #return output
    if iterate > -1:
        output += f"and {tens[iterate]}"
        iterate = -1
    
    #More than ten
    if ourNum >= 10 and ourNum < 20:
        while ourNum >= 0:
            #sub off
            ourNum -= 1
            #Add one
            iterate +=1
        #return output
        if iterate > -1:
            output += f" and {teenagers[iterate-9]}"
            iterate = -1

        #At this point I hit a snag, and had to re-do some of the earlier logic.
        #I copied this document, and titled it "V1.1"

    #return output without any extra whitespace or "and"s we might have tacked on somewhere.
    print(output.lstrip( "and "))
    cont = (input("do you wish to continue?(y/n):").lower()+"n")[0]