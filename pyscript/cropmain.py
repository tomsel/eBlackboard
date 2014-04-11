

from SimpleCV import *
from crophelp import *
import time
import os
def cropping_fram(filename):
    img = Image(filename)
    print("image is in crop function")
    #img = Image("testmark.jpg")
    corners=[(0,0),(3030, -800),(3600,2044),(250,1944)]
    img=img.warp(corners)
    img.save("warped.jpg")



    #print (countingcoordinates(blobs))
    img=findingblobs(img)
    if img == "false":
        foo=0
	print("oj")
        #WHAT WILL HAPPEN IF BOARD IS BLOCKED
    else:
        img.save(filename)
	print("image cropped and saved")
#    img=os.system('raspistill -o '+"newpct.jpg")
#    findingblobs(img)

    
    #Rader som tar en ny bild efter en stunds sleep
    


def cropping_bak(filename):
    img = Image(filename)
    print("image is in crop function")
    #img = Image("testmark.jpg")
    corners=[(0,0),(2992, -900),(3500,2044),(250,1944)]
    img=img.warp(corners)



    img=findingblobsbak(img)
    if img == "false":
        foo=0
        #WHAT WILL HAPPEN IF BOARD IS BLOCKED
    else:
        img.save(filename)

    
    #Rader som tar en ny bild efter en stunds sleep
