################
# E-Blackboard #
################

#Start off by importing a bunch of libraries that we need
import subprocess
import signal
import time
import os
import sys
import traceback
import RPi.GPIO as GPIO
import datetime
from ftpupload import upload #now sftp
from mysqlcon import insertdata
from metadata import get_course
from imgprocessing import *

#Configure GPIO pins on the Raspberry
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)		#Left Front
GPIO.setup(17, GPIO.IN)		#Right Front
GPIO.setup(22, GPIO.IN)		#Left Back
GPIO.setup(27, GPIO.IN)		#Right Back

GPIO.setup(9, GPIO.OUT, initial=False)		#Gren Diode
GPIO.setup(10, GPIO.OUT, initial=False)		#Red Diode

GPIO.setup(18, GPIO.OUT)	#Pulsemodulator for the servo

#Spawning a subprocess which sets up portforwarding on port 3306 for our database connection
tunnel=subprocess.Popen("python2.7 tunnel.py", shell=True, preexec_fn=os.setsid) 

#Set up some static information for easier handlig
imgpath='eblackboard.se/public_html/img'

#These three lines will upload the device's IP address to our webserver
os.system("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d ':' -f2 | cut -d ' ' -f1 >> IP.txt")
upload('eblackboard.se','public_html','IP.txt')
os.system("rm IP.txt")

#Center the unit.
for x in range (0, 10):
		GPIO.output(18, True)
		time.sleep(0.0015)
		GPIO.output(18, False)
		time.sleep(0.1)

crntPos='c'	
lstPos=['l','c','r']
lstPosN=[0.0013, 0.0015, 0.0017]

GPIO.output(9, True) #Might want to wait with the all-clear until tunnel is open.

def servo(dest):
	signals = np.linspace(lstPosN[lstPos.index(crntPos)],lstPosN[lstPos.index(dest)], 101)
	for signal in signals:
		GPIO.output(18, True)
		time.sleep(signal)
		print signal
		GPIO.output(18, False)
		time.sleep(0.02-signal)

#The trigger function. 
#When ran it will check for activity on the GPIO pins and if there's activity it will return the pin number in question. 
#It also controls the servo and lights a diode.
def trigger():
	ret=0
	dest = crntPos
	if GPIO.input(4) == False:	
		ret=4
		dest = 'l'
	
	if GPIO.input(17) == False:
		ret=17
		dest = 'r'
	
	if GPIO.input(22) == False:
		ret=22
		dest = 'l'
	
	if GPIO.input(27) == False:
		ret=27
		dest = 'r'
		
	if ret!=0:
		GPIO.output(10, True)
		servo(dest)
		time.sleep(1)
		GPIO.output(9, True)
		print ret
	return ret, dest 
	
#This is the actual main part of the program.
#It is basically an infinite loop. If an exception is thrown we catch it and exit the program properly.
try:
	while True:
		[poll, crntPos]=trigger()		#Polling the trigger function to check the pins
		if poll!=0:			#If there is activity:
			print "running"
			#Set a bunch of variables
			
			#This is used when there's no lecture held in EA:
			[course_code, course_name]=["wrk001", "work may 30"]
			#[course_code, course_name]=get_course("EA")
			

			if course_code != None:
				datestamp = datetime.date.today().isoformat()
				timestamp = time.strftime("%H:%M:%S", time.gmtime())
				filename=datestamp+'.'+timestamp+'.jpg'
				os.system('raspistill -n -t 2000 -o '+filename)	#Tell the camera module to take a picture (after 2000ms) 
			
				#Check which sensor was triggered and crop the picture accordingly
				if(poll==4 or poll==17):
					imgproc(filename)
				elif(poll==22 or poll==27):
					imgproc(filename)

				#Upload the picture to the server and remove the picture file. Also insert the data in our database table.
				upload(imgpath,course_code,filename)
				os.system("rm "+filename)
				insertdata('../img/'+course_code+'/'+filename, datestamp, course_code, course_name)
			
				#Turn off the diodes
				GPIO.output(10, False)

#If the user presses 'Ctrl+C'
except KeyboardInterrupt:
	os.killpg(tunnel.pid, signal.SIGTERM) #Kill the subprocess we spawned
	GPIO.cleanup() #cleanup on all GPIO channels
	print("Process terminated")
	sys.exit(0)
	
#If the program throws a different exception
except Exception as e:
	os.killpg(tunnel.pid, signal.SIGTERM) #Kill the subprocess we spawned
	GPIO.cleanup() #cleanup on all GPIO channels
	print ('*** Caight exception: %s: %s' % (e.__class__, e))
	traceback.print_exc()
	sys.exit(1)
    
