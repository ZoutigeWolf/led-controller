import sys
import board
import neopixel

LENGTH = 90

pixels = neopixel.NeoPixel(board.D18, LENGTH)


def fill_effect(r, g, b):
    pixels.fill((r, g, b))