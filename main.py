import time
import board
import neopixel

def generate_rainbow_colors():
    rainbow_colors = []
    for i in range(255):
        if i < 85:
            r = int(255 * (i / 85))
            g = int(255 * (i / 85))
            b = int(255 * ((85 - i) / 85))
        elif i < 170:
            i -= 85
            r = int(255 * (i / 85))
            g = int(255 * ((85 - i) / 85))
            b = 0
        else:
            i -= 170
            r = int(255 * ((85 - i) / 85))
            g = 0
            b = int(255 * (i / 85))
        rainbow_colors.append((r, g, b))
    return rainbow_colors


COLORS = generate_rainbow_colors()

LENGTH = 90

pixels = neopixel.NeoPixel(board.D18, LENGTH)

offset = 0

while True:
    for i in range(LENGTH):
        pixels[i] = COLORS[i]

    offset += 1
