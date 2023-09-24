import pygame
from random import *

pygame.init()

screen = pygame.display.set_mode((1000,1000))

running = True

image = pygame.image.load("sheep.png").convert()

image = pygame.transform.scale(image, (50,50))

image_droit = pygame.transform.flip(image, True, False)

image_down=pygame.transform.rotate (image, 90) 

image_UP =  pygame.transform.flip(image_down, False, True)


clock = pygame.time.Clock()

x = 500
y = 500


while running :

    screen.fill((0,0,0))
    screen.blit(image, (x,y))
    pygame.display.flip()

    
    for event in pygame.event.get():
        if pygame.key.get_pressed()[pygame.K_ESCAPE] :
            running = False



    random = randint(1,4)
    time = randint(5,150)


    if random == 1 :
        for i in range(0,time):
            x -= 1
            screen.fill((0,0,0))
            screen.blit(image, (x,y))
            pygame.display.flip()

    if random == 2 :
        for i in range(0,time):
            x += 1
            screen.fill((0,0,0))
            screen.blit(image_droit, (x,y))
            pygame.display.flip()

    if random == 3 :
        for i in range(0,time):
            y -= 1
            screen.fill((0,0,0))
            screen.blit(image_UP, (x,y))
            pygame.display.flip()


    if random == 4 :
        for i in range(0,time):
            y += 1
        
            screen.fill((0,0,0))
            screen.blit(image_down, (x,y))
            pygame.display.flip()


    pygame.time.delay(300)


   
    

pygame.quit()
