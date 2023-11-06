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

keep_going = True
while keep_going:
    screen.blit(surf, (50, 50))

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            keep_going = False

    if v <= 500:  # Проверяем не закончили-ли мы
        pygame.draw.rect(surf, 'Red', (h, v, 25, 25), 1)

        pygame.display.flip()

        if h < 500:
            h += 25  # Увеличиваем координату по x
        else:
            h = 0  # Обнуляем x-координату
            v += 25  # Увеличиваем координату по y

    clock.tick(25)
