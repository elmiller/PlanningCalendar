#!/usr/bin/python

import datetime
from datetime import timedelta
import sys

# Test if arguments were set at the command line
if len(sys.argv) > 2:
	enteryear = int(sys.argv[1])
	entermonth = int(sys.argv[2])

# If no arguments, read input with prompt
else:
	# Get user input for year
	enteryear = input("Enter year (yyyy): ")
	# Get user input for month
	entermonth = input("Enter month number (mm): ")

# Validate input for year
if enteryear in range(2012,2021):
	thisyear = enteryear
else:
	print "Error: enter a year in the range 2012-2020."
	sys.exit()

# Validate input for month
if entermonth in range(1,13):
	thismonth = entermonth
else:
	print "Error: enter 1-12 for the month."
	sys.exit()

# Set calendar variables
now = datetime.datetime.now()

startday = 1
startdate = datetime.date(thisyear,thismonth,startday)

# Loop through the month and print date and subjects
for x in range(0,31):
	eachday = startdate + datetime.timedelta(days=x)
	# Include only weekdays
	if eachday.weekday() in range(0,5):
		print eachday.strftime("%A, %B %d, %Y")
		print "LA"
		print "EH\n"
