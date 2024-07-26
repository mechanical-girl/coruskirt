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

pixel_colours = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]


for i in range(num_of_nps):
    for j in range(pix_per_np):
        this_choice = random.choice(colours)
        pixel_colours[i][j] = this_choice
        nps[i][j] = this_choice

np0.write()
np2.write()
np4.write()
np6.write()

while True:
    i = random.randint(0, num_of_nps -1)
    j = random.randint(0, pix_per_np -1)
    this_choice = random.choice(colours)

    while this_choice == pixel_colours[i][j]:
        this_choice = random.choice(colours)

    transition = []
    current_colour = pixel_colours[i][j]
    for pct in range(5):
        shade = []
        for c in range(len(current_colour)):
            shade.append(int(current_colour[c]*((100-(20*pct))/100)))
        transition.append(shade)

    for pct in range(5):
        shade = []
        for c in range(len(this_choice)):
            shade.append(int(this_choice[c]*((20*pct)/100)))
        transition.append(shade)

    for shade in transition:
        nps[i][j] = shade
        nps[i].write()
        time.sleep(50)

    pixel_colours[i][j] = this_choice
