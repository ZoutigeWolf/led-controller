import sys
import board
import neopixel

LENGTH = 90

pixels = neopixel.NeoPixel(board.D18, LENGTH)

values = map(sys.argv[1].split(), int)

pixels.fill(tuple(values))