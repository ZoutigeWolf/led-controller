import sys
import board
import neopixel

LENGTH = 90

pixels = neopixel.NeoPixel(board.D18, LENGTH)

pixels.fill((
    int(sys.argv[1]),
    int(sys.argv[2]),
    int(sys.argv[3])
))