import time
import os
import urllib
import pytz
from icalendar import Calendar, Event
from datetime import date, datetime, timedelta

#TODO: 
#figure out a good way to extract the program(s) associated with the course

def download_schedule(ROOM):
	if ROOM == 'EA':
		url = 'https://se.timeedit.net/web/chalmers/db1/public/ri667Q7QYo8ZQ4Q5c66Q3175yZZf50.ics'
	urllib.urlretrieve (url, "schema.ics")

def get_course(ROOM):
	metadata = []
	currenttime = datetime.now(pytz.utc) #datetime(2014, 3, 17, 12, 30, 0, 0, pytz.utc)
	if time.time() - os.path.getmtime("schema.ics") > 1200:
		download_schedule(ROOM)
	filename = open('schema.ics','rb')
	cal = Calendar.from_ical(filename.read())
	for component in cal.walk():
		if component.name == "VEVENT":
			if component.get('dtstart').dt < currenttime and component.get('dtend').dt+timedelta(minutes=14) > currenttime: 
				summary = component.get('summary')
				splitted = summary.split(",")
				if splitted[0]==ROOM:
					return "no course"
				else:
					return str(splitted[0])
	
	return "no course"
	filename.close()
