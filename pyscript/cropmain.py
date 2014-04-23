
#from main import *
from SimpleCV import *
from crophelp import *
import time
import os
def cropping_fram(filename,cnt):
    img = Image(filename)
    imgcopy=img
    print("image is in crop function")
    #img = Image("testmark.jpg")
    #corners=[(0,0),(3030, -800),(3600,2044),(250,1944)]
    #img=img.warp(corners)
    img.save("warped.jpg")



    #print (countingcoordinates(blobs))
    img=findingblobs(img)
    if img == "false":
        cnt=cnt+1
        foo=1
        print("blackboard not found, repeating! ")
        time.sleep(1)
        if (cnt <5):
            #add the function that takes a new picture here
            cropping_fram(filename,cnt)
        else:
            imgcopy.save(filename+"2.jpg")

    else:
        img.save(filename+"2.jpg")
        print("image cropped and saved")
#    img=os.system('raspistill -o '+"newpct.jpg")
#    findingblobs(img)

    
    #Rader som tar en ny bild efter en stunds sleep
    


def cropping_bak(filename,cnt):
    img = Image(filename)
    imgcopy=img
    print("image is in crop function")
    #img = Image("testmark.jpg")
    corners=[(0,0),(2992, -900),(3500,2044),(250,1944)]
    img=img.warp(corners)



    img=findingblobsbak(img)
    if img == "false":
        cnt=cnt+1
        foo=1
        print("blackboard not found, repeating! ")
        time.sleep(1)
        if (cnt <5):
            #add the function that takes a new picture here
            cropping_bak(filename,cnt)
        else:
            imgcopy.save(filename+"2.jpg")
        #HOW TO CANCEL IF THE SENSOR IS ACTIVATED?? possible rebuild of the main program
        #mainprog()
    else:
        img.save(filename+"2.jpg")
        print("image cropped and saved")
    
    #Rader som tar en ny bild efter en stunds sleep
