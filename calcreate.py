#!/usr/bin/python

#importing modules
import datetime
from datetime import timedelta
import sys

#get user input for month
entermonth = input("Enter month number: ")

#validate input
if entermonth in range(1,13):
	thismonth = entermonth
else:
	print "Error: enter 1-12."
	sys.exit()

#get user input for year
enteryear = input("Enter year: ")

#validate input
if enteryear in range(2012,2021):
	thisyear = enteryear
else:
	print "Error: enter 2012-2020."
	sys.exit()


#set calendar variables
now = datetime.datetime.now()
#thisyear = now.year
startday = 1
startdate = datetime.date(thisyear,thismonth,startday)

#loop through the month and print date and subjects
for x in range(0,31):
	eachday = startdate + datetime.timedelta(days=x)
	#include only weekdays
	if eachday.weekday() in range(0,5):
		print eachday.strftime("%A, %B %d, %Y")
		print "LA"
		print "EH\n"
