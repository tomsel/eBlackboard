import urllib
from icalendar import Calendar, Event

def download_schedule(ROOM):
	if ROOM == 'EA':
		url = 'https://se.timeedit.net/web/chalmers/db1/public/ri667Q7QYo8ZQ4Q5c66Q3175yZZf50.ics'
	urllib.urlretrieve (url, "schema.ics")
	print('download finished')

def get_class():
	cal=Calendar("schema.ics")
			
download_schedule('EA')
get_class()
