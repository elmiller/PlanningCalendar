#!/usr/bin/python

import datetime, calendar, sys, re
from datetime import timedelta

# Create lists for each day
Monday = ['EH']
Tuesday = ['EH', 'HR']
Wednesday = ['EH']
Thursday = ['EH', 'HR']
Friday = ['EH']

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
if enteryear in range(2012,2051):
	thisyear = enteryear
else:
	print "Error: enter a year in the range 2012-2050."
	sys.exit()

# Validate input for month
if entermonth in range(1,13):
	thismonth = entermonth
else:
	print "Error: enter 1-12 for the month."
	sys.exit()

# Set calendar variables
now = datetime.datetime.now()

startdate = datetime.date(thisyear,thismonth,1)

# Find how many days are in the current month.
daysinmonth = calendar.monthrange(thisyear, thismonth)[1]

print startdate.strftime("%B %Y\n")

# Loop through the month and print date and subjects
for x in range(1,daysinmonth):
	eachday = startdate + datetime.timedelta(days=x)

	# Print "Week of..."
	if eachday.weekday() in range(1):
		weekline = eachday.strftime("Week of %A, %B %e, %Y\n")
		# Remove repeated spaces date is single digit number
		print re.sub(r"\s\s+", " ",weekline)

	# Include only weekdays
	if eachday.weekday() in range(0,5):
		dayline = eachday.strftime("%A, %B %e, %Y")
		# Remove repeated spaces date is single digit number
		print re.sub(r"\s\s+", " ",dayline)
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
