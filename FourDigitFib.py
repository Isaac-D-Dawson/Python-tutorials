#FourDigitFib.py        04.02.2020

#Program 6

#generate environment variables
seq = [1,1,1,1]
print("enter the Nth term, Greater than four please:")
nTh = int(input())

#Make sure the input is more than four, otherwise we might as well jsut say "1"
if nTh <= 4:
    print("1")
else:
    #Set our starting value for the loop at the fourth number.
    i = 3
    #Count from the fourth number up to the request.
    while i <= nTh:
        #Stick the sum of the last four digits into the next slot.
        seq.append(seq[i-4]+seq[i-3]+seq[i-2]+seq[i-1])
        #incriment i, otherwise we never stop.
        i+=1
    #Print the result.
    print(seq[nTh])