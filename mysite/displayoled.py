import time
from demo_opts import get_device
from luma.core.render import canvas
from luma.core import legacy
from PIL import ImageFont


def displaytextoled(texttext):
    #def main():
    MY_CUSTOM_BITMAP_FONT = [
        [
            0x00, 0x3e, 0x08, 0x3e, 0x00, 0x3e, 0x2a, 0x22,
            0x00, 0x3e, 0x20, 0x20, 0x00, 0x3e, 0x0a, 0x0e
        ]
    ]

    device = get_device()
    with canvas(device) as draw:
        ## Note that "\0" is the zero-th character in the font (i.e the only one)
        #legacy.text(draw, (0, 0), "\0", fill="white", font=MY_CUSTOM_BITMAP_FONT)

        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((0, 0), texttext, fill="white")

    time.sleep(5)


 
