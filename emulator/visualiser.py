import cairo
import time
import pygame
import math
import sys

np0 = [(90,30), (10,50), (0,0)]
np2 = [(25,100), (240, 10), (290, 25)]
np4 = [(180,80), (90, 85), (45, 95)]
np6 = [(160, 45), (200,40), (310, 45)]

pixels = np0+np2+np4+np6

WIDTH, HEIGHT = 1820, 520

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.scale(WIDTH, HEIGHT)

pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.get_surface()

while True:
    for line in sys.stdin:
        splitline = line.rstrip("\n").split()
        pin = int(splitline[1])
        index = int(splitline[2])
        r = int(splitline[3])/255
        g = int(splitline[4])/255
        b = int(splitline[5])/255
        print(f"{pin}[{index}] ({r},{g},{b})", flush=True)
        if pin == 0:
            coords = np0[index]
        elif pin == 2:
            coords= np2[index]
        elif pin == 4:
            coords = np4[index]
        else:
            coords = np6[index]

        x = coords[0]*5+10
        y = coords[1]*5+10

        ctx.arc(x, y, 10, 0, 2*math.pi)
        ctx.set_source_rgb(r, g, b)
        ctx.fill()

    buf = surface.get_dataa()
    image = pygame.image.frombuffer(buf, (WIDTH, HEIGHT), "RGB")

    screen.blit(image, (0,0))
    pygame.diplay.flip()

    pygame.event.get()
    time.sleep(0.1)
