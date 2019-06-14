import pygame,sys,random
from pygame.locals import *

BLACK = (0,0,0)
BLUE = (10,0,225)
WHITE = (255,255,255)

FPS = 60

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 700
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT-10
        self.speedx = 0
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:    
        	self.rect.left = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1,50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)
mobs = []
for i in range(8):
    m = Mob()
    mobs.append(m)
    
pygame.init()
screen = pygame.display.set_mode((480,700))
player = Player()
mob = Mob()

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
                player.speedx = 8
        if event.type == KEYUP:
            if event.key == K_LEFT:
                player.speedx = 0
            if event.key == K_RIGHT:
                player.speedx = 0
    
    for m in mobs:
        m.update()
    mob.update()
    
    player.update()
    screen.fill(BLACK)
    screen.blit(player.image,player.rect)
    screen.blit(mob.image,mob.rect)
    for m in mobs:
        screen.blit(m.image,m.rect)
    pygame.display.flip()
    		
