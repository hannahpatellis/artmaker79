from PIL import Image

## Get image from webcam, take a photo every x seconds
## Math to average together blocks of pixels to match the led rows/cols

im = Image.open('bode.png')
imrgb = im.convert("RGB")
pixels = list(imrgb.getdata())
width, height = im.size

ledrows = 9
ledcols = 7

for x in pixels:
    y = x[0]+x[1]+x[2]
    y = y/3
    y = round(y, 0)
    print(y)

# print(pixels)

print(len(pixels))
