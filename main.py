import machine
#import emulator.machine as machine
#import emulator.capture as neopixel
import neopixel
import time
#import ripple
#import sweep
import random

#sleeptime = 1000
sleeptime = 1

np0 = neopixel.NeoPixel(machine.Pin(0), 3)
np2 = neopixel.NeoPixel(machine.Pin(2), 3)
np4 = neopixel.NeoPixel(machine.Pin(4), 3)
np6 = neopixel.NeoPixel(machine.Pin(6), 3)

nps = [np0, np2, np4, np6]

#ripple.trans_ripple((255,255,255), np0, np2, np4, np6)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

blue = (95, 205, 252)
pink = (247, 168, 184)
white = (255,255,255)

colours = [blue, pink, white, pink, blue]

num_of_nps = 4
pix_per_np = 3


for i in range(num_of_nps):
    for j in range(pix_per_np):
        nps[i][j] = random.choice(colours)

np0.write()
np2.write()
np4.write()
np6.write()

while True:
    target = [random.randint(0, num_of_nps-1), random.randint(0, pix_per_np-1)]

    nps[target[0]][target[1]] = random.choice(colours)
    nps[target[0]].write()
    time.sleep(500)
