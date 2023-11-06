import pygame


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("MyExperiments")

WHITE = (255, 255, 255)
surf = pygame.Surface((500, 500))
surf.fill(WHITE)
sth = 0
stv = 0

keep_going = True
while keep_going:
    screen.blit(surf, (50, 50))
    pygame.display.update()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            keep_going = False

    if sth < 500:
        pygame.draw.line(surf, (0, 125, 255), (0, sth), (500, sth), width=1)
        sth += 10

    if stv < 500:
        pygame.draw.line(surf, (0, 125, 255), (stv, 0), (stv, 500), width=1)
        stv += 10

    clock.tick(5)  # ??????????????
