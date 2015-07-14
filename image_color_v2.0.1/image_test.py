import Image,ImageDraw,ImageFont
import random 
import math

ch = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
width = 240
height = 60
font_size = 24

def randChar():
    return ch[random.randint(0,61)]

def randChColor():
    return ((random.randint(64,127)),(random.randint(64,127)),(random.randint(64,127)))

def randBgColor():
    return ((random.randint(32,255)),(random.randint(32,255)),(random.randint(32,255)))
#    return (255,255,255)

def randLineColor():
    return ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
#    return (0,0,0)

def randLineStartPos():
    return (random.randint(0,width*0.25),random.randint(0,60))

def randLineEndPos():
    return (random.randint(width*0.75,width),random.randint(0,60))

def randChRotate(img,ch_list):
    for x,y,ch in ch_list:
        rect_val = (x,y,x+font_size,y+font_size)
        rect = img.crop(rect_val)
        rect = rect.convert('RGBA')
        rect = rect.rotate(random.randint(0,45),expand=0)
        img.paste(rect,rect_val)

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

#    randChRotate(img,ch_list)
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill = randBgColor())
    for j in range(0,4):
        draw.line((randLineStartPos(),randLineEndPos()),fill=randLineColor(),width=1)
    
    img.save('test.jpg')

if __name__ == '__main__':
    genImage()
