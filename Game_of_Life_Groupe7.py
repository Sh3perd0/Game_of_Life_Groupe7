import pygame
import random as r

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 1900
hauteur_fenetre = 1020
blanc = (255,255,255)

# Création de la fenêtre
screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("grille_test")



#construire la classe BOB
class Bob:
	def __init__(self, spd, mas, nrgy, case ,pos): #initialisation
		self.scale = mas*50
		load_bob = pygame.image.load("Bob.png")
		self.img_bob = pygame.transform.scale(load_bob,(self.scale,self.scale))
		self.speed = spd
		self.mass = mas
		self.energy = nrgy
		self.position = pos
		screen.blit(self.img_bob, (case[pos][0]-1/2*self.scale, case[pos][1]-3/4*self.scale))
		
	def mouvement(self,rand_pos, scale, case): #fonction pour bouger dans BOB
		load_bob = pygame.image.load("Bob.png")
		img_bob = pygame.transform.scale(load_bob,(scale,scale))
		screen.blit(img_bob, (case[rand_pos][0]-1/2*scale, case[rand_pos][1]-3/4*scale))
		#fenetre.blit(img_bob, (pos_x, pos_y))

			
		


#Construire la classe CUBE 	
class Cube:
	def __init__(self, x_image, y_image, size_cube):
		load_cube = pygame.image.load("cube_img2.png")
		img_cube = pygame.transform.scale(load_cube, (size_cube,size_cube))
		screen.blit(img_cube, (x_image, y_image))


#La Classe Grille est constitué de nb_cell*nb_cell fois la classe Cube
class Grille:
	def __init__(self, nb_cell, size_cube):
		self.case = []
		for y in range(nb_cell):
			for x in range (nb_cell):
				x_range = size_cube/2.8
				y_range = size_cube/5
				x_pos = largeur_fenetre-nb_cell*(size_cube/2)+x*x_range-y*x_range
				y_pos = 100+x*y_range+y*y_range 
				pos_cube = Cube(x_pos, y_pos, size_cube)
				self.case.append([x_pos+1/2*size_cube, y_pos+1/4*size_cube])

def fun_pos_move(position_actuel): #fonction pour savoir dans quelle sens peut aller le Bob
	move = []
	try_top_pos = position_actuel-nb_cell
	try_bot_pos = position_actuel+nb_cell
	try_r_pos = position_actuel+1
	try_l_pos = position_actuel-1
	if try_top_pos>=0:
		move.append(try_top_pos)
	if try_bot_pos<=(nb_cell*nb_cell-1):
		move.append(try_bot_pos)
	if try_r_pos <= (nb_cell*nb_cell-1) and try_r_pos%nb_cell != 0:
		move.append(try_r_pos)
	if try_l_pos >= 0 and position_actuel%nb_cell != 0:
		move.append(try_l_pos)
	return move 
	
#INITIALISATION****************************************

nb_cell = 10 #taille d'un coté de la map
size_cube = 100 #taille des cubes


screen.fill(blanc)
grille = Grille(nb_cell, size_cube)

nb_bob = 4
all_bob = []
for i in range(nb_bob):
	position_bob = (r.randint(0,nb_cell*nb_cell-1))
	bob = Bob(1,r.uniform(0.5,1.5),1,grille.case,position_bob)
	all_bob.append(bob)



pygame.time.delay(500)
pygame.display.flip()

# Boucle principale ***********************************
def main():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #evenement si l'on quitte le jeu
				pygame.quit() 
		        
		screen.fill(blanc)
		grille = Grille(nb_cell, size_cube) #recréation de la grille 
		

		
		for bob in all_bob: #faire agir les BOBS
			mouvement_possible = fun_pos_move(bob.position)
			new_pos = r.choice(mouvement_possible)
			bob.mouvement(new_pos, bob.scale, grille.case)
			bob.position = new_pos
			
			

		
		pygame.time.delay(500)#delay d'attente
		
		pygame.display.flip()

if __name__ == "__main__": #lance le jeu
    main()

