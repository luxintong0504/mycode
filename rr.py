import pygame, sys
from pygame.locals import * 

pygame.init()

surface = pygame.display.set_mode((640,480))

pygame.display.set_caption("dudu")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()