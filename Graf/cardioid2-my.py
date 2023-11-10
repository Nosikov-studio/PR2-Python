import pygame
import math

pygame.init()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("MyCardioid")

radius = 400
num_lines = 200

tr = screen.get_width() // 2, screen.get_height() // 2
current_time = 0
keep_going = True
while keep_going:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            keep_going = False

    for i in range(num_lines):
        theta = (2 * math.pi / num_lines) * i
        x1 = int(radius * math.cos(theta))+tr[0]
        y1 = int(radius * math.sin(theta))+tr[1]

        x2 = int(radius * math.cos(2*theta))+tr[0]
        y2 = int(radius * math.sin(2*theta))+tr[1]

        pygame.draw.aaline(screen, 'white', (x1, y1), (x2, y2))

        pygame.display.update()

    #
