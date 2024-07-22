import pygame
import sys

np0 = [(0,0), (90,30), (110,25)]
np2 = [(160,50), (180, 80), (200, 50)]
np4 = [(240, 10), (200, 30), (330, 60)]
np6 = [(10, 50), (60, 90), (10, 80)]

running = True
pygame.init()
screen = pygame.display.set_mode((1820,520))
screen.fill((0, 0, 0))

pixels = np0+np2+np4+np6

for pixel in pixels:
    x = pixel[0]*5+10
    y = pixel[1]* 5+10
    pygame.draw.circle(screen, (255,255,255), (x,y), 10)
    pygame.display.update()

while True:
    for line in sys.stdin:
        splitline = line.rstrip("\n").split()
        pin = int(splitline[1])
        index = int(splitline[2])
        r = int(splitline[3])
        g = int(splitline[4])
        b = int(splitline[5])
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

        pygame.draw.circle(screen, (r, g, b), (x, y), 10)
        pygame.display.update()
