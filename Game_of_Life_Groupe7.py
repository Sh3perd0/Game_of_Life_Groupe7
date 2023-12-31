import pygame
from random import randint
x=500
y=360
i=0
dimension_x=1280
dimension_y=700
pygame.init() #init de pygame
screen=pygame.display.set_mode((dimension_x,dimension_y)) #taille screen pygame
clock=pygame.time.Clock() #setup d'une clock
running=True #elle est active

class Bob: #classe blobs qui def leur caracteristiques
    def __init__(self,speed,mass,energy,perception):
        self.size=mass*136
        self.speed=speed
        self.mass=mass
        self.energy=energy
        self.perception=perception
        self.load_bob_sprite = pygame.image.load("bob.png")
        self.img_bob = pygame.transform.scale(self.load_bob_sprite,(self.size,self.size))
        
        
        


    def position(pos):
        pass

        








#text_font = pygame.font.SysFont("Times New Roman",30)


#def draw_text(text,font,text_col,x,y): #fonction qui affiche du texte
   # img=font.render(text,True,text_col)
   # screen.blit(img,(x,y))

time=150#var arbitraire du randint de deplacement

bob_1=Bob(1,1,1,1)
hauteur=bob_1.img_bob.get_height()
largeur=bob_1.img_bob.get_width()
print(hauteur,largeur)
while running:
    random=randint(1,4)

    screen.fill((0,0,0)) #permet de colorer le screen en noir ,afin de ne pas laisser de traces lors d'un déplacement par exemple #dessin du rectangle
    key = pygame.key.get_pressed() #réagit à une touche préssée
    if random==1: #ici q veut dire on presse la touche q
        for i in range(0,randint(20,time)):
            if x>0+largeur:
                x=x-1
                screen.fill((0,0,0))
                screen.blit(bob_1.img_bob,(x,y)) #-1 correspond à un déplacement négatif en x, 0 un déplacment nul en y
                pygame.display.flip()
            else:
                break
    elif random==2:#à noter que la base est telle que x standart mais y vers le bas
        for i in range(0,randint(20,time)):
            if x<dimension_x-largeur:
                x=x+1
                screen.fill((0,0,0))
                screen.blit(bob_1.img_bob,(x,y))
                pygame.display.flip()
            else:
                 break
    elif random==3:
        for i in range(0,randint(20,time)):
            if y>0+hauteur:
                y=y-1
                screen.fill((0,0,0))
                screen.blit(bob_1.img_bob,(x,y))
                pygame.display.flip()
            else:
                break
    elif random==4:
      
        for i in range(0,randint(20,time)):
            if y<dimension_y-hauteur:
                y=y+1
                screen.fill((0,0,0))
                screen.blit(bob_1.img_bob,(x,y))
                pygame.display.flip()
            else:
                break

    pygame.time.delay(1200)#délai avant actualisation
    pygame.display.flip()#affiche au screen
    
    




    for event in pygame.event.get():
        if key[pygame.K_ESCAPE]:
            running=False#ferme l'interface graphique si echap est appuyé
    pygame.display.update()

    


pygame.quit()














