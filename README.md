Planning Calendar
================

Python script to create a weekday, linear calendar for lesson planning.

## About

The idea for this script was born soon after my first child. After returning to work, I found myself trying to get my lesson planning done while holding my baby as he drifted off to sleep. I tried using a Google Calendar, but found the format too constraining to write out my ideas, so I started writing out my ideas in Evernote. I soon realized it would be helpful to have the dates listed out for me in advance, so I could plan ahead for the month.

Since I was working on my phone, I used [Pythonista](http://omz-software.com/pythonista/) to write out this script. I was new to Python at the time, but was able to get this script working within a few nights.

## Usage

Run the script from the command line with `plancal yyyy mm`. If you leave off the arguments, the script will ask for the month and year:  
`Enter year (yyyy): 2013`  
`Enter month number (mm): 9`

The script will then list the weekdays for the specified month in the following format:

May 2015

Week of Monday, May 4, 2015

Monday, May 4, 2015
LA  
EH  

Tuesday, May 5, 2015
LA  
EH  
HR  

Wednesday, May 6, 2015
LA  
EH  

Thursday, May 7, 2015
LA  
EH  
HR  

Friday, May 8, 2015
LA  
EH  
