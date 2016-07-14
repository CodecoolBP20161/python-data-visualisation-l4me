from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
from text_box import TextBox

img = Image.new("RGB", (600, 600), "white")
fonts = []
fonts.append(ImageFont.truetype("Xposed.ttf", 10))
fonts.append(ImageFont.truetype("Xposed.ttf", 16))
fonts.append(ImageFont.truetype("Xposed.ttf", 22))
fonts.append(ImageFont.truetype("Xposed.ttf", 26))
fonts.append(ImageFont.truetype("Xposed.ttf", 48))


sizes = [(60, 15), (120, 30), (180, 45), (240, 60), (300, 75)]
available = [True]*400
for i in TextBox.client():
    text_box = Image.new("RGB", sizes[i.size-1], i.color)
    draw = ImageDraw.Draw(text_box)
    w, h = draw.textsize(i.text, fonts[i.size-1])
    draw.text(((sizes[i.size-1][0]-w)/2, (sizes[i.size-1][1]-h)/2), i.text, (255, 255, 255), fonts[i.size-1])
    free = False
    while not free:
        x = random.randint(0, 10-i.size)
        y = random.randint(0, 40-i.size)
        free = True
        for j in range(i.size):
            for k in range(i.size):
                free = free and available[(y+j)*10+(x+k)]
    for j in range(i.size):
        for k in range(i.size):
            available[(y+j)*10+(x+k)] = False
    img.paste(text_box, (x*60, y*15))
img.save('sample-out.png')
img.show()
