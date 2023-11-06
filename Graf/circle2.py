import pygame
import sys
from math import *


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("MyExperiments")


r = 100
theta = 0
center = [150, 150]

WHITE = (255, 255, 255)
surf = pygame.Surface((500, 500))
surf.fill(WHITE)
surf2 = pygame.Surface((300, 300))
surf2.fill("Yellow")
surf2.set_alpha(50)

i = 0
x = 0
keep_going = True
while keep_going:

    screen.blit(surf, (50, 50))
    surf.blit(surf2, (50, 50))
    surf2.fill('Yellow')
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.display.flip()

    if i <= 10:
        pygame.draw.line(surf, (0, 125, 255), (0, 500), (x, 0), width=1)

    if (i > 10 and i <= 20):
        pygame.draw.line(surf, (0, 125, 255), (0, 500), (500, y), width=1)

    if (i > 20 and i <= 30):
        pygame.draw.line(surf, (0, 125, 255), (500, 500), (500-x, 0), width=1)

    if (i > 30 and i <= 40):
        pygame.draw.line(surf, (0, 125, 255), (500, 500), (0, y), width=1)

    i += 1
    x = 50*(i % 10)
    y = 50*(i % 10)

    xc = center[0]+r*cos(theta)
    yc = center[1]+r*sin(theta)

    xc2 = 400+r*cos(theta)
    yc2 = 400+r*sin(theta)

    pygame.draw.circle(surf2, 'black', center, r, width=1)
    pygame.draw.circle(surf2, 'red', (xc, yc), 8)
    pygame.draw.circle(surf, 'green', (xc2, yc2), 10)

    theta += 0.1

    clock.tick(25)
