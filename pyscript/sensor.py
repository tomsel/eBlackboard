import time
import os
import RPi.GPIO as GPIO
import Image
from ftpscript import upload
from mysqlcon import insertdata

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)		#LILA
GPIO.setup(17, GPIO.IN)		#BRUN
GPIO.setup(24, GPIO.OUT)	#ROD
GPIO.setup(25, GPIO.OUT)	#BLA

tunnel=subprocess.Popen("python2.7 tunnel.py", shell=True)
imgcounter = 0 #nollas aldrig i programmet
date = '2014-03-11' #ska fungera automatiskt i framtiden
imgpath='/eblackboard.se/public_html/eBlackboard/webinterface/img/'
course='TDA514' #ska fungera automatiskt i framtiden

try:
	while True:
		if GPIO.input(17) == False:
			time.sleep(3)
			GPIO.output(24, True)
			#ta bild
			imgcounter++
			filename=date+str(imgcounter)+'.jpg'
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
			insertdata(imgpath+course+'/'+filename, date, course)
		
			while GPIO.input(17) == False:
		       		count = 1
	   		GPIO.output(24, False)

	   	if GPIO.input(22) == False:
			time.sleep(3) 
			GPIO.output(25, True)
			#ta bild
			imgcounter++
			filename=date+str(imgcounter)+'.jpg'
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
			insertdata(imgpath+course+'/'+filename, date, course)
		
	    	while GPIO.input(22) == False:
	    		count = 2
			GPIO.output(25, False)  
			
except KeyboardInterrupt
	tunnel.terminate()
	print("Process terminated")
