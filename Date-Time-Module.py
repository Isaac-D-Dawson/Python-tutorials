#Date-Time-Module.py    04.12.2019

import datetime #Imports internal module, enabling the datetime object and attached methods.

print(datetime.date(2002, 1, 18))
#Takes in a year, month, and day, and arranges them in a nice format.
# not that it does not like railing zeroes.
print(datetime.date.today())
tday = datetime.date.today()
print(tday.day)     #formatting to only show day.
print(tday.month)   #formatting to only show month.
print(tday.year)    #formatting to only show year.
#Keep in mind that these method calls only work when used with a closure.

print(tday.weekday())   #returns the number of which day it is, assining monday at 0
print(tday.isoweekday())#returns the number of which day it is, assining monday at 1
#".isoweekday" is designed to be more readable by humans. keep this in mind when using these.

tDelta = datetime.timedelta(days=-7)
tDelta2 = datetime.timedelta(days=2, hours=6, minutes=25)
print(tDelta+tDelta2)
#".timedelta()" allows you to generate time formats and get the sum or difference.

#time delta's can also be used on other date formats, such as ".today".
print(tday - tDelta)    #show the date 7 days ago
print(tday + tDelta)    #show the date 7 days from now
#Operating on a date with a time delta returns another date.
#Operating on a date with another date returns a time delta.
#A time delta is effectively a differnce in time. this means while you can't have 

#test code to get days till birthday
mbday = datetime.date(2020, 1, 18)
tbday = mbday - tday
print(tbday.total_seconds())

#how old am I?
age = tday- datetime.date(2002, 1, 18)
print(age)                  #in days
print(age.total_seconds())  #in seconds

t = datetime.time(1, 15, 25, 10005) #creates a niceformatted time.
print(t)
dt = datetime.datetime(2018, 12, 4, 15, 2, 30, 252356)
print(dt) #".datetime()"s are also compatible with ".timedelta" operations.

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())