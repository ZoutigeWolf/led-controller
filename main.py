import time
import board
import neopixel

def remap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def generate_rainbow_colors():
    rainbow_colors = []
    for i in range(255):
        if i < 85:
            r = 255
            g = int(255 * (i / 85))
            b = 0
        elif i < 170:
            i -= 85
            r = int(255 * ((85 - i) / 85))
            g = 255
            b = int(255 * (i / 85))
        else:
            i -= 170
            r = 0
            g = int(255 * ((85 - i) / 85))
            b = 255
        rainbow_colors.append((r, g, b))
    return rainbow_colors




COLORS = generate_rainbow_colors()

LENGTH = 90

pixels = neopixel.NeoPixel(board.D18, LENGTH)

offset = 0

while True:
    for i in range(LENGTH):
        pixels[i] = COLORS[(i * 10 + offset) % 255]

    offset += 25
