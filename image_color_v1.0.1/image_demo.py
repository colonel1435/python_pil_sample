import Image,ImageDraw,ImageFont,ImageFilter

import random

ch = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 
      'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      1,2,3,4,5,6,7,8,9,0)
def rndChar():
#    return chr(random.randint(65,90))
     return ch[random.randint(0,62)]
def rndColor():
    return (random.randint(32,255),random.randint(32,255),random.randint(32,255))
def rndColor1():
    return (random.randint(64,127),random.randint(64,127),random.randint(64,255))
width = 60*4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf',36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill = rndColor())
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor1())
#image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')


