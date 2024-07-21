import pygame
import time
import json

pixel_pos = [(0, 0), (90, 30), (110, 25), (160, 50), (180, 80), (200, 50), (240, 10), (280, 30), (330, 60), (10, 50), (60, 90), (10, 80)]
np0 = [(0,0), (90,30), (110,25)]
np2 = [(160,50), (180, 80), (200, 50)]
np4 = [(240, 10), (200, 30), (330, 60)]
np6 = [(10, 50), (60, 90), (10, 80)]

hertz = 60

with open("output.json", "r") as f:
    states = json.loads(f.read())

running = True
pygame.init()
screen = pygame.display.set_mode((1820,520))
screen.fill((0, 0, 0))

for pixel in pixel_pos:
    x = pixel[0]*5+10
    y = pixel[1]* 5+10
    pygame.draw.circle(screen, (255,255,255), (x,y), 10)
    pygame.display.update()

clock = pygame.time.Clock()

start_time = time.time()
while True:
    to_delete = 0
    current_time = time.time()-start_time
    
    for state in states:
        if state[0] < current_time:
            to_delete += 1
            if state[1] == 0:
                coords = np0[state[2]]
            elif state[1] == 2:
                coords= np2[state[2]]
            elif state[1] == 4:
                coords = np4[state[2]]
            else:
                coords = np6[state[2]]

            x = coords[0]*5+10
            y = coords[1]*5+10

            pygame.draw.circle(screen, state[3], (x, y), 10)
            pygame.display.update()

    for _ in range(to_delete):
        del(states[0])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass

    clock.tick(hertz)
