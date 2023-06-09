import colorsys
import board
import neopixel


def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


LENGTH = 84

pixels = neopixel.NeoPixel(board.D18, LENGTH, auto_write=False)

def rainbow_wave_effect():
    offset = 0

    while True:
        for i in range(LENGTH):
            (r, g, b) = colorsys.hsv_to_rgb(remap(i + offset, 0, LENGTH - 1, 0, 1), 1, 1)
            pixels[i] = (
                int(remap(r, 0, 1, 0, 255)),
                int(remap(g, 0, 1, 0, 255)),
                int(remap(b, 0, 1, 0, 255))
            )

        pixels.show()
        offset += 1
