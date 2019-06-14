import pygame, sys
from pygame.locals import * 

COLOR=(100,50,220)

pygame.init()

surface = pygame.display.set_mode((640,480))

pygame.display.set_caption("dudu")

font1 = pygame.font.Font(None,100)
s = font1.render("Emily",True,COLOR)
rect = s.get_rect()
rect.center = (320,240)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            print("KEYDOWN")
        elif event.type == KEYUP:
            print("KEYUP")
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            print("mm: %d, %d"%(mouse_x,mouse_y))
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x,mouse_y = event.pos
            print("md: %d, %d"%(mouse_x,mouse_y))
        elif event.type == MOUSEBUTTONUP:
            mouse_x,mouse_y = event.pos
            print("mu: %d, %d"%(mouse_x,mouse_y))
            

    
    surface.fill((0,0,0))
    surface.blit(s, rect)
    pygame.draw.polygon(surface,COLOR,((320,166),(336,150),(320,134),(304,150)))
    pygame.draw.polygon(surface,COLOR,((320,346),(336,330),(320,314),(304,330)))
    pygame.draw.circle(surface,COLOR,(320,150),30,2)
    pygame.draw.circle(surface,COLOR,(320,330),30,2)
    pygame.display.update()