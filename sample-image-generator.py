from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
from text_box import TextBox


def image_generator(text_boxes):
    img = Image.new("RGB", (600, 600), "lightgrey")
    font_size = [8, 16, 22, 26, 46]
    fonts = [ImageFont.truetype("Font_1.ttf", font_size[i]) for i in range(5)]
    sizes = [(60, 15), (120, 30), (180, 45), (240, 60), (300, 75)]
    available = [True]*400

    for i in text_boxes:
        text_box = Image.new("RGB", sizes[i.size], i.color)
        draw = ImageDraw.Draw(text_box)
        w, h = draw.textsize(i.text, fonts[i.size])
        draw.text(((sizes[i.size][0]-w)/2, (sizes[i.size][1]-h)/2), i.text, (255, 255, 255), fonts[i.size])
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
