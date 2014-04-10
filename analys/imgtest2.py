
from SimpleCV import *
from crophelp import countingcoordinates
from crophelp import getKey
from crophelp import crop1
img = Image("realtest2.jpg")
color_blue = img.colorDistance(color =(56, 121, 31))
onlyblue=color_blue.binarize(31)
blobs=onlyblue.findBlobs()
blobs.draw()
#markers=list(marker for marker in blobs if abs(1500-marker.area())<1200 )
#print(len(markers))
sortedcor=countingcoordinates(blobs)
print(sortedcor)
if sortedcor!="false":
    img=crop1(img, sortedcor)
    onlyblue.show()
    img.save("croppic.jpg")
else:
    print("falseee")
    onlyblue.show()
    
#color_purple = img.colorDistance(color = (56, 121, 31))
#onlypurple=img-color_purple
#onlypurple=color_purple.binarize(40)
#blobs=onlypurple.findBlobs()
#blobs.draw()
#fixat intervallet
#tavla=next(b for b in blobs if abs(1500 - b.area()) < 1000)
#coordinatesblue= tavla.coordinates()
#print(tavla.area())
#print(coordinatesblue)
#onlypurple.show()

#color_green = img.colorDistance(color = (0, 255, 0))

#onlygreen=img-color_green
#blobsg=onlygreen.findBlobs()
#tavlag=next(b for b in blobsg if abs(700 - b.area()) < 200)
#coordinatesgreen=tavlag.coordinates()
#print(coordinatesgreen)
#img=img.crop(coordinatesblue[0],coordinatesblue[1],coordinatesgreen[0]-coordinatesblue[0], coordinatesgreen[1]-coordinatesblue[1])
#img.save("nytavla.jpg")
#win = img.show()

#wait for user input before closing
#raw_input()
#win.quit()
