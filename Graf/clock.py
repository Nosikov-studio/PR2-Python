import pygame
import math
import datetime

pygame.init()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()
FPS = 50


def cdp(R, theta):
    x = math.cos(2*math.pi*theta/360)*R
    y = math.sin(2*math.pi*theta/360)*R
    return x+400-15, -(y-400)-15


def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        current_time = datetime.datetime.now()
        print(current_time)
        sec = current_time.second

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, 'black', (400, 400), 400, 4)

        # second
        R = 350
        theta = sec*(360/60)
        pygame.draw.line(screen, (0, 0, 0), (400, 400), cdp(R, theta), width=8)
        pygame.display.update()
        clock.tick(FPS)


game()
pygame.quit()
