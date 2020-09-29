#wordToNumber.py        04.02.2020

#program 1 (Chux, start from zero like a normal robot!)

#Lets make a quick list of the words we're comparing to, matched to indexes.

#Catch all the followings, which jsut have the "teen" suffix)

#Hits the same issue as the previous ones....Hashmap?
#Yeah, Memoise'd hashmap.



#Lets quickly make one to handle all the odd exceptions.
#   Idea: Stick with the "index" theme.
#   Upside: General consistency and ease of access
#   Downside:I'd need to include some hundred odd blank spaces.
#   OR: I'd have to generate an absurdly large list on init.
#   Idea 2: Memoise this stuff.


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
#allocate memory for result
output = 0
#allocate continue value
cont = "y"
#allocate while iterator
iterate = 0
#set the archived output:
archOut = output

#outer while loop to keep the program running until the user requests a stop.
while cont == "y":
    #Input value
    ourNum = input().lower()
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
    #return the result and clear it for the next loop.
    print(output)
    output = 0
    #ask if we want to go again.
    cont = input("do you wish to continue(y/n):").lower()[0]