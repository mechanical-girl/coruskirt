import machine, neopixel
import time


rpwm = machine.PWM(machine.Pin(18)) # RED
gpwm = machine.PWM(machine.Pin(19)) # GREEN
bpwm = machine.PWM(machine.Pin(20)) # BLUE

np0 = neopixel.NeoPixel(machine.Pin(0), 1)

rpwm.freq(1000)
gpwm.freq(1000)
bpwm.freq(1000)

rduty = 0
gduty = 65535
bduty = 65535

np0[0] = (255,0,0)
#np0[0] = (0, 255, 0)
#np0[2] = (0, 0, 255)

np0.write()
rpwm.duty_u16(rduty)
gpwm.duty_u16(gduty)
bpwm.duty_u16(bduty)


while True:
    time.sleep(1)
    
    np0.write()