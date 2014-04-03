import time
import os
import urllib
import pytz
from HTMLParser import HTMLParser
from icalendar import Calendar, Event
from datetime import date, datetime, timedelta

class MyHTMLParser(HTMLParser):
	savecourse=0
	savelink=0
	data=''
	def handle_starttag(self, tag, attrs):
		if tag=='a' and self.savelink==1:
			self.data=attrs[0][1]
			self.savelink=0
		if tag=='td' and self.savecourse==1:
			self.savecourse=2
		else:
			self.savecourse=0
	def handle_data(self,data):
		if self.savecourse==2:
			self.data=data
			self.savecourse=0
		if data=='Course':
			self.savelink=1 
		if data=='Course id':
			self.savecourse=1

def download_schedule(ROOM):
	if ROOM == 'EA':
		#Subscription link for room EA
		url = 'https://se.timeedit.net/web/chalmers/db1/public/ri667Q7QYo8ZQ4Q5c66Q3175yZZf50.ics'
	urllib.urlretrieve (url, "schema.ics")

def get_course(ROOM):
	currenttime = datetime.now(pytz.utc) #datetime(2014, 3, 17, 12, 30, 0, 0, pytz.utc)
	if time.time() - os.path.getmtime("schema.ics") > 1200:
		download_schedule(ROOM)
	filename = open('schema.ics','rb')
	cal = Calendar.from_ical(filename.read())
	for component in cal.walk():
		if component.name == "VEVENT":
			if component.get('dtstart').dt < currenttime and component.get('dtend').dt+timedelta(minutes=14) > currenttime: 
				ID = component.get('DESCRIPTION')
				splitted = ID.split(" ")
				return id_to_course(splitted[1], ROOM)
	
	return "no course"
	filename.close()
	
def id_to_course(ID, ROOM):
	if ROOM == 'EA':
		#Base link for EA, by modifying the objects ID we should be able to port this solution to other rooms
		url='https://se.timeedit.net/web/chalmers/db1/public/staticss.html?p=0.m%2C0.d&sid=3&objects=192402.186&ox=0&types=0&fe=0&fw=t&id='+str(ID)+'&fr=t&h=f&step=0'
	
	urllib.urlretrieve(url, 'page.html')
	parser = MyHTMLParser()
	filename = open('page.html', 'r')
	parser.feed(filename.read())
	url2=parser.data
	parser.close()
	
	urllib.urlretrieve('https://se.timeedit.net/web/chalmers/db1/public/'+url2, 'page2.html')
	parser = MyHTMLParser()
	filename = open('page2.html', 'r')
	parser.feed(filename.read())
	course=parser.data
	parser.close()
	
	return course
