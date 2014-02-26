from SimpleCV import *
import time
import os

disp = Display()

while disp.isNotDone:
	cntblue = 0
	os.system('raspistill -n -w 640 -h 420 -o imgtest.jpg')
	time.sleep(4)
	img = Image("imgtest.jpg")
	dis = img.colorDistance(color = (60, 30, 110)).invert()
	seg = dis.stretch(200, 255)
	blobs = seg.findBlobs()
	if blobs:
		for b in blobs:
			bcircle = b.isCircle(0.15)
			if  bcircle & (b.area() > 30):
				cntblue+=1
				b.draw()
		if cntblue == 3:		
			hej = img.save("hej3.jpg")
		seg.save(disp)

	

	