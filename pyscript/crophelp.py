from SimpleCV import *
def getKey(item):
    return item[0]

def countingcoordinates(blobs):
    if not blobs:
        return("false")
    markers=list(marker for marker in blobs if abs(1500-marker.area())<1200 )
    #print(len(markers))
    if len(markers) == 2:
        coordinates=[]
        for marker in markers:
            coordinates.append(marker.coordinates())
        sortedcor=sorted(coordinates, key= getKey)
        return(sortedcor)
    else:
        return ("false")
def crop1(img, sortedcor):
    img2=img.crop(sortedcor[0][0],sortedcor[0][1],sortedcor[1][0]-sortedcor[0][0], sortedcor[1][1]-sortedcor[0][1])
    img.save("nytavla.jpg")
    return(img2)

def findingblobs(img):
    img=Image("warped.jpg")
    img.save("predistance.jpg")
    color_blue = img.colorDistance(color=(56, 121, 3))
    color_blue.save("colordistance.jpg")
    onlyblue=color_blue.binarize(32)
    onlyblue.save("binarized.jpg")
    blobs=onlyblue.findBlobs()
    sortedcor=countingcoordinates(blobs)
    if sortedcor!="false":
        img=crop1(img, sortedcor)
        return(img)
    else:
        return("false")
    
def findingblobsbak(img):
    color_blue = img.colorDistance(color = (255, 0, 0))
    onlyblue=color_blue.binarize(60)

    blobs=onlyblue.findBlobs()
    sortedcor=countingcoordinates(blobs)
    if sortedcor!="false":
        crop1(img, sortedcor)
        return(img)
    else:
        return("false")
