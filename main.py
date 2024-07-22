#import machine
import emulator.machine as machine
import emulator.capture as neopixel
#import neopixel
import time
#from ripple import ripple

#sleeptime = 1000
sleeptime = 1

np0 = neopixel.NeoPixel(machine.Pin(0), 3)
np2 = neopixel.NeoPixel(machine.Pin(2), 3)
np4 = neopixel.NeoPixel(machine.Pin(4), 3)
np6 = neopixel.NeoPixel(machine.Pin(6), 3)

#ripple((255,255,255), np0, np2, np4, np6)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

np0.write()
np2.write()
np4.write()
np6.write()

while True:
    time.sleep(sleeptime)
    
    np0[0] = red
    np0[1] = green
    np0[2] = blue
    np2[0] = red
    np2[1] = green
    np2[2] = blue
    np4[0] = red
    np4[1] = green
    np4[2] = blue
    np6[0] = red
    np6[1] = green
    np6[2] = blue
    np0.write()
    np2.write()
    np4.write()
    np6.write()
    
    time.sleep(sleeptime)
    
    np0[1] = red
    np0[2] = green
    np0[0] = blue
    np2[1] = red
    np2[2] = green
    np2[0] = blue
    np4[1] = red
    np4[2] = green
    np4[0] = blue
    np6[1] = red
    np6[2] = green
    np6[0] = blue
    np0.write()
    np2.write()
    np4.write()
    np6.write()
    
    time.sleep(sleeptime)
    
    np0[2] = red
    np0[0] = green
    np0[1] = blue
    np2[2] = red
    np2[0] = green
    np2[1] = blue
    np4[2] = red
    np4[0] = green
    np4[1] = blue
    np6[2] = red
    np6[0] = green
    np6[1] = blue
    np0.write()
    np2.write()
    np4.write()
    np6.write()
    
