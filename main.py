import time
import board
import neopixel

LENGTH = 90

RED = {255, 0, 0}
GREEN = {0, 255, 0}
BLUE = {0, 0, 255}

WHITE = RED | GREEN | BLUE
BLACK = {0, 0, 0}

pixels = neopixel.NeoPixel(board.D18, LENGTH)

i = 0

while True:
    pixels.fill(tuple(BLACK))

    v = i % LENGTH

    pixels[v] = (255, 0, 255)

    if (v - 1) >= 0:
        pixels[v - 1] = tuple(RED | BLUE)

    if (v + 1) < LENGTH:
        pixels[v + 1] = tuple(RED | BLUE)

    i += 1
    time.sleep(1)

