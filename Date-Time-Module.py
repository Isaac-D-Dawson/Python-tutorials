#Date-Time-Module.py    04.12.2019

import datetime #Imports internal module, enabling the datetime object and attached methods.
import pytz     #Import PythonTimeZone package.

# print(datetime.date(2002, 1, 18))
# #Takes in a year, month, and day, and arranges them in a nice format.
# # note that it does not like railing zeroes.
# print(datetime.date.today())
# tday = datetime.date.today()
# print(tday.day)     #formatting to only show day.
# print(tday.month)   #formatting to only show month.
# print(tday.year)    #formatting to only show year.
# #Keep in mind that these method calls only work when used with a closure.

# print(tday.weekday())   #returns the number of which day it is, assining monday at 0
# print(tday.isoweekday())#returns the number of which day it is, assining monday at 1
# #".isoweekday()" is designed to be more readable by humans. keep this in mind when using these.

# tDelta = datetime.timedelta(days=-7)
# tDelta2 = datetime.timedelta(days=2, hours=6, minutes=25)
# print(tDelta+tDelta2)
# #".timedelta()" allows you to generate time formats and get the sum or difference.

# #time delta's can also be used on other date formats, such as ".today".
# print(tday - tDelta)    #show the date 7 days ago
# print(tday + tDelta)    #show the date 7 days from now
# #Operating on a date with a time delta returns another date.
# #Operating on a date with another date returns a time delta.
# #A time delta is effectively a differnce in time. this means while you can't have 

# #test code to get days till birthday
# mbday = datetime.date(2020, 1, 18)
# tbday = mbday - tday
# print(tbday.total_seconds())

# #how old am I?
# age = tday- datetime.date(2002, 1, 18)
# print(age)                  #in days
# print(age.total_seconds())  #in seconds

# t = datetime.time(1, 15, 25, 10005) #creates a niceformatted time.
# print(t)
# dt = datetime.datetime(2018, 12, 4, 15, 2, 30, 252356)
# print(dt) #".datetime()"s are also compatible with ".timedelta" operations.

# print(datetime.datetime.today())    #Returns current date and time, doesn't take arguments
# print(datetime.datetime.now())      #returns current date and time, takes in in PyTZ KWargs
# print(datetime.datetime.utcnow())   #Reutrns a Timezone Sensitive date and time, accepts PyTZ KWargs

# print(datetime.date.today().day)
# print(type(datetime))

#continued 1-/12.2019

#Using pytz package from here on in, installed at start of doc.

print(datetime.datetime(2002, 1, 18, 3, 8, 30))                     #returns a timzone naive date/time
print(datetime.datetime(2002, 1, 18, 3, 8, 30, tzinfo=pytz.UTC))    #uses UTC date/time

print(datetime.datetime.now())                              #returns a timzone naive date/time
print(datetime.datetime.utcnow().replace(tzinfo=pytz.UTC))   #also uses UTC date/time, but is horrible.

print(datetime.datetime.now(tz=pytz.timezone("US/Mountain")))               #uses US Mountain date/time
print(datetime.datetime.utcnow().astimezone(pytz.timezone("US/Mountain")))  #uses US Mountain date/time, but god no

print([x for x in pytz.all_timezones]) #List comprehension tha treturns all the pytz timezones.

#Explanation of this nonsense
#Print(Define timezone("Continent/timezone")."is the timezone that the following should use("datetime module"."datetime class"."time right now"()))
print(pytz.timezone('Pacific/Auckland').localize(datetime.datetime.now()))
#Please, never ever use code like this. Avoid naive timezones wherever possible.

print(datetime.datetime.now())
print(datetime.datetime.now().isoformat())
#Returns the current time in ISO format.
