import colorsys
import time
import board
import neopixel


def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


LENGTH = 84

pixels = neopixel.NeoPixel(board.D18, LENGTH, auto_write=False)

pixels.fill((0, 0, 0))

i = 0

while True:
    (r, g, b) = colorsys.hsv_to_rgb(remap(i, 0, LENGTH - 1, 0, 1), 1, 1)
    pixels[i] = (
        int(remap(r, 0, 1, 0, 255)),
        int(remap(g, 0, 1, 0, 255)),
        int(remap(b, 0, 1, 0, 255))
    )

    if i == 83:
        pixels.fill((0, 0, 0))
        i = -1

    pixels.show()

    i += 1
