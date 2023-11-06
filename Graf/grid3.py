import pygame


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("MyExperiments")

WHITE = (255, 255, 255)
surf = pygame.Surface((500, 500))
surf.fill(WHITE)
h = 0
v = 0
i = 0
m = 20
n = 20
imax = m*n
current_time = 0
keep_going = True
while keep_going:
    screen.blit(surf, (50, 50))

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            keep_going = False

    current_time = pygame.time.get_ticks()
    # print(current_time)

    if (i <= imax):
        pygame.draw.rect(surf, 'Red', (h, v, 25, 25), 1)

        pygame.display.flip()

        clock.tick(25)
        i += 1
        h = (i//20)*25
        v = (i % 20)*25

    # ??????????????
