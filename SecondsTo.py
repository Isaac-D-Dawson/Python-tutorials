#SecondsTo.py       04.02.2020

#Program #9

#Ask for and ge thte int of seconds.
print("Please enter the number of seconds:")
seconds = int(input())
#initialise variables
minuites = 0
hours = 0
days = 0

#days:
while seconds >= (3600*24):
    seconds -= 3600*24
    days += 1
#hours:
while seconds >= 3600:
    seconds -= 3600
    hours += 1
#minuites:
while seconds >= 60:
    seconds -= 60
    minuites += 1

#return results:
print(f"{days} days, {hours} hours, {minuites} minuites, and {seconds}, seconds")