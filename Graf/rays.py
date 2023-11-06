import pygame


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("MyExperiments")

WHITE = (255, 255, 255)
surf = pygame.Surface((500, 500))
surf.fill(WHITE)
i = 0
x = 0
keep_going = True
while keep_going:
    screen.blit(surf, (50, 50))

    for event in pygame.event.get():
        print(event)
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

    clock.tick(25)
