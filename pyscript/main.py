################
# E-Blackboard #
################

#Start off by importing a bunch of libraries that we need
import subprocess
import signal
import time
import os
import sys
import RPi.GPIO as GPIO
import datetime
from ftpupload import upload #now sftp
from mysqlcon import insertdata
from metadata import get_course
from cropmain import *

#Configure GPIO pins on the Raspbery
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)		#Left Front
GPIO.setup(17, GPIO.IN)		#Left Back
GPIO.setup(22, GPIO.IN)		#Right Front
GPIO.setup(27, GPIO.IN)		#Right Back

GPIO.setup(9, GPIO.OUT)		#Gren Diode
GPIO.setup(10, GPIO.OUT)	#Red Diode

GPIO.setup(18, GPIO.OUT)	#Pulsemodulator for the servo

#Spawning a subprocess which sets up portforwarding on port 3306 for our database connection
tunnel=subprocess.Popen("python2.7 tunnel.py", shell=True, preexec_fn=os.setsid) 

#Set up some static information for easier handlig
imgpath='/eblackboard.se/public_html/img/'

#This is used when there's no lecture held in EA:
#[course_code, course_name]=["wrk011", "working 22 april"]

#These three lines will upload the device's IP address to our webserver
os.system("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d ':' -f2 | cut -d ' ' -f1 >> IP.txt")
upload('/eblackboard.se/','public_html','IP.txt')
os.system("rm IP.txt")

#The trigger function. 
#When ran it will check for activity on the GPIO pins and if there's activity it will return the pin number in question. 
#It also controls the servo and lights a diode.
def trigger():
	ret=0
	if GPIO.input(4) == False:	
		ret=4
		GPIO.output(10, True)
		for x in range (0, 7):
			GPIO.output(18, True)
			time.sleep(0.009)
			GPIO.output(18, False)
			time.sleep(1)
	
	if GPIO.input(17) == False:
		ret=17
		GPIO.output(10, True)
		for x in range (0, 7):
			GPIO.output(18, True)
			time.sleep(0.009)
			GPIO.output(18, False)
			time.sleep(0.5)
	
	if GPIO.input(22) == False:
		ret=22
		GPIO.output(10, True)
		for x in range (0, 7):
			GPIO.output(18, True)
			time.sleep(0.0019)
			GPIO.output(18, False)
			time.sleep(0.5)
	
	if GPIO.input(27) == False:
		ret=27
		GPIO.output(10, True)
		for x in range (0, 7):
			GPIO.output(18, True)
			time.sleep(0.0019)
			GPIO.output(18, False)
			time.sleep(0.5)
	if ret!=0:
		time.sleep(2)
		GPIO.output(9, True)
		print ret
	return ret

	
#This is the actual main part of the program.
#It is basically an infinite loop. If an exception is thrown we catch it and exit the program properly.
try:
	while True:
		poll=trigger()		#Polling the trigger function to check the pins
		if poll!=0:			#If there is activity:
			#Set a bunch of variables
			[course_code, course_name]=get_course("EA")
			if course_code != "none":
				datestamp = datetime.date.today().isoformat()
				timestamp = time.strftime("%H:%M:%S", time.gmtime())
				filename=datestamp+'.'+timestamp+'.jpg'
				os.system('raspistill -o '+filename)	#Tell the camera module to take a picture
			
				#Check which sensor was triggered and crop the picture accordingly
				if(poll==4 or poll==22):
					cropping_fram(filename, 0)
				elif(poll==17 or poll==27):
					cropping_bak(filename, 0)

				#Upload the picture to the server and remove the picture file. Also insert the data in our database table.
				upload(imgpath,course_code,filename)
				os.system("rm "+filename)
				insertdata('../img/'+course_code+'/'+filename, datestamp, course_code, course_name)
			
				#Turn off the diodes
				GPIO.output(10, False)
				time.sleep(3)
				GPIO.output(9, False)

#If the user presses 'Ctrl+C'
except KeyboardInterrupt:
	os.killpg(tunnel.pid, signal.SIGTERM) #Kill the subprocess we spawned
	GPIO.cleanup() #cleanup on all GPIO channels
	print("Process terminated")
	sys.exit(0)
	
#If the program throws a different exception
except:
	os.killpg(tunnel.pid, signal.SIGTERM) #Kill the subprocess we spawned
	GPIO.cleanup() #cleanup on all GPIO channels
    print "Unexpected error: ", sys.exc_info()[0]
    
