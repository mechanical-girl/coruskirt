import pygame
import threading
import queue
import sys

def stdin_reader(stdin_queue):
    while True:
        for line in sys.stdin:
            stdin_queue.put(line)

np0 = [(90,30), (10,50), (0,0)]
np2 = [(25,100), (240, 10), (290, 25)]
np4 = [(180,80), (90, 85), (45, 95)]
np6 = [(160, 45), (200,40), (310, 45)]

running = True
pygame.init()
screen = pygame.display.set_mode((1820,520))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
FPS = 60

pixels = np0+np2+np4+np6

stdin_queue = queue.Queue()
stdin_thread = threading.Thread(target=stdin_reader, args=(stdin_queue,))
stdin_thread.daemon = True
stdin_thread.start()

while True:
    while not stdin_queue.empty():
        line = stdin_queue.get()
        splitline = line.rstrip("\n").split()
        pin = int(splitline[1])
        index = int(splitline[2])
        r = int(splitline[3])
        g = int(splitline[4])
        b = int(splitline[5])
        #print(f"{pin}[{index}] ({r},{g},{b})", flush=True)
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
    clock.tick(FPS)

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
