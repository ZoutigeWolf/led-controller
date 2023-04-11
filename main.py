import time
import board
import neopixel

def generate_rainbow_colors():
    rainbow_colors = []
    for i in range(255):
        r = int(255 * ((i / 255) ** 2))
        g = int(255 * ((1 - ((i / 255) - 0.5) ** 2) ** 0.5))
        b = int(255 * (((255 - i) / 255) ** 2))
        rainbow_colors.append((r, g, b))
    return rainbow_colors


COLORS = generate_rainbow_colors()

LENGTH = 90

pixels = neopixel.NeoPixel(board.D18, LENGTH)

offset = 0

while True:
    print(offset)
    pixels[0] = COLORS[(offset) % 255]


    offset += 10
