#!/usr/bin/python

import datetime
from datetime import timedelta
import sys

# Create lists for each day
Monday = ['LA\n1. Update planners\n2. Journal entry\n3. Reading time', 'EH']
Tuesday = ['LA', 'EH']
Wednesday = ['HR: ', 'LA', 'EH']
Thursday = ['LA', 'EH']
Friday = ['LA', 'EH']

# Create function that loops through the lists and prints the teachers and events for the day.
def printSchedule(day):
    for event in day:
        print event
    # Include a blank line at the end of the day
    print

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
        # Sets value of theday to a day of the week (i.e. "Monday")
        theday = eachday.strftime("%A")
        if theday == "Monday":
            printSchedule(Monday)
        elif theday == "Tuesday":
            printSchedule(Tuesday)
        elif theday == "Wednesday":
            printSchedule(Wednesday)
        elif theday == "Thursday":
            printSchedule(Thursday)
        elif theday == "Friday":
            printSchedule(Friday)
