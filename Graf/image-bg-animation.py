import pygame


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([930, 700])
pygame.display.set_caption("MyExperiments")


icon = pygame.image.load('images/rocket.png')
pygame.display.set_icon(icon)  # иконка для приложения

# pl = pygame.image.load('images/spr/spr1.png')

bg = pygame.image.load('images/bg.jpg')

walk = [
    pygame.image.load('images/spr/spr1.png'),
    pygame.image.load('images/spr/spr2.png'),
    pygame.image.load('images/spr/spr3.png'),
    pygame.image.load('images/spr/spr4.png')
]
plcount = 0
bg_x = 0

bg_sound = pygame.mixer.Sound('sounds/s.mp3')
bg_sound.play()

keep_going = True
while keep_going:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x+930, 0))
    bg_x -= 2

    screen.blit(walk[plcount], (150, 430))
    if plcount == 3:
        plcount = 0
    else:
        plcount += 1
    pygame.display.update()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            keep_going = False

    clock.tick(20)  # количество фреймов в секунду
