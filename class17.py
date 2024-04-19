import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

width,height = 64*10, 64*8
screen = pygame.display.set_mode((width,height))
keys = [False,False,False,False]
player_y = 200
player_x = 200
font = pygame.font.SysFont("calibri.ttf",50)
rect1 = pygame.Rect(0,0,48,48)

player = pygame.image.load("hero.png")
lava = pygame.image.load("candy.png")

while True:
    screen.fill((255,255,0))
    screen.blit(lava,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            elif event.key==K_LEFT:
                keys[1]=False
            elif event.key==K_DOWN:
                keys[2]=False
            elif event.key==K_RIGHT:
                keys[3]=False
    if keys[0]:
        if player_y>0:
            player_y -= 4
    if keys[1]:
        if player_x>0:
            player_x -= 4
    if keys[2]:
        if player_y < height:
            player_y += 4
    if keys[3]:
        if player_x < width:
            player_x += 4
    rect1.center = pygame.mouse.get_pos()
    rect2 = player.get_rect()
    collide = rect2.colliderect(rect1)
    if collide:
        text = font.render("GAME OVER!",True,(255,0,0))
        textRect = text.get_rect()
        textRect.center = (width/2,height/2)
        screen.blit(text,textRect)
        pygame.display.update()
