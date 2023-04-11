import time
import board
import neopixel

LENGTH = 90

RED = 0x100000
GREEN = 0x001000
BLUE = 0x000010

WHITE = RED | GREEN | BLUE
BLACK = 0x000000

pixels = neopixel.NeoPixel(board.D18, LENGTH)

i = 0

while True:
    pixels.fill(BLACK)

    v = i % LENGTH

    pixels[v] = (255, 0, 255)

    if (v - 1) >= 0:
        pixels[v - 1] = BLUE | RED

    if (v + 1) < LENGTH:
        pixels[v + 1] = BLUE | RED

    i += 1
    time.sleep(1)

