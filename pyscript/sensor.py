import subprocess
import time
import os
import sys
#import RPi.GPIO as GPIO
import Image
from datetime import date
from ftpscript import upload
from mysqlcon import insertdata
from download import get_course

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(22, GPIO.IN)		#LILA
#GPIO.setup(17, GPIO.IN)		#BRUN
#GPIO.setup(24, GPIO.OUT)	#ROD
#GPIO.setup(25, GPIO.OUT)	#BLA

tunnel=subprocess.Popen("python2.7 tunnel.py", shell=True)
datestamp = date.today()
imgpath='/eblackboard.se/public_html/img/'
course=get_course("EA") 

os.system("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d ':' -f2 | cut -d ' ' -f1 >> IP.txt")
upload('IP.txt','..')

try:
	while True:
		if raw_input("waiting for input"):
			time.sleep(3)
			#GPIO.output(24, True)
			#ta bild
			timestamp = time.strftime("%H:%M:%S", time.gmtime())
			filename="logo.png"
			#filename=datestamp+'.'+timestamp+'.jpg'
			#os.system('raspistill -o '+filename)
			time.sleep(9)

			#input_img=Image.open("image.jpg")
			#box= (300, 300, 1300, 1000)
			#output_img = input_img.crop(box)
			#output_img.save("croppedimg.jpg")
			
			#ladda upp bild till ftp
			upload(filename,course)
			#ladda hem ics och ta fram data
			#pupulera databas
			insertdata('../img/'+course+'/'+filename, datestamp, course)
			
			#while GPIO.input(17) == False:
		       	#	count = 1
	   		#GPIO.output(24, False)

	   	if False:
			time.sleep(3) 
			#GPIO.output(25, True)
			#ta bild
			timestamp = time.strftime("%H:%M:%S", time.gmtime())
			filename=datestamp+'.'+timestamp+'.jpg'
			os.system('raspistill -o '+filename)
			time.sleep(9)
			
			#input_img=Image.open("image.jpg")
			#box= (300, 300, 1300, 1000)
			#output_img = input_img.crop(box)
			#output_img.save("croppedimg.jpg")
		
			#ladda upp bild till ftp
			upload(filename,course)
			#ladda hem ics och ta fram data
			#pupulera databas
			insertdata('../img/'+course+'/'+filename, datestamp, course)
		
	    		#while GPIO.input(22) == False:
	    		#count = 2
			#GPIO.output(25, False)  
			
except KeyboardInterrupt:
	tunnel.terminate()
	print("Process terminated")
	sys.exit(0)
