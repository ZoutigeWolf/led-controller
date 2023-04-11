import time
import board
import neopixel

LENGTH = 90

pixels = neopixel.NeoPixel(board.D18, LENGTH)

i = 0

while True:
    pixels.fill((0, 0, 0))
    pixels[i % 90] = (255, 0, 255)
    i += 1
