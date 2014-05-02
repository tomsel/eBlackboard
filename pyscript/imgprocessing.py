from SimpleCV.ImageClass import * 
from SimpleCV.Features import * 
from scipy.cluster.vq import kmeans
import numpy as np
import sys

#TODO: -Implement custom exceptions and handle them properly
#	   -Tweak blob size value
#	   -Figure out aspect ratio of the blackboard and tweak final image size

#Initial strategy:
#Load the original image, run edge detection and dilate the edges. 
#Then floodfill whatever enclosed area is in the center of the image.
#The blackboard should now be a big white thing in the middle. 
#Now we erode the smaller junk that was found around the blackboard.

def imgproc(filename):
	#avoid img7, img11
	#img2 is not exactly fair either
	#img12 is... interesting
	#img = Image("img1.jpg")
	img = Image(filename)
	img2 = img.edges().dilate(1)
	#img2.save('tmp/1 dilated edges.jpg')

	#We assume the camera is centered on the blackboard and that one of the target point doesn't hit text or figures.
	targets=np.array(((img.width/2,img.height/2-20-150),
					  (img.width/2+50,img.height/2-150),
					  (img.width/2-50,img.height/2-150)))

	img2fill=img2.floodFill(targets, color=(255,255,255))
	for target in targets:
		img2fill.drawCircle(target,10,(0,0,255),3)
	
	#img2fill.save('tmp/2 flooded.jpg')

	img3 = img2fill.erode(4)
	#img3.save('tmp/3 eroded.jpg')

	#Here we actually do the detective work of finding that big white thing, and then we smooth it out.
	blobs = img3.findBlobs(minsize=100000) #TODO: tweak this value
	#TODO: if len(blob)>1: raise exception
	mask = blobs[0].getFullHullMask()
	#mask.save('tmp/4 mask.jpg')

	#Let's draw a couple of lines
	lines=mask.findLines(threshold=80, minlinelength=50, maxlinegap=5) 
	lines.draw((255,0,0), 5)
	#mask.save('tmp/5 lines.jpg')

	#Find out where the lines intersect. This will be roughly where the corners are.
	corners = [] 
	for i in range(0,len(lines)-1):
		for j in range(i+1,len(lines)):
			angle = np.absolute(lines[i].angle()-lines[j].angle())
			if angle > 50 and angle < 130:
				pt=lines[i].findIntersection(lines[j])
				if pt[0]>0 and pt[0]<img.width and pt[1]>0 and pt[1]<img.height: #making sure the corners are in the image. Could be a waste of computing time
					corners.append(pt)
			
	#Regard the duplicate corners as clusters and find the centre of each cluster through the k-means algorithm.
	cornerArray = kmeans(np.array(corners), 4)[0]

	#Find the centre of mass of the blackboard projection.
	center=np.array((0,0))
	for corner in cornerArray:
		img.drawCircle(corner, 20, (255,0,0), 2)
		center+=corner
	center = np.divide(center,len(cornerArray))
	img.drawCircle(center, 20, (0,255,0), 4)
	#img.save('tmp/6 corners.jpg')

	#Rearrange the corners to sit where they're supposed to
	top=[]
	bot=[]
	for corner in cornerArray:
		if corner[1] < center[1]:
			top.append((corner[0],corner[1]))
		else:
			bot.append((corner[0],corner[1]))

	if top[0][0]>top[1][0]:
		top.reverse()
	if bot[1][0]>bot[0][0]:
		bot.reverse()
	top.extend(bot)
	cornerArray=np.array(top)

	#Change the perspective, crop, and Bob's your uncle. Done
	width=2000
	height=1000
	points = ((0,0),(width,0),(width,height),(0,height)) #These values will have to be adjusted to fit aspect ratio
	src = tuple(map(tuple, cornerArray))
	result = cv.CreateMat(3,3,cv.CV_32FC1)
	cv.GetPerspectiveTransform(src,points,result)
	img5 = img.transformPerspective(result).crop(0,0,width,height)

	#img5.save('tmp/7 result.jpg')
	img5.save(filename)