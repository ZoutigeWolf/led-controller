import colorsys
import time
import board
import neopixel


def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


LENGTH = 84

pixels = neopixel.NeoPixel(board.D18, LENGTH, auto_write=False)


def increase(decrease):
    for i in range(LENGTH - 1, -1, -1) if decrease else range(LENGTH):
        (r, g, b) = colorsys.hsv_to_rgb(remap(i, 0, LENGTH - 1, 0, 1), 1, 1)
        pixels[i] = (
            int(remap(r, 0, 1, 0, 255)),
            int(remap(g, 0, 1, 0, 255)),
            int(remap(b, 0, 1, 0, 255))
        ) if not decrease else (0, 0, 0)

        pixels.show()

        if i == 83 and not decrease:
            increase(True)
            return

        elif i == 0 and decrease:
            increase(False)
            return

        i += 1

        time.sleep(0.1)


increase(False)
