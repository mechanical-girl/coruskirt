import pygame

print("hello, world")

class neopixel:
    def __init__(self):
        self.window = 1000

        self.np_radius = 10
        self.pixel_pos = [(0, 0), (90, 30), (110, 25), (160, 50), (180, 80), (200, 50), (240, 10), (280, 30), (330, 60), (10, 50), (60, 90), (10, 80)]

        pygame.init()
        self.screen = pygame.display.set_mode((1800, 500))
        self.screen.fill((0, 0, 0))

        for pixel in self.pixel_pos:
            x = pixel[0]*5
            y = pixel[1]*5
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), self.np_radius)

        pygame.display.update()

