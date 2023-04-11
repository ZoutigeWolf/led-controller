import time
import board
import neopixel

LENGTH = 90

pixels = neopixel.NeoPixel(board.D18, LENGTH)

i = 0

while True:
    for j in range(len(pixels)):
        pixels[j] = (255, 0, 255) if i % 90 == j else (0, 0, 0)

    i += 1;
