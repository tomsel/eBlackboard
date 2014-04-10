

from SimpleCV import *
from crophelp import *
import time
import os
def cropping_fram(filename):
    img = Image(filename)
    #img = Image("testmark.jpg")
#corners=[(0,0),(2992, -900),(3500,2044),(250,1944)]
#straight=img.warp(corners)
#img=straight


    #print (countingcoordinates(blobs))
    img=findingblobs(img)
    if img == "false":
        
        #WHAT WILL HAPPEN IF BOARD IS BLOCKED
    else:
        img.save(filename)
#    img=os.system('raspistill -o '+"newpct.jpg")
#    findingblobs(img)

    
    #Rader som tar en ny bild efter en stunds sleep
    


def cropping_bak(filename):
    img = Image(filename)


    img=findingblobsbak(img)
    if img == "false":
        
        #WHAT WILL HAPPEN IF BOARD IS BLOCKED
    else:
        img.save(filename)

    
    #Rader som tar en ny bild efter en stunds sleep
