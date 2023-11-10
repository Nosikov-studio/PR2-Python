import pygame
import math

pygame.init()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("MyCardioid")
clock = pygame.time.Clock()

radius = 400
num_lines = 200
tr = 400, 400
coeff = 0
n = 0


def arcline(alfa, beta):
    # theta = (2 * math.pi / num_lines)
    #
    #

    x1 = int(radius * math.cos(alfa/180*math.pi))+tr[0]
    y1 = int(radius * math.sin(alfa/180*math.pi))+tr[1]

    x2 = int(radius * math.cos(beta/180*math.pi))+tr[0]
    y2 = int(radius * math.sin(beta/180*math.pi))+tr[1]

    pygame.draw.aaline(screen, 'white', (x1, y1), (x2, y2))
    pygame.display.update()


current_time = 0
keep_going = True
while keep_going:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            keep_going = False

    time = pygame.time.get_ticks()

    radius = 300
    # factor = 1 + 0.0001 * time

    if n == 360:
        n = 0
        coeff += 1
        screen.fill('black')

    arcline(n, n*coeff)
    arcline(n, n*(coeff-1))

    n += 1

    clock.tick(60)

    #
