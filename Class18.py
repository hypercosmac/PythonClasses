import pygame

pygame.init()
pygame.font.init()

width, height = 64*16,64*9
screen = pygame.display.set_mode((width,height))
#icon_x,icon_y = (screen.get_rect().center)


rect1 = pygame.Rect(*screen.get_rect().center, 0,0).inflate(100,100)
rect2 = pygame.Rect(0,0,75,75)
#icon = pygame.image.load("hero.png")

while True:
    screen.fill((0,0,100))
    #screen.blit(icon,(icon_x,icon_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    
    rect2.center = pygame.mouse.get_pos()
    collide = rect1.colliderect(rect2)
    color = (250,0,0) if collide else (255,255,255)
    pygame.draw.rect(screen,color,rect1)
    pygame.draw.rect(screen,(0,255,0),rect2,4,1)
    pygame.display.flip()  
