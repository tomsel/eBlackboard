from SimpleCV import *
def getKey(item):
    return item[0]

def countingcoordinates(blobs):
    markers=list(marker for marker in blobs if abs(700-marker.area())<1200 )
    if len(markers) == 2:
        coordinates=[]
        for marker in markers:
            coordinates.append(marker.coordinates())
        sortedcor=sorted(coordinates, key= getKey)
        return(sortedcor)
    else:
        return ("false")
def crop1(img, sortedcor):
    img=img.crop(sortedcor[0][0],sortedcor[0][1],sortedcor[1][0]-sortedcor[0][0], sortedcor[1][1]-sortedcor[0][1])
    img.save("nytavla.jpg")
    return(img)

def findingblobs(img):
    color_blue = img.colorDistance(color = (0, 0, 255))
    onlyblue=img-color_blue

    blobs=onlyblue.findBlobs()
    sortedcor=countingcoordinates(blobs)
    if sortedcor!="false":
        crop1(img, sortedcor)
        return(img)
    else:
        return("false")
    
def findingblobsbak(img):
    color_blue = img.colorDistance(color = (0, 255, 0))
    onlyblue=img-color_blue

    blobs=onlyblue.findBlobs()
    sortedcor=countingcoordinates(blobs)
    if sortedcor!="false":
        crop1(img, sortedcor)
        return(img)
    else:
        return("false")
