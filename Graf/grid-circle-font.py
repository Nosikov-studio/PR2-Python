import pygame


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("MyExperiments")

WHITE = (255, 255, 255)
surf = pygame.Surface((500, 500))
surf.fill(WHITE)


myfont = pygame.font.Font("fonts/Roboto-Black.ttf", 72)
text = myfont.render("Hello!", True, "Green")

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

    pygame.draw.circle(surf, "Red", (250, 250), 200)
    pygame.draw.circle(surf, "Blue", (250, 250), 100)

    surf.blit(text, (250, 250))

    clock.tick(1)  # ??????????????
