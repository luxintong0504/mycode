import pygame
from pygame.locals import *

BLACK = (0,0,0)
BLUE = (10,0,225)

FPS = 10

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 700
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom =SCREEN_HEIGHT-10
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx

pygame.init()
screen = pygame.display.set_mode((480,700))
player = Player()

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
    	if event.type == QUIT:
    	    pygame.quit()
    	    sys.exit()
    	if event.type == KEYDOWN:
    	    if event.key == K_LEFT:
    	        player.speedx = -8
    	    if event.key == K_RIGHT:
    	        player.speedx =8

    
    player.update()
    screen.fill(BLACK)
    screen.blit(player.image,player.rect)

    pygame.display.flip()
    		
