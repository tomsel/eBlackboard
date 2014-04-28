#import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import Image
#def crop_image(image, finishedimage, x, y, width, height):
def ownfilter(pxvalues):
    input_img = Image.open("unfiltered.jpg")
    input_img=input_img.convert('RGB')
    K=input_img.size
    X=K[0]-1
    Y=K[1]-1
    print("X AND Y")
    print(X)
    print(Y)

#x=700
#y=420
#box = (x, y, x + 1800, y + 850)
    px=input_img.getpixel((X,Y))
    R,G,B=px
    brightness=sum([R,G,B])/3
    print("BRIGHTNESS:")
    print(brightness)
    enhancer=ImageEnhance.Contrast(input_img)
    if (brightness<70):
        output_image=enhancer.enhance(1.2)
    else:
        output_image=enhancer.enhance(0.8)
    
    
    fi=output_image.filter(ImageFilter.EDGE_ENHANCE)
    fi.save("filteredimg" +".jpg")
    return fi

#fi=newImage.filter(ImageFilter.EDGE_ENHANCE)
#fi1=fi.filter(ImageFilter.BLUR)
#fi1=fi.stretch(200,255)
#fi1.invert()
#fi.save("filterimage1" +".jpg")

#def main():
#    crop_image("19marstest.jpg","output", 700, 420, 1800, 850)

#if __name__ == '__main__': main()

