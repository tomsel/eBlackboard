
from SimpleCV import *

img = Image("dotboard.jpg")
color_purple = img.colorDistance(color = (0, 0, 255))
onlypurple=img-color_purple

blobs=onlypurple.findBlobs()

tavla=next(b for b in blobs if abs(700 - b.area()) < 300)
coordinatesblue= tavla.coordinates()

color_green = img.colorDistance(color = (0, 255, 0))

onlygreen=img-color_green
blobsg=onlygreen.findBlobs()
tavlag=next(b for b in blobsg if abs(700 - b.area()) < 300)
coordinatesgreen=tavlag.coordinates()
print(coordinatesgreen)
img=img.crop(coordinatesblue[0],coordinatesblue[1],coordinatesgreen[0]-coordinatesblue[0], coordinatesgreen[1]-coordinatesblue[1])
img.save("nytavla.jpg")
win = img.show()

#wait for user input before closing
raw_input()
win.quit()
