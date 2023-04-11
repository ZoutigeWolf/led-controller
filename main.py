import colorsys
import board
import neopixel


def remap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


LENGTH = 90

pixels = neopixel.NeoPixel(board.D18, LENGTH)

offset = 0

while True:
    for i in range(LENGTH):
        (r, g, b) = colorsys.hsv_to_rgb(remap(i + offset, 0, LENGTH - 1, 0, 1), 1, 1)
        pixels[i] = (
            remap(int(r), 0, 1, 0, 255),
            remap(int(g), 0, 1, 0, 255),
            remap(int(b), 0, 1, 0, 255)
        )

    offset += 1
