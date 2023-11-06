import pygame


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("MyExperiments")

WHITE = (255, 255, 255)
surf = pygame.Surface((500, 500))
surf.fill(WHITE)


keep_going = True
while keep_going:
    screen.blit(surf, (50, 50))
    pygame.display.update()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            keep_going = False
    for st in range(0, 500, 10):
        pygame.draw.line(surf, (0, 125, 255), (0, st), (500, st), width=1)

    for st in range(0, 500, 10):
        pygame.draw.line(surf, (0, 125, 255), (st, 0), (st, 500), width=1)

    clock.tick(10)  # ??????????????
