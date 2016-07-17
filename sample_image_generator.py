from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
from text_box import TextBox


def image_generator(text_boxes, coloring):
    img = Image.new("RGB", (600, 600), "lightgrey")
    fonts = [ImageFont.truetype("Font_1.ttf", i) for i in [8, 16, 22, 26, 46]]
    available = [True]*400

    for i in text_boxes:
        bg = [i.color, "lightgrey"]
        text_color = ["white", i.color]
        box_size = (60*(i.size+1), 15*(i.size+1))
        text_box = Image.new("RGB", box_size, bg[coloring-1])
        draw = ImageDraw.Draw(text_box)
        w, h = draw.textsize(i.text, fonts[i.size])
        draw.text(((box_size[0]-w)/2, (box_size[1]-h)/2), i.text, text_color[coloring-1], fonts[i.size])

        free = False
        while not free:
            x = random.randrange(10-i.size)
            y = random.randrange(40-i.size)
            free = True
            for j in range(i.size+1):
                for k in range(i.size+1):
                    free = free and available[(y+j)*10+(x+k)]
        for j in range(i.size+1):
            for k in range(i.size+1):
                available[(y+j)*10+(x+k)] = False
        img.paste(text_box, (x*60, y*15))

    img.save('sample-out.png')
    img.show()
