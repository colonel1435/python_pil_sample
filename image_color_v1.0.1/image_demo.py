# -*- coding:utf-8 -*-
#!/usr/bin/python
# Python:          3.4.3
# Platform:        Windows
# Author:          Mr.Yuan	fusu1435@163.com
# Program:         验证码图片生成
# History:         2015.6.4 v1.0.1
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

ch = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
width = 60*4
height = 60
def randChar():
    return ch[random.randint(0,61)]
def randBgColor():
    return (random.randint(32,255),random.randint(32,255),random.randint(32,255))
def randChColor():
    return (random.randint(64,127),random.randint(64,127),random.randint(64,255))
def randLineColor():
#    return ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
    return (0,0,0)
def randLineStartPos():
    return (random.randint(0,width*0.25),random.randint(0,60))

def randLineEndPos():
    return (random.randint(width*0.75,width),random.randint(0,60))
def genImage():    
    image = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('FreeSans.ttf',36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(0,height):
            draw.point((x,y),fill = randBgColor())
    for t in range(0,4):
        draw.text((60*t+10,10),randChar(),font=font,fill=randChColor())
    
    for j in range(0,4):
        draw.line((randLineStartPos(),randLineEndPos()),fill=randLineColor(),width=1)
	#image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg','jpeg')

if __name__ == '__main__':
	genImage()
