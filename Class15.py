import pygame
pygame.font.init()
display_surface = pygame.display.set_mode((700,500))
pygame.display.set_caption("Pygame Exploration")

font1 = pygame.font.SysFont("calibri.ttf",50)
font2 = pygame.font.SysFont("calibri.ttf",30)

text1 = font1.render("Hello!",True,(0,255,0))
text2 = font2.render("My Pygame text",True, (0,255,0))

textRect1 = text1.get_rect()
textRect2 =  text2.get_rect()

textRect1.center = (350,400)
textRect2.center = (350,440)

image = pygame.image.load(r'comp.webp')
image2 = pygame.image.load(r'comp.webp')

image = pygame.transform.scale(image,(300,225))
image2 = pygame.transform.scale(image,(300,225))

image = pygame.transform.flip(image,True,False)
while True:
    display_surface.fill((255,115,0))
    display_surface.blit(text1,textRect1)
    display_surface.blit(text2,textRect2)

    display_surface.blit(image,(50,50))
    display_surface.blit(image2,(349,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
    
                         
