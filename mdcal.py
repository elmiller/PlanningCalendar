#!/usr/bin/python

import datetime
from datetime import timedelta
import sys

# Create lists for each day
Monday = ['LA\n\n1. Update planners\n2.\n', '\nEH']
Tuesday = ['LA', '\nEH', '\nHR']
Wednesday = ['LA', '\nEH']
Thursday = ['LA', '\nEH', '\nHR']
Friday = ['LA\n\n1. Reading Log Reflection\n2.\n', '\nEH']

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

# Print Monday as heading

print now.strftime("# %B %Y\n")

# Loop through the month and print date and subjects
for x in range(0,31):
	eachday = startdate + datetime.timedelta(days=x)
	
	# Print "Week of..."
	if eachday.weekday() in range(1):
		print eachday.strftime("## Week of %A, %B %d, %Y\n")

	# Include only weekdays
	if eachday.weekday() in range(0,5):
		print eachday.strftime("%A, %B %d, %Y\n")
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
            print "<br><hr><br>"