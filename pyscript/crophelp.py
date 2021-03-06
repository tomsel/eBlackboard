from SimpleCV import *
from pyfilter import ownfilter
def getKey(item):
    return item[0]

def countingcoordinates(blobs):
    if not blobs:
        return("false")
    markers=list(marker for marker in blobs if abs(1500-marker.area())<1200 and marker.isCircle(0.35))
    print("MARKERS:")
    print(len(markers))
    if len(markers) == 2:
        coordinates=[]
        for marker in markers:
            coordinates.append(marker.coordinates())
        sortedcor=sorted(coordinates, key= getKey)
        if(sortedcor[0][0]>sortedcor[1][0] or sortedcor[0][1]>sortedcor[1][1]):
            print("fail!")
            return("false")
        print(sortedcor)
        return(sortedcor)
    else:
        return ("false")
def crop1(img, sortedcor):
    img2=img.crop(sortedcor[0][0],sortedcor[0][1],sortedcor[1][0]-sortedcor[0][0], sortedcor[1][1]-sortedcor[0][1])
    #img.save("nytavla.jpg")
    return(img2)

def findingblobs(img):
    img=Image("warped.jpg")
    img.save("predistance.jpg")
    #color_blue = img.colorDistance(color=(86, 127, 25))
    color_blue = img.colorDistance(color=(60, 115, 50))
    #color_blue = img.colorDistance(color=(40, 112, 6))
    color_blue.save("colordistance.jpg")
    onlyblue=color_blue.binarize(27)
    #onlyblue=color_blue.binarize(32)
    onlyblue.save("binarized.jpg")
    blobs=onlyblue.findBlobs()
    #blobs.draw()
    #onlyblue.save("binarized.jpg")
    sortedcor=countingcoordinates(blobs)
    if sortedcor!="false":
        img=crop1(img, sortedcor)
        img.save("unfiltered.jpg")
        img=ownfilter(sortedcor)
        return(img)
    else:
        return("false")
    
def findingblobsbak(img):
    color_blue = img.colorDistance(color = (181, 45, 48))
    color_blue.save("colordistance.jpg")
    onlyblue=color_blue.binarize(40)
    onlyblue.save("binarized.jpg")
    blobs=onlyblue.findBlobs()
    sortedcor=countingcoordinates(blobs)
    if sortedcor!="false":
        print("cropping!!!")
        img=crop1(img, sortedcor)
        img=ownfilter(sortedcor)
        return(img)
    else:
        return("false")
