#NumerWordConverter.py      12.02.2020

cont = "y"

#identifier codes for units
numSuffixes = "ero,one,two,ree,our,ive,six,seven,ght,ine,ten,leven,lve,hirteen,ourteen,fifteen,sixteen,seventeen,ghtteen,ineteen".split(",")
#identifier codes for tens
tenSuffixes = "wenty,irty,urty,fty,xty,venty,hty,ety".split(",")
#identifier codes for hundreds
hundredSuffixes = "one hundred,two hundred,ree hundred,our hundred,ive hundred,six hundred,seven hundred,ght hundred,ine hundred,one thousand".split(",")
#identifier codes for thousands
thousandSuffixes = "one thousand,two thousand,ree thousand,our thousand,ive thousand,six thousand,seven thousand,ght thousand,ine thousand,ten thousand".split(",")
#identifier codes for ten thousands
tenThousandSuffixes ="wenty thousand,irty thousand,urty thousand,fty thousand,xty thousand,venty thousand,hty thousand,ety thousand".split(",")
#identifier codes for Hundred thousands
hundredThousandSuffixes = "one hundred thousand,two hundred thousand,ree hundred thousand,our hundred thousand,ive hundred thousand,six hundred thousand,seven hundred thousand,ght hundred thousand,ine hundred thousand,one million".split(",")

units = "one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen".split(",")
tens = "ten,twenty,thirty,fourty,fifty,sixty,seventy,eighty,ninety".split(",")

while cont[0] != "n":
    #get user input
    if cont[0] not in "n" and cont != "":
        ourIn = input().lower()
    else:
        ourIn = cont
    
    inType = ""

    for i in ourIn:
        if i in "0123456789":
            #print("number")
            pass
        else:
            inType = "word"
            #print("word")

    ourNum = ourIn
    if inType == "word":
        
        output = 0
        #As long as the inout is more than nothing.
        while len(ourNum) > 0:
            #if the last few charachters are in one of the suffixes...
            for i in range(numSuffixes.index(numSuffixes[-1]), -1, -1):
                if ourNum[-(len(numSuffixes[i])):] == numSuffixes[i]:
                    #write it to the output...
                    output += i
                    #and trim the matched chars off.
                    ourNum = ourNum.rstrip(numSuffixes[i])

            for i in range(tenSuffixes.index(tenSuffixes[-1]), -1, -1):
                if ourNum[-(len(tenSuffixes[i])):] == tenSuffixes[i]:
                    output += (i+2)*10
                    ourNum = ourNum.rstrip(tenSuffixes[i])

            for i in range(hundredSuffixes.index(hundredSuffixes[-1]), -1, -1):
                if ourNum[-(len(hundredSuffixes[i])):] == hundredSuffixes[i]:
                    output += (i+2)*100
                    ourNum = ourNum.rstrip(hundredSuffixes[i])

            for i in range(thousandSuffixes.index(thousandSuffixes[-1]), -1, -1):
                if ourNum[-(len(thousandSuffixes[i])):] == thousandSuffixes[i]:
                    output += (i+1)*1000
                    ourNum = ourNum.rstrip(thousandSuffixes[i])

            for i in range(tenThousandSuffixes.index(tenThousandSuffixes[-1]), -1, -1):
                if ourNum[-(len(tenThousandSuffixes[i])):] == tenThousandSuffixes[i]:
                    output += (i+2)*10000
                    ourNum = ourNum.rstrip(tenThousandSuffixes[i])

            for i in range(hundredThousandSuffixes.index(hundredThousandSuffixes[-1]), -1, -1):
                if ourNum[-(len(hundredThousandSuffixes[i])):] == hundredThousandSuffixes[i]:
                    output += (i+1)*100000
                    ourNum = ourNum.rstrip(hundredThousandSuffixes[i])

            #if the input exists...
            if len(ourNum) > 0:
                #pull off the last character
                ourNum = ourNum.rstrip(ourNum[-1])
            
            print(output)
    else:
        #main program loop

        #reset the output and iterator
        output = ""
        iterate = -1
        
        #get user input
        ourNum = int(ourIn)
        
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
                output += f"{units[iterate]}-thousand "
                iterate = -1
            #I might re-do this upper section later by merging the units and the teens? but the
            # first goal is to make it work at all.
            # EDIT, V 1.1: Did Exactly That.

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

        #Trying some different logic here
        if ourNum in range(11, 20):
            output += f"{units[ourNum-1]}"
            ourNum = 0

        #More than 10
        while ourNum >= 10:
            #sub off
            ourNum -= 10
            #Add one
            iterate += 1
        #return output
        if iterate > -1:
            output += f"{tens[iterate]} "
            iterate = -1

            #Did run into issue where 

        #Trying some different logic here
        if ourNum in range(1, 11):
            output += f"{units[ourNum-1]}"
            ourNum = 0

        #return output without any extra whitespace or "and"s we might have tacked on somewhere.
        print(output)#.lstrip( "and "))
    cont = input("Do you wish to continue?(y/n)").lower()+"y"