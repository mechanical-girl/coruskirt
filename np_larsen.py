#import machine, neopixel
import time



np0 = [0, 0, 0]
np1 = [0, 0, 0]

#np0 = neopixel.NeoPixel(machine.Pin(0), 3)
#np1 = neopixel.NeoPixel(machine.Pin(1), 3)


larsen_order = [np0[2], np0[1], np0[0], np1[0], np1[1], np1[2]]
larsen_index = 0
larsen_increasing = True

frequency = 10

while True:
    for m, pixel in enumerate(larsen_order):
        if m == larsen_index:
            pixel = 1
            #pixel.write(255, 0, 0)
        else:
            pixel = 0
            #pixel.write(0, 0, 0)
        
        print(pixel, end='')
    print()
    
    if larsen_index == len(larsen_order)-1:
        larsen_increasing = False
    elif larsen_index == 0:
        larsen_increasing = True
    
    if larsen_increasing:
        larsen_index += 1
    else:
        larsen_index -= 1
        
            
    time.sleep(1/frequency)