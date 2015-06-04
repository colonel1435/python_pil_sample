# -*- coding:utf-8 -*-
#!/usr/bin/python
# Python:          3.4.3
# Platform:        Windows
# Author:          Mr.Yuan	fusu1435@163.com
# Program:         验证码图片生成
# History:         2015.6.4 v3.0.1
from PIL import Image,ImageDraw,ImageFont
import random 
import math

ch = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
width = 240
height = 60
font_size = 24

def randChar():
    return ch[random.randint(0,61)]

def randChColor():
    return ((random.randint(32,255)),(random.randint(32,255)),(random.randint(32,255)))

def randBgColor():
    return ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))

def randLineColor():
    return ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))

def randLineStartPos():
    return (random.randint(0,width*0.25),random.randint(0,60))

def randLineEndPos():
    return (random.randint(width*0.75,width),random.randint(0,60))

def randChRotate(img,ch_list):
	  for x,y,ch in ch_list:
	  	rect_val = (x,y,x+font_size,y+font_size)
	  	rect = img.crop(rect_val)
	  	rect = rect.rotate(random.randint(0,45))
	  	img.paste(rect,rect_val)
#                rect.show()

def randChPos(ch_list):
    xMargin = 30 
    yMargin = font_size+5
    x_space = 10
    x_list = []
    for i in range(0,4):

        x = random.randint(xMargin,width-xMargin)
        y = random.randint(yMargin,height-yMargin)
        for val in x_list:
            if math.abs(x,val) < x_space:
               if x - val > 0:
                   x = x + x_space/2
               else:
                   x = x - x_space/2
        ch_list.append((x,y,randChar()))
        print(ch_list[i])

def genImage():
    ch_list = []
    font = ImageFont.truetype('FreeSans.ttf',font_size)
    img = Image.new('RGB',(width,height),(255,255,255))
    draw = ImageDraw.Draw(img)
    randChPos(ch_list)
    for x,y,ch in ch_list:
        draw.text((x,y),ch,font=font,fill=randChColor())
#        draw.text((60*i+10,20),randChar(),font=font,fill=randChColor())

    for j in range(0,4):
        draw.line((randLineStartPos(),randLineEndPos()),fill=randLineColor(),width=2)
#    randChRotate(img,ch_list)
    
    img.show()
    img.save('test.jpg','jpeg')

if __name__ == '__main__':
    genImage()
