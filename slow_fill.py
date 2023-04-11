import colorsys
import board
import neopixel


def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


LENGTH = 90

pixels = neopixel.NeoPixel(board.D18, LENGTH, auto_write=False)

i = 0

while True:
    (r, g, b) = colorsys.hsv_to_rgb(remap(i % LENGTH, 0, LENGTH - 1, 0, 1), 1, 1)
    pixels[i % LENGTH] = (
        int(remap(r, 0, 1, 0, 255)),
        int(remap(g, 0, 1, 0, 255)),
        int(remap(b, 0, 1, 0, 255))
    )

    if i > 0:
        pixels[i - 1] = (0, 0, 0)

    pixels.show()
    i += 1
