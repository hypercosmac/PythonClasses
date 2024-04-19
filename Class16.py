import pygame
from pygame.locals import (
    K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT)
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
x,y = 50,50
v,z = 400,300
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True
screen.fill((255,255,255))
image = pygame.image.load(r'intro_ball.gif')
screen.blit(image,(x,y))
surf = pygame.Surface((50,50))
surf.fill((0,0,0))
rect = surf.get_rect()
screen.blit(surf, (v,z))
pygame.draw.line(screen,(0,0,255),(60,100),(260,500))
pygame.draw.circle(screen,(0,255,0),(200,300),(50))
pygame.draw.rect(screen,(255,0,0),(400,200,100,50),20)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                y = y-1
                z = z-1 
            elif event.key == K_DOWN:
                y = y+1
                z = z+1
            elif event.key == K_LEFT:
                x = x-1
                v = v-1
            elif event.key == K_RIGHT:
                x = x+1
                v = v+1    
            screen.blit(image,(x,y))
            screen.blit(surf,(v,z))
        elif event.type == QUIT:
            running = False
        pygame.display.update()

    
    
     
