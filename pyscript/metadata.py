import time
import os
import urllib
import pytz
from HTMLParser import HTMLParser
from icalendar import Calendar, Event
from datetime import date, datetime, timedelta

#no longer used
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

#no longer used
def get_course(ROOM):
	#currenttime = datetime.now(pytz.utc) 
	currenttime = datetime(2014, 4, 4, 9, 0, 0, 0, pytz.utc)
	if time.time() - os.path.getmtime("schema.ics") > 1200:
		download_schedule(ROOM)
	filename = open('schema.ics','rb')
	cal = Calendar.from_ical(filename.read())
	for component in cal.walk():
		if component.name == "VEVENT":
			if component.get('dtstart').dt < currenttime and component.get('dtend').dt+timedelta(minutes=14) > currenttime: 
				ID = component.get('DESCRIPTION').split("ID ")[1]
				name = str(component.get('SUMMARY').split(",")[0])
				if summary == ROOM:
					return "none"
				else:
					print ID
					return [id_to_course(ID, ROOM), str(component.get('summary').split(",")[0])]
	
	return "none"
	filename.close()

#no longer used	
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
	
def get_course2(ROOM):
	#currenttime = datetime.now(pytz.utc) 
	currenttime = datetime(2014, 4, 8, 9, 0, 0, 0, pytz.utc)
	if time.time() - os.path.getmtime("schema.ics") > 1200:
		download_schedule(ROOM)
	filename = open('schema.ics','rb')
	cal = Calendar.from_ical(filename.read())
	for component in cal.walk():
		if component.name == "VEVENT":
			if component.get('DTSTART').dt < currenttime and component.get('DTEND').dt+timedelta(minutes=14) > currenttime: 
				code = component.get('SUMMARY')
				name = component.get('DESCRIPTION').split('\n', 1)[0]
				if name == 'ID' or len(code)>8:
					return "none"
				else:
					return [code, name]
	
	return "none"
	filename.close()

