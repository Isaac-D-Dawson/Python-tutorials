
#Help sought from stackoverflow, page https://stackoverflow.com/a/4326729 , Highest voted answer to "How to index a dictionary"
#messgae aquired from http://www.pythonchallenge.com/pc/def/map.html

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
message = "def/map"

alphabetOrig = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
alphabetShift = {" ":" ", ".":".", "'":"'", "(":"(", ")":")", "/":"/", "?":"?"}
for i in alphabetOrig:
    alphabetShift[i] = alphabetOrig[alphabetOrig.index(i)-2]
alphabetShifted = {}
for i in alphabetShift:
    alphabetShifted[alphabetShift[i]] = i

print("the alphabet used by the cipher, Value to key.")
print(alphabetShift)
print("The corrected alphabet.")
print(alphabetShifted)

output = ""

print("Decoding the message")
for i in message:
    #output.append(alphabetShifted[i])
    output = output + alphabetShifted[i]

print(str(output))

#or just use string.maketrans(), but I don't understand how that one works?

# stringA = "koe"
# stringB = "mqg"
# stringCheese = "everybody thinks twice before solving this. that's a handy little function. isn't it?"
# print(stringCheese.translate(stringCheese.maketrans(alphabetShifted)))

# print(message.translate(alphabetShifted))