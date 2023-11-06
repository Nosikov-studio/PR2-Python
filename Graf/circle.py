import pygame
import sys
from math import *


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("MyExperiments-Circle")

WHITE = (255, 255, 255)
# surf = pygame.Surface((500, 500))
# surf.fill(WHITE)
i = 0
x = 0

r = 100
theta = 0
center = [150, 300]
keep_going = True
while keep_going:
    # screen.blit(surf, (50, 50))
    screen.fill([50, 100, 150])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    x = center[0]+r*cos(theta)
    y = center[1]+r*sin(theta)

    pygame.draw.circle(screen, 'black', center, r, width=1)
    pygame.draw.circle(screen, 'orange', (x, y), 8)

    theta += 0.1
    # pygame.display.update()
    pygame.display.flip()
    clock.tick(10)
