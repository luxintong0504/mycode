import pygame,sys,random
from pygame.locals import *

BLACK = (0,0,0)
BLUE = (10,0,225)
WHITE = (255,255,255)
YELLOW = (250,250,0)

FPS = 28

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
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-4,4)
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10 or \
                self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:    
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((8,14))
        self.image.fill(YELLOW)
        self .rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
   
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
pygame.init()
screen = pygame.display.set_mode((480,700))

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#def fun_c(r1,r2):
#    if r1.left > r2.right or r1.right < r2.left:
#        return False
#    if r1.top > r2.bottom or r1.bottom < r2.top:
#        return False
#    return True;

ms = [ ]
for i in range(10):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m) 
    ms.append(m)

clock = pygame.time.Clock()

running = True
while running:
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
        
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.shoot()

    player.update()
    
    screen.fill(BLACK)
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player,mobs,False) 
    if hits: running = False
    hits = pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    #for m in ms:
    #    if fun_c(m.rect,player.rect):
    #        sys.exit()

    all_sprites.draw(screen)
    
    pygame.display.flip()
    		
