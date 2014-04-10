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
from cropmain import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)		#Vanster
GPIO.setup(17, GPIO.IN)		#Vanster
GPIO.setup(22, GPIO.OUT)	#Hoger
GPIO.setup(27, GPIO.OUT)	#Hoger

GPIO.setup(9, GPIO.OUT)		#Gron Diod
GPIO.setup(10, GPIO.OUT)	#Rod Diod

GPIO.setup(18, GPIO.OUT)	#PulsModdare Motor

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

		if GPIO.input(4) == False:
			print('4')
			GPIO.output(10, True)
			for x in range (0, 7):
				GPIO.output(18, True)
				time.sleep(0.0012)
				GPIO.output(18, False)
				time.sleep(0.5)
			time.sleep(2)
			GPIO.output(9, True)
			time.sleep(5) #Remove
			
			timestamp = time.strftime("%H:%M:%S", time.gmtime())
			filename=datestamp+'.'+timestamp+'.jpg'
			os.system('cp sample.jpg '+filename)
			os.system('raspistill -o '+filename)
	
			cropping_fram(filename)

			#ladda upp bild till ftp
			upload(filename,course)
			os.system("rm "+filename)
			#ladda hem ics och ta fram data
			#pupulera databas
			insertdata('../img/'+course+'/'+filename, datestamp, course)

			GPIO.output(10, False)
			time.sleep(3)
			GPIO.output(9, False)

		if GPIO.input(17) == False:
			print('17')
			GPIO.output(10, True)
			for x in range (0, 7):
				GPIO.output(18, True)
				time.sleep(0.0012)
				GPIO.output(18, False)
				time.sleep(0.5)
			time.sleep(2)
			GPIO.output(9, True)
			time.sleep(5) #Remove
			
			timestamp = time.strftime("%H:%M:%S", time.gmtime())
			filename=datestamp+'.'+timestamp+'.jpg'
			os.system('cp sample.jpg '+filename)
			os.system('raspistill -o '+filename)
	
			cropping_bak(filename)

			#ladda upp bild till ftp
			upload(filename,course)
			os.system("rm "+filename)
			#ladda hem ics och ta fram data
			#pupulera databas
			insertdata('../img/'+course+'/'+filename, datestamp, course)

			GPIO.output(10, False)
			time.sleep(3)
			GPIO.output(9, False)

		if GPIO.input(22) == False:
			print('22')
			GPIO.output(10, True)
			for x in range (0, 7):
				GPIO.output(18, True)
				time.sleep(0.0017)
				GPIO.output(18, False)
				time.sleep(0.5)
			time.sleep(2)
			GPIO.output(9, True)
			time.sleep(5) #Remove
			
			timestamp = time.strftime("%H:%M:%S", time.gmtime())
			filename=datestamp+'.'+timestamp+'.jpg'
			os.system('cp sample.jpg '+filename)
			os.system('raspistill -o '+filename)
	
			cropping_fram(filename)

			#ladda upp bild till ftp
			upload(filename,course)
			os.system("rm "+filename)
			#ladda hem ics och ta fram data
			#pupulera databas
			insertdata('../img/'+course+'/'+filename, datestamp, course)

			GPIO.output(10, False)
			time.sleep(3)
			GPIO.output(9, False)


		if GPIO.input(27) == False:
			print('27')
			GPIO.output(10, True)
			for x in range (0, 7):
				GPIO.output(18, True)
				time.sleep(0.0017)
				GPIO.output(18, False)
				time.sleep(0.5)
			time.sleep(2)
			GPIO.output(9, True)
			time.sleep(5) #Remove
			
			timestamp = time.strftime("%H:%M:%S", time.gmtime())
			filename=datestamp+'.'+timestamp+'.jpg'
			os.system('cp sample.jpg '+filename)
			os.system('raspistill -o '+filename)
	
			cropping_bak(filename)

			#ladda upp bild till ftp
			upload(filename,course)
			os.system("rm "+filename)
			#ladda hem ics och ta fram data
			#pupulera databas
			insertdata('../img/'+course+'/'+filename, datestamp, course)

			GPIO.output(10, False)
			time.sleep(3)
			GPIO.output(9, False)


	GPIO.cleanup(4)
	GPIO.cleanup(17)
	GPIO.cleanup(22)
	GPIO.cleanup(27)
	GPIO.cleanup(10)
	GPIO.cleanup(9)
	GPIO.cleanup(18)


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

	   	#if False:
	   	#if GPIO.input(22) == False:
			#time.sleep(3)
			#GPIO.output(24, True)
			#ta bild
			#timestamp = time.strftime("%H:%M:%S", time.gmtime())
			#filename=datestamp+'.'+timestamp+'.jpg'
			#os.system('raspistill -o '+filename)
			#time.sleep(9)

			#input_img=Image.open("image.jpg")
			#box= (300, 300, 1300, 1000)
			#output_img = input_img.crop(box)
			#output_img.save(filename)
			
			#ladda upp bild till ftp
			#upload(filename,course)
			#os.system("rm "+filename)
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
