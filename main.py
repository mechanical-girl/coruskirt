import machine
#import emulator.emulator as neopixel
import neopixel
import time

np0 = neopixel.NeoPixel(machine.Pin(0), 3)
np2 = neopixel.NeoPixel(machine.Pin(2), 3)
np4 = neopixel.NeoPixel(machine.Pin(4), 3)
np6 = neopixel.NeoPixel(machine.Pin(6), 3)

np0[0] = (255,0,0)
np0[1] = (0, 255, 0)
np0[2] = (0, 0, 255)
np2[0] = (255,0,0)
np2[1] = (0, 255, 0)
np2[2] = (0, 0, 255)
np4[0] = (255,0,0)
np4[1] = (0, 255, 0)
np4[2] = (0, 0, 255)
np6[0] = (255,0,0)
np6[1] = (0, 255, 0)
np6[2] = (0, 0, 255)

np0.write()
np2.write()
np4.write()
np6.write()

while True:
    time.sleep(1000)
    
    np0.write()
    np2.write()
    np4.write()
    np6.write()
