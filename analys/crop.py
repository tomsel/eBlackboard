import Image

def crop_image(image, finishedimage, x, y, width, height):
    input_img = Image.open(image)
    box = (x, y, x + width, y + height)
    output_img = input_img.crop(box)
    output_img.save(finishedimage +".png")

def main():
    crop_image("image.png","output", 0, 0, 1029, 300)

if __name__ == '__main__': main()
