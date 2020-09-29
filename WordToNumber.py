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

ourNum = input().lower()
ourWord = ""
numPrefixes = "zer,one,two,thr,fou,fiv,six,sev,eig,nin,ten,ele,twe,thi,null,fif".split(",")
teenSuffix = "rteen"
tensSuffix = "ty"
#do some operations to "ourNum" to get the extra charachters out
# ourNum = ourNum.split(",")
# for i in ourNum:
#     for c in i:
#         ourWord += c
# ourNum = ourWord
# ourWord = ""
# ourNum = ourNum.split("-")
# for i in ourNum:
#     for c in i:
#         ourWord += c
# ourNum = ourWord.split(" ")
# print(ourNum)
#COME BACK TO THIS INNA BIT K?

print(ourNum)
print(numPrefixes)
print(teenSuffix)

if ourNum[0:3] == numPrefixes[0]:
    print("0")
if ourNum[0:3] == numPrefixes[1]:
    print("1")
if ourNum[0:3] == numPrefixes[2]:
    print("2")
if ourNum[0:3] == numPrefixes[3]:
    print("3")
if ourNum[0:3] == numPrefixes[4]:
    if ourNum[-5:] == teenSuffix:
        print("14")
    else:
        if ourNum[-2:] == tensSuffix:
            print("40")
        else:
            print("4")

if ourNum[0:3] == numPrefixes[5]:
    if ourNum[-5:] == teenSuffix:
        print("15")
    else:
        if ourNum[-2:] == tensSuffix:
            print("50")
        else:
            print("5")

if ourNum[0:3] == numPrefixes[6]:
    if ourNum[-5:] == teenSuffix:
        print("16")
    else:
        if ourNum[-2:] == tensSuffix:
            print("60")
        else:
            print("6")

if ourNum[0:3] == numPrefixes[7]:
    if ourNum[-5:] == teenSuffix:
        print("17")
    else:
        if ourNum[-2:] == tensSuffix:
            print("70")
        else:
            print("7")

if ourNum[0:3] == numPrefixes[8]:
    if ourNum[-5:] == teenSuffix:
        print("18")
    else:
        if ourNum[-2:] == tensSuffix:
            print("80")
        else:
            print("8")

if ourNum[0:3] == numPrefixes[9]:
    if ourNum[-5:] == teenSuffix:
        print("19")
    else:
        if ourNum[-2:] == tensSuffix:
            print("90")
        else:
            print("9")

if ourNum[0:3] == numPrefixes[10]:
    print("10")
if ourNum[0:3] == numPrefixes[11]:
    print("11")
if ourNum[0:3] == numPrefixes[12]:
    if ourNum[-5:] == teenSuffix:
        print("12")
    else:
        print("20")

if ourNum[0:3] == numPrefixes[13]:
    if ourNum[-5:] == teenSuffix:
        print("13")
    else:
        print("30")

if ourNum[0:3] == numPrefixes[15]:
    if ourNum[-5:] == teenSuffix:
        print("15")
    else:
        print("50")



print(ourNum[-5:])