import math
import time

np0_coords = [(90,30), (10,50), (0,0)]
np2_coords = [(25,100), (240, 10), (290, 25)]
np4_coords = [(180,80), (90, 85), (45, 95)]
np6_coords = [(160, 45), (200,40), (310, 45)]

coords = [np0_coords, np2_coords, np4_coords, np6_coords]

def ripple(rgb, np0, np1, np2, np3):
    nps = [np0, np1, np2, np3]
    controller = (190, 35)

    radius = 0

    while True:
        if radius > 250:
            radius = 0
            for i in nps:
                for j in i:
                    j = (0, 0, 0)
                i.write()

        for i, np in enumerate(coords):
            for j, pix in enumerate(np):
                d = math.sqrt((pix[0]-controller[0])**2+(pix[1]-controller[1])**2)
                if d < radius:
                    nps[i][j] = rgb
                else:
                    nps[i][j] = (0,0,0)

            nps[i].write()

        radius += 10
        time.sleep(0.1)

