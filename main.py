import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 150)

for i in range(150):
    pixels[i] = (255, 0, 0)
    print(i)
    time.sleep(0.5)
