# -*- coding:utf-8 -*-
#usr/bin/python
# Python: 	python3.4.3
# platform:	windows
# Author:	Mr.Yuan		fusu1435@163.com
# Program:	验证码图片生成
# History:	2015.6.4 v1.0.1
from PIL import Image,ImageDraw,ImageFont
import random 

ch = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def randChar():
    return ch[random.randint(0,61)]

def randChColor():
    return ((random.randint(32,255)),(random.randint(32,255)),(random.randint(32,255)))

def randBgColor():
    return ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))

def randLineColor():
    return ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))

def randLinePos():
    return (random.randint(0,240),random.randint(0,60))
    
def genImage():
    width = 240
    height = 60
    font = ImageFont.truetype('FreeSans.ttf',16)
    img = Image.new('RGB',(width,height),(255,255,255))
    draw = ImageDraw.Draw(img)
    for i in range(0,4):
        draw.text((60*i+10,20),randChar(),font=font,fill=randChColor())

    for j in range(0,5):
        draw.line((randLinePos(),randLinePos()),fill=randLineColor(),width=1)
    img.show()
    img.save('test.jpg','jpeg')
if __name__ == '__main__':
    genImage()
