import Image

#def crop_image(image, finishedimage, x, y, width, height):
#   input_img = Image.open(image)
#    box = (x, y, x + width, y + height)
#    output_img = input_img.crop(box)
#    output_img.save(finishedimage +".png")

input_img=Image.open("image.jpg")
box= (300, 300, 1300, 1000)
output_img = input_img.crop(box)
output_img.save("croppedimg.jpg")
#def main():
#    crop_image("image.jpg","output", 0, 0, 1029, 300)
#
#if __name__ == '__main__': main()
