import pygame
pygame.init()

pygame.display.set_mode((1920, 1080), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN)
pygame.display.set_caption("Andrew")
pygame.display.set_icon(pygame.image.load("unnamed.bmp"))

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          exit()

    clock.tick(FPS)