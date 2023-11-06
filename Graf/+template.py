import pygame


pygame.init()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()
FPS = 50


def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
        clock.tick(FPS)


game()
pygame.quit()
