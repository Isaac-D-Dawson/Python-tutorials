#timeDifference.py  03.02.2020

#program #4

#Grab packages
import datetime as dt
import pytz

#Get dates
print("Enter date one in (yyyy, mm, dd)")
date1 = input()
print("Enter date two in (yyyy, mm, dd)")
date2 = input()

#use split to get the values
date1list = date1.split(",")
date2list = date2.split(",")

#Create dates

date1time = dt.date(int(date1list[0]), int(date1list[1]), int(date1list[2]))
date2time = dt.date(int(date2list[0]), int(date2list[1]), int(date2list[2]))
print("difference is:")
print(date1time - date2time)