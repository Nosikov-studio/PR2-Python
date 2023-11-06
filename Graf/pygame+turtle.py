import pygame
import turtle

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("MyExperiments")

WHITE = (255, 255, 255)
surf = pygame.Surface((500, 500))
surf.fill(WHITE)
h = 0
v = 0

keep_going = True
while keep_going:
    screen.blit(surf, (50, 50))
    pygame.display.update()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            keep_going = False
    for v in range(0, 500, 25):
        pygame.draw.rect(surf, 'Red', (h, v, 25, 25), 1)
    # pygame.time.delay(200)

    if h < 500:
        h += 25

    # ВЫЗЫВАЕТ ОТДЕЛЬНОЕ ОКНО!!!!!!!!
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(360):
        t.pencolor('red')
        t.width(x/100+1)
        t.forward(x)
        t.left(59)

    clock.tick(5)
    # ??????????????
