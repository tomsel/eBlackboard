import time
import os
import RPi.GPIO as GPIO
import Image
import ftplib 

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)		#LILA
GPIO.setup(17, GPIO.IN)		#BRUN
GPIO.setup(24, GPIO.OUT)	#ROD
GPIO.setup(25, GPIO.OUT)	#BLA

while True:

	if GPIO.input(17) == False:
		time.sleep(3)
		GPIO.output(24, True)
		os.system('raspistill -o image.jpg')
		time.sleep(9)
		#input_img=Image.open("image.jpg")
		#box= (300, 300, 1300, 1000)
		#output_img = input_img.crop(box)
		#output_img.save("croppedimg.jpg")
		
		#session = ftplib.FTP('129.16.235.90','simon','linser') 
		#file = open('croppedimg.jpg','rb') # file to send 
		#session.storbinary('STOR eBlackboard/hello.jpg', file) # send the file 
		#file.close() # close file and FTP 
		#session.quit()
		
		while GPIO.input(17) == False:
           		count = 1
   		GPIO.output(24, False)

   	if GPIO.input(22) == False:
		time.sleep(3) 
		GPIO.output(25, True)
		os.system('raspistill -o image.jpg')
		time.sleep(9)
		#input_img=Image.open("image.jpg")
		#box= (300, 300, 1300, 1000)
		#output_img = input_img.crop(box)
		#output_img.save("croppedimg.jpg")
		
		#session = ftplib.FTP('129.16.235.90','simon','linser') 
		#file = open('croppedimg.jpg','rb') # file to send 
		#session.storbinary('STOR eBlackboard/hello.jpg', file) # send the file 
		#file.close() # close file and FTP 
		#session.quit()
		
        	while GPIO.input(22) == False:
        		count = 2
    		GPIO.output(25, False)  
