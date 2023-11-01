import pygame
from random import randint
from math import pi


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("MyExperiments")
x = 0
y = 0
n = 0
# load the fonts
font = pygame.font.SysFont("Times new Roman", 72)
# Render the text in new surface
text = font.render("Hello, Pygame", True, (158, 16, 16))
# **************************************
RED = (255, 0, 0)
hero = pygame.Surface((100, 100))
hero.fill(RED)
# **************************************
WHITE = (255, 255, 255)
surf = pygame.Surface((150, 150))
surf.fill(WHITE)

# **************************************
keep_going = True
while keep_going:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            keep_going = False       # альтернатива sys.exit()
    # цвет экрана
    screen.fill((255, 0, 0))
    # цвет экрана - другой вариант
    screen.fill(pygame.Color('yellow'))
    # цвет экрана случайный
    screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    # круг
    pygame.draw.circle(screen, (0, 255, 0), (100, 200), 20)

    pygame.draw.circle(screen, (0, 0, 255), (x, y), 20)

    x += 3
    pygame.draw.circle(screen, (0, 0, 255), (200, 100), 20, 10)
    # эллипс
    pygame.draw.ellipse(screen, (0, 255, 0), (300, 500, 100, 75))

    # эллиптическая дуга
    pygame.draw.arc(screen, (0, 0, 0), [210, 75, 150, 125], 0, pi / 2, 2)

    # полигон
    pygame.draw.polygon(screen, (0, 255, 0), [[350, 300], [
                        280, 250], [500, 300], [600, 450]])
    # прямоугольник - передача экземпляра класса Rect
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))

    # прямоугольник
    pygame.draw.rect(screen, (255, 255, 255), (200, 200, 100, 75))
    pygame.draw.rect(screen, (255, 255, 255), (500, 300, 100, 75), 8)
    pygame.draw.rect(screen, (255, 255, 255), (700, 500, 100, 75))
    # прямая линия
    pygame.draw.line(screen, (0, 125, 255), (10, 10), (550, 300), width=1)
    pygame.draw.line(screen, (255, 0, 0), (0, 400), (n, 400), width=1)
    n += 10
    # прямая линия (сглаженная)
    pygame.draw.aaline(screen, (0, 125, 255), (20, 70), (300, 55))

    # ломанная линия (False - не замыкать)
    pygame.draw.lines(screen, (0, 0, 0), False, [
                      [0, 300], [50, 350], [200, 150], [220, 30]], 5)

    # текст
    screen.blit(text, (320 - text.get_width() //
                2, 240 - text.get_height() // 2))
    screen.blit(text, (300, 300))

    screen.blit(hero, (590, 100))  #
    screen.blit(surf, (500, 20))  #
    pygame.display.update()

    clock.tick(1)
