import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 90)

pixels[89] = (255, 0, 0)
