import subprocess
import signal
import time
import os
import sys
#import RPi.GPIO as GPIO
#import Image
import datetime
from ftpupload import upload
from mysqlcon import insertdata
from metadata import get_course2 as get_course

"""GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)		#LILA
GPIO.setup(23, GPIO.IN)		#BRUN
GPIO.setup(24, GPIO.OUT)	#ROD
GPIO.setup(25, GPIO.OUT)	#BLA"""

tunnel=subprocess.Popen("python2.7 tunnel.py", shell=True, preexec_fn=os.setsid)
datestamp = datetime.date.today().isoformat()
imgpath='/eblackboard.se/public_html/img/'
course=get_course("EA")
course_code=course[0]
course_name=course[1]
#course="TEK016"
#os.system("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d ':' -f2 | cut -d ' ' -f1 >> IP.txt")
#upload('/eblackboard.se/','public_html','IP.txt')
#os.system("rm IP.txt")

try:
	while True:
		if raw_input("Waiting for input..."):
		#if GPIO.input(23)==False:
			#time.sleep(3)
			#GPIO.output(24, True)
			#ta bild
			timestamp = time.strftime("%H:%M:%S", time.gmtime())
			filename=datestamp+'.'+timestamp+'.jpg'
			os.system('cp sample.jpg '+filename)
			#os.system('raspistill -o '+filename)
			#time.sleep(9)

			#input_img=Image.open("image.jpg")
			#box= (300, 300, 1300, 1000)
			#output_img = input_img.crop(box)
			#output_img.save(filename)
			
			#ladda upp bild till ftp
			upload(imgpath,course_code,filename)
			os.system("rm "+filename)
			#ladda hem ics och ta fram data
			#pupulera databas
			print course_code
			print course_name
			insertdata('../img/'+course_code+'/'+filename, datestamp, course_code, course_name)
			
			#while GPIO.input(23) == False:
		    #   		count = 1
	   		#GPIO.output(24, False)

	   	if False:
	   	#if GPIO.input(22) == False:
			#time.sleep(3)
			#GPIO.output(24, True)
			#ta bild
			timestamp = time.strftime("%H:%M:%S", time.gmtime())
			filename=datestamp+'.'+timestamp+'.jpg'
			os.system('raspistill -o '+filename)
			#time.sleep(9)

			#input_img=Image.open("image.jpg")
			#box= (300, 300, 1300, 1000)
			#output_img = input_img.crop(box)
			#output_img.save(filename)
			
			#ladda upp bild till ftp
			upload(filename,course)
			os.system("rm "+filename)
			#ladda hem ics och ta fram data
			#pupulera databas
			insertdata('../img/'+course+'/'+filename, datestamp, course)
		
	    	#while GPIO.input(22) == False:
	    	#	count = 2
			#GPIO.output(25, False)  
			
except KeyboardInterrupt:
	os.killpg(tunnel.pid, signal.SIGTERM)
	print("Process terminated")
	sys.exit(0)
