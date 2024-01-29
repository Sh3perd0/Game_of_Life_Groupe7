#bibliothèques

import pygame
import sys
from settings import Settings
import os
import json
#import constant.settings as sett

#import main

#sys.path.insert(0, 'C:/Users/d3velopp/Documents/Python/Game_Of_Life/Game_of_Life_Groupe7')
pygame.init()
pygame.font.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialisation de Pygame

#pour sortir a la fin
doonce = True

# Paramètres par défaut de la résolution de la fenêtre
default_width = 1920
default_height = 1080

#Paramètres par défaut de la résolution de l'image actuelle
default_width_image = 1920
default_height_image = 1080

#ajouter chaque chemin d'image ici
image_paths = ["image_premier_plan_0.png","image_premier_plan_1.png","start_menu_0.png", "start_menu_1.png", "how_to_play.png", "Bob_number.png", "Volume.png", "music_choice.png", "graphical_settings.png", "skin_choice_settings.png","Food_number.png","Tick_number.png","default_energy.png","loose_of_energy.png","Reproducing_energy.png","_newborn_energy_parth.png","max_energy.png","default_speed.png","default_perception.png","default_mass.png","default_memory.png","max_framerate.png","_newborn_energy_sexual.png","gridsize.png"]
skin_paths_1 =["blue_fallguy.png","purple_fallguy.png","green_fallguy.png"]
skin_paths_2=["blue_stickman.png","purple_stickman.png","green_stickman.png"]
skin_paths_3=["pink_amogus.png","green_amogus.png","red_amogus.png"]
default_set_skin = skin_paths_1

set_skin_choisis=default_set_skin

#taille de l'écran
screen_width = default_width
screen_height = default_height

#résolution de la fenetre actuelle
current_res_x=default_width
current_res_y=default_height

# Création de la fenêtre
screen = pygame.display.set_mode((current_res_x, current_res_y))
pygame.display.set_caption("Game of Life")

image_premier_plan_settings = Settings(0, 0, 0, 0, (255, 255, 0),"image_premier_plan_0.png",(default_width_image,default_height_image))
main_menu_settings = Settings(current_res_x // 2 - 200, current_res_y // 2 + 100, 400, 100, (255, 255, 0),"start_menu_0.png", (default_width_image,default_height_image))
how_to_play_settings = Settings(current_res_x // 2 - 450, current_res_y // 2, 0, 0, (255, 255, 0), "how_to_play.png" , (default_width_image,default_height_image))
bob_number_settings = Settings(current_res_x // 2 - 418, current_res_y // 2 + 161, 850, 155, (255, 255, 0), "Bob_number.png" , (default_width_image,default_height_image))
volume_settings = Settings(current_res_x // 2 - 418, current_res_y // 2 + 161, 850, 155, (255, 255, 0), "Volume.png", (default_width_image,default_height_image))
music_settings = Settings(current_res_x *0.0703 , current_res_y *  0.63 , 485, 155, (255, 255, 0), "music_choice.png", (default_width_image,default_height_image))
#graphical_settings = Settings(current_res_x*0.0703 , current_res_y *  0.63 , 0, 0, (255, 255, 0), "graphical_settings.png", (default_width_image,default_height_image))
#resolution_settings = Settings(current_res_x // 2 - 418, current_res_y // 2 + 161, 850, 155, (255, 255, 0), "resolution.png", (default_width_image,default_height_image))
skin_choice_settings = Settings(current_res_x *0.11 , current_res_y *  0.63 , 485, 155, (255, 255, 0), "skin_choice_settings.png",(default_width_image,default_height_image))

food_number_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "Food_number.png" , (default_width_image,default_height_image))
tick_number_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "Tick_number.png" , (default_width_image,default_height_image))
default_energy_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "default_energy.png" , (default_width_image,default_height_image))
loose_of_energy_repr_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "loose_of_energy_repr.png" , (default_width_image,default_height_image))
reproducing_energy_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "Reproducing_energy.png" , (default_width_image,default_height_image))
newborn_energy_parth_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "_newborn_energy_parth.png" , (default_width_image,default_height_image))
max_energy_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "max_energy.png" , (default_width_image,default_height_image))
default_speed_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "default_speed.png" , (default_width_image,default_height_image))
default_perception_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "default_perception.png" , (default_width_image,default_height_image))
default_mass_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "default_mass.png" , (default_width_image,default_height_image))
default_memory_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "default_memory.png" , (default_width_image,default_height_image))
max_framerate_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "max_framerate.png" , (default_width_image,default_height_image))
newborn_energy_sexual_settings = Settings(current_res_x // 2 - 423, current_res_y // 2 + 130, 820, 155, (255, 255, 0), "_newborn_energy_sexual.png" , (default_width_image,default_height_image))
map_settings = Settings(current_res_x // 2 - 410, current_res_y // 2 + 140, 820, 155, (255, 255, 0), "gridsize.png" , (default_width_image,default_height_image))



# Initialisation des variables d'état
selection = 0
running = True
image_premier_plan_settings_displayed = False
bob_number_settings_displayed = False
music_settings_displayed=False
volume_settings_displayed =False
graphical_settings_displayed =False
resolution_settings_displayed=False   #resolutions 
skin_choice_displayed = False
default_energy_settings_displayed = False
default_mass_settings_displayed = False
default_memory_settings_displayed = False
default_perception_settings_displayed = False
default_speed_settings_displayed = False
food_number_settings_displayed = False
loose_of_energy_repr_settings_displayed = False
max_energy_settings_displayed = False
max_framerate_settings_displayed = False
newborn_energy_parth_settings_displayed = False
newborn_energy_sexual_settings_displayed = False
reproducing_energy_settings_displayed = False
tick_number_settings_displayed = False
map_settings_displayed = False

last_cursor_position = None
mainmenu_settings_displayed = False
how_to_play_settings_displayed = False
dragging_bob_number = False
dragging_volume=False
dragging_newborn_energy_parth= False
dragging_newborn_energy_sexual = False
dragging_default_energy = False
dragging_default_mass = False
dragging_default_memory = False
dragging_default_perception = False
dragging_default_speed = False
dragging_food_number = False
dragging_loose_of_energy_repr = False
dragging_max_energy = False
dragging_max_framerate = False
dragging_reproducing_energy = False
dragging_tick_number = False
dragging_map = False
enter_pressed = False
escape_pressed = False
scaled_image=None

# Paramètres des sliders
slider_length = 400
slider_height = 10

slider_x_newborn_energy_parth = int((screen_width - slider_length) / 2)
slider_y_newborn_energy_parth = int(screen_height / 2) + 235

slider_x_map = int((screen_width - slider_length) / 2)
slider_y_map= int(screen_height / 2) + 235

slider_x_newborn_energy_sexual = int((screen_width - slider_length) / 2)
slider_y_newborn_energy_sexual = int(screen_height / 2) + 235

slider_x_default_energy = int((screen_width - slider_length) / 2)
slider_y_default_energy = int(screen_height / 2) + 235

slider_x_default_mass = int((screen_width - slider_length) / 2)
slider_y_default_mass = int(screen_height / 2) + 235

slider_x_default_memory = int((screen_width - slider_length) / 2)
slider_y_default_memory = int(screen_height / 2) + 235

slider_x_default_perception = int((screen_width - slider_length) / 2)
slider_y_default_perception = int(screen_height / 2) + 235

slider_x_default_speed = int((screen_width - slider_length) / 2)
slider_y_default_speed = int(screen_height / 2) + 235

slider_x_food_number = int((screen_width - slider_length) / 2)
slider_y_food_number = int(screen_height / 2) + 235

slider_x_loose_of_energy_repr = int((screen_width - slider_length) / 2)
slider_y_loose_of_energy_repr = int(screen_height / 2) + 235

slider_x_max_energy = int((screen_width - slider_length) / 2)
slider_y_max_energy = int(screen_height / 2) + 235

slider_x_max_framerate = int((screen_width - slider_length) / 2)
slider_y_max_framerate = int(screen_height / 2) + 235

slider_x_reproducing_energy = int((screen_width - slider_length) / 2)
slider_y_reproducing_energy = int(screen_height / 2) + 235

slider_x_tick_number = int((screen_width - slider_length) / 2)
slider_y_tick_number = int(screen_height / 2) + 235

slider_x_bob = int((screen_width - slider_length) / 2)
slider_y_bob = int(screen_height / 2) + 235

slider_x_volume = int((screen_width - slider_length) / 2)
slider_y_volume = int(screen_height / 2) + 235

###VALEURS DE BASES POUR CHAQUE PARAMETRE
###CE NE SONT PAS DES VALEURS AU HASARD MAIS LES VALEURS DE BASE ENONCEES DANS LE SUJET.

min_value = 0 #valeur minimale pour les sliders
max_value = 500
current_value_bob = 1 #valeur courante de bob choisi avec le slider bob_number
current_volume=100 #valeur courante pour le volume choisi avec le slider volume
current_newborn_energy_parth=int(50)
current_newborn_energy_sexual=100
current_default_energy=100
current_default_mass=1
current_default_memory=1
current_default_perception=1
current_default_speed=1
current_food_number=400
current_loose_of_energy_repr=100
current_max_energy=200
current_max_framerate=60
current_reproducing_energy=150
current_tick_number=100
current_map=10


cursor_offset_y = -5
global_cursor_position_bob = int((screen_width - slider_length) / 2)
global_cursor_position_volume = int((screen_width - slider_length) / 2)
global_cursor_position_newborn_energy_parth = int((screen_width - slider_length) / 2)
global_cursor_position_newborn_energy_sexual = int((screen_width - slider_length) / 2)
global_cursor_position_default_energy = int((screen_width - slider_length) / 2)
global_cursor_position_default_mass = int((screen_width - slider_length) / 2)
global_cursor_position_default_memory = int((screen_width - slider_length) / 2)
global_cursor_position_default_perception = int((screen_width - slider_length) / 2)
global_cursor_position_default_speed = int((screen_width - slider_length) / 2)
global_cursor_position_food_number = int((screen_width - slider_length) / 2)
global_cursor_position_loose_of_energy_repr = int((screen_width - slider_length) / 2)
global_cursor_position_max_energy = int((screen_width - slider_length) / 2)
global_cursor_position_max_framerate = int((screen_width - slider_length) / 2)
global_cursor_position_reproducing_energy = int((screen_width - slider_length) / 2)
global_cursor_position_tick_number = int((screen_width - slider_length) / 2)
global_cursor_position_map= int((screen_width - slider_length) / 2)




#autres variables

cursor_x_bob=0
cursor_x_volume=0
cursor_x_newborn_energy_parth=0
cursor_x_newborn_energy_sexual=0
cursor_x_default_energy=0
cursor_x_default_mass=0
cursor_x_default_memory=0
cursor_x_default_perception=0
cursor_x_default_speed=0
cursor_x_food_number=0
cursor_x_loose_of_energy_repr=0
cursor_x_max_energy=0
cursor_x_max_framerate=0
cursor_x_reproducing_energy=0
cursor_x_tick_number=0
cursor_x_map=0

cursor_position=0
global_cursor_position_bob=slider_x_bob
global_cursor_position_volume=slider_x_volume
global_cursor_position_newborn_energy_parth=slider_x_newborn_energy_parth
global_cursor_position_newborn_energy_sexual=slider_x_newborn_energy_sexual
global_cursor_position_default_energy=slider_x_default_energy
global_cursor_position_default_mass=slider_x_default_mass
global_cursor_position_default_memory=slider_x_default_memory
global_cursor_position_default_perception=slider_x_default_perception
global_cursor_position_default_speed=slider_x_default_speed
global_cursor_position_food_number=slider_x_food_number
global_cursor_position_loose_of_energy_repr=slider_x_loose_of_energy_repr
global_cursor_position_max_energy=slider_x_max_energy
global_cursor_position_max_framerate=slider_x_max_framerate
global_cursor_position_reproducing_energy=slider_x_reproducing_energy
global_cursor_position_tick_number=slider_x_tick_number
global_cursor_position_map=slider_x_map

current_settings = image_premier_plan_settings #premiere page de settings, et également définie comme la courante
animation_speed = 2 #vitesse animation 
switch_interval = 500 #vitesse de switch 
last_switch_time = pygame.time.get_ticks() #get tick depuis le dernier switch

#font_msg_path = os.path.join("", "font", "menu/font/SpaceMono-Regular.ttf") 
#chemin de la police de base
font_msg_path = "SpaceMono-Regular.ttf"
font_msg = pygame.font.Font(font_msg_path, 20) #taille police de base 

font_slider_bob = pygame.font.Font(font_msg_path, 25)
font_slider_volume = pygame.font.Font(font_msg_path, 25)
font_slider_newborn_energy_parth=pygame.font.Font(font_msg_path, 25)
font_slider_newborn_energy_sexual=font_slider_volume
font_slider_default_energy=font_slider_volume
font_slider_default_mass=font_slider_volume
font_slider_default_memory=font_slider_volume
font_slider_default_perception=font_slider_volume
font_slider_default_speed=font_slider_volume
font_slider_food_number=font_slider_volume
font_slider_loose_of_energy_repr=font_slider_volume
font_slider_max_energy=font_slider_volume
font_slider_max_framerate=font_slider_volume
font_slider_reproducing_energy=font_slider_volume
font_slider_tick_number=font_slider_volume
font_slider_map=font_slider_volume

#texte affiché sur les parametres hors main menu
text_surface_settings = font_msg.render("Entrée : Choisir    Echap : Retour", True, (255, 255, 0))
text_hitbox_settings = text_surface_settings.get_rect(topleft=(200, 105))

#texte affiché sur le main menu
text_surface_main_menu = font_msg.render("Entrée : Choisir    Echap : Quitter le jeu", True, (255, 255, 0))
text_hitbox_main_menu = text_surface_main_menu.get_rect(topleft=(200, 105))

text_credits = font_msg.render("Made by Thomas, Lucien, Quyen, Quynh, Abrouk and Leopold ", True, (255, 255, 0))
text_hitbox_credits = text_credits.get_rect(topright=(1733, 105))

#musiques possibles
music_left = pygame.mixer.Sound("_deep_in_the_Chimney.mp3")
music_middle = pygame.mixer.Sound("_go Green.mp3")
music_right = pygame.mixer.Sound("_ninja Skills.mp3")
music_choice=music_left


#fonctions de slider attention les yeux y'a plein d'instances de ce slider, pour autant de paramètres ajustables !
def update_slider_position_bob():
    global current_value_bob
    #cette variable est la position calculée du curseur en fonction de la valeur de bob_number
    cursor_position_bob = slider_x_bob + (current_value_bob / max_value) * slider_length - 5
    #cette variable est la position du curseur en temps réel
    cursor_x_bob = max(min(cursor_position_bob - slider_x_bob, slider_length - 10), 0)
    return slider_x_bob + cursor_x_bob 

def update_slider_position_volume():
    global current_volume
    cursor_position_volume = slider_x_volume + (current_volume / max_value) * slider_length - 5
    cursor_x_volume = max(min(cursor_position_volume - slider_x_volume, slider_length - 10), 0)
    return slider_x_volume + cursor_x_volume

def update_slider_position_map():
    global current_map
    cursor_position_map = slider_x_map + (current_map/ max_value) * slider_length - 5
    cursor_x_map= max(min(cursor_position_map - slider_x_map, slider_length - 10), 0)
    return slider_x_map + cursor_x_map

def update_slider_position_newborn_energy_parth():
    global current_newborn_energy_parth
    cursor_position_newborn_energy_parth = slider_x_newborn_energy_parth + (current_newborn_energy_parth / max_value) * slider_length - 5
    cursor_x_newborn_energy_parth = max(min(cursor_position_newborn_energy_parth - slider_x_newborn_energy_parth, slider_length - 10), 0)
    return slider_x_newborn_energy_parth + cursor_x_newborn_energy_parth

def update_slider_position_newborn_energy_sexual():
    global current_newborn_energy_sexual
    cursor_position_newborn_energy_sexual = slider_x_newborn_energy_sexual + (current_newborn_energy_sexual / max_value) * slider_length - 5
    cursor_x_newborn_energy_sexual = max(min(cursor_position_newborn_energy_sexual - slider_x_newborn_energy_sexual, slider_length - 10), 0)
    return slider_x_newborn_energy_sexual + cursor_x_newborn_energy_sexual 

def update_slider_position_default_energy():
    global current_default_energy
    cursor_position_default_energy = slider_x_default_energy + (current_default_energy / max_value) * slider_length - 5
    cursor_x_default_energy = max(min(cursor_position_default_energy - slider_x_default_energy, slider_length - 10), 0)
    return slider_x_default_energy + cursor_x_default_energy  

def update_slider_position_default_mass():
    global current_default_mass
    cursor_position_default_mass = slider_x_default_mass + (current_default_mass / max_value) * slider_length - 5
    cursor_x_default_mass = max(min(cursor_position_default_mass - slider_x_default_mass, slider_length - 10), 0)
    return slider_x_default_mass + cursor_x_default_mass

def update_slider_position_default_memory():
    global current_default_memory
    cursor_position_default_memory = slider_x_default_memory + (current_default_memory / max_value) * slider_length - 5
    cursor_x_default_memory = max(min(cursor_position_default_memory - slider_x_volume, slider_length - 10), 0)
    return slider_x_default_memory + cursor_x_default_memory

def update_slider_position_default_perception():
    global current_default_perception
    cursor_position_default_perception = slider_x_default_perception + (current_default_perception / max_value) * slider_length - 5
    cursor_x_default_perception= max(min(cursor_position_default_perception - slider_x_default_perception, slider_length - 10), 0)
    return slider_x_default_perception + cursor_x_default_perception 

def update_slider_position_default_speed():
    global current_default_speed
    cursor_position_default_speed = slider_x_default_speed + (current_default_speed / max_value) * slider_length - 5
    cursor_x_default_speed = max(min(cursor_position_default_speed - slider_x_default_speed, slider_length - 10), 0)
    return slider_x_default_speed + cursor_x_default_speed  

def update_slider_position_food_number():
    global current_food_number
    cursor_position_food_number = slider_x_food_number + (current_food_number / max_value) * slider_length - 5
    cursor_x_food_number = max(min(cursor_position_food_number - slider_x_food_number, slider_length - 10), 0)
    return slider_x_food_number + cursor_x_food_number

def update_slider_position_loose_of_energy_repr():
    global current_loose_of_energy_repr
    cursor_position_loose_of_energy_repr = slider_x_loose_of_energy_repr + (current_loose_of_energy_repr / max_value) * slider_length - 5
    cursor_x_loose_of_energy_repr = max(min(cursor_position_loose_of_energy_repr - slider_x_loose_of_energy_repr, slider_length - 10), 0)
    return slider_x_loose_of_energy_repr + cursor_x_loose_of_energy_repr 

def update_slider_position_max_energy():
    global current_max_energy
    cursor_position_max_energy = slider_x_max_energy + (current_max_energy / max_value) * slider_length - 5
    cursor_x_max_energy = max(min(cursor_position_max_energy - slider_x_max_energy, slider_length - 10), 0)
    return slider_x_max_energy + cursor_x_max_energy

def update_slider_position_max_framerate():
    global current_max_framerate
    cursor_position_max_framerate = slider_x_max_framerate + (current_max_framerate / max_value) * slider_length - 5
    cursor_x_max_framerate = max(min(cursor_position_max_framerate - slider_x_max_framerate, slider_length - 10), 0)
    return slider_x_max_framerate + cursor_x_max_framerate

def update_slider_position_reproducing_energy():
    global current_reproducing_energy
    cursor_position_reproducing_energy = slider_x_reproducing_energy + (current_reproducing_energy / max_value) * slider_length - 5
    cursor_x_reproducing_energy = max(min(cursor_position_reproducing_energy - slider_x_reproducing_energy, slider_length - 10), 0)
    return slider_x_reproducing_energy + cursor_x_reproducing_energy

def update_slider_position_tick_number():
    global current_tick_number
    cursor_position_tick_number = slider_x_tick_number + (current_tick_number / max_value) * slider_length - 5
    cursor_x_tick_number = max(min(cursor_position_tick_number - slider_x_tick_number, slider_length - 10), 0)
    return slider_x_tick_number + cursor_x_tick_number 

    

cursor_x_bob=update_slider_position_bob()
cursor_x_volume=update_slider_position_volume()
cursor_x_newborn_energy_parth=update_slider_position_newborn_energy_parth()
cursor_x_newborn_energy_sexual=update_slider_position_newborn_energy_sexual()
cursor_x_default_energy=update_slider_position_default_energy()
cursor_x_default_mass=update_slider_position_default_mass()
cursor_x_default_memory=update_slider_position_default_memory()
cursor_x_default_perception=update_slider_position_default_perception()
cursor_x_default_speed=update_slider_position_default_speed()
cursor_x_food_number=update_slider_position_food_number()
cursor_x_loose_of_energy_repr=update_slider_position_loose_of_energy_repr()
cursor_x_max_energy=update_slider_position_max_energy()
cursor_x_max_framerate=update_slider_position_max_framerate()
cursor_x_reproducing_energy=update_slider_position_reproducing_energy()
cursor_x_tick_number=update_slider_position_tick_number()
cursor_x_map=update_slider_position_map()
# Redimensionnement de toutes les images


#les deux curseurs des slider
cursor_slider_bob = pygame.Rect(update_slider_position_bob(), slider_y_bob + cursor_offset_y, 10, 20)
cursor_slider_volume = pygame.Rect(update_slider_position_volume(), slider_y_volume + cursor_offset_y, 10, 20)
cursor_slider_newborn_energy_parth = pygame.Rect(update_slider_position_newborn_energy_parth(), slider_y_newborn_energy_parth + cursor_offset_y, 10, 20)
cursor_slider_newborn_energy_sexual = pygame.Rect(update_slider_position_newborn_energy_sexual(), slider_y_newborn_energy_sexual + cursor_offset_y, 10, 20)
cursor_slider_default_energy = pygame.Rect(update_slider_position_default_energy(), slider_y_default_energy + cursor_offset_y, 10, 20)
cursor_slider_default_mass = pygame.Rect(update_slider_position_default_mass(), slider_y_default_mass + cursor_offset_y, 10, 20)
cursor_slider_default_memory = pygame.Rect(update_slider_position_default_memory(), slider_y_default_memory + cursor_offset_y, 10, 20)
cursor_slider_default_perception = pygame.Rect(update_slider_position_default_perception(), slider_y_default_perception + cursor_offset_y, 10, 20)
cursor_slider_default_speed = pygame.Rect(update_slider_position_default_speed(), slider_y_default_speed + cursor_offset_y, 10, 20)
cursor_slider_food_number= pygame.Rect(update_slider_position_food_number(), slider_y_food_number + cursor_offset_y, 10, 20)
cursor_slider_loose_of_energy_repr = pygame.Rect(update_slider_position_loose_of_energy_repr(), slider_y_loose_of_energy_repr + cursor_offset_y, 10, 20)
cursor_slider_max_energy = pygame.Rect(update_slider_position_max_energy(), slider_y_max_energy + cursor_offset_y, 10, 20)
cursor_slider_max_framerate = pygame.Rect(update_slider_position_max_framerate(), slider_y_max_framerate + cursor_offset_y, 10, 20)
cursor_slider_tick_number = pygame.Rect(update_slider_position_tick_number(), slider_y_tick_number + cursor_offset_y, 10, 20)
cursor_slider_reproducing_energy = pygame.Rect(update_slider_position_reproducing_energy(), slider_y_reproducing_energy + cursor_offset_y, 10, 20)
cursor_slider_map = pygame.Rect(update_slider_position_map(), slider_y_map + cursor_offset_y, 10, 20)



# Boucle principale du jeu
while running:

    for event in pygame.event.get():
        if (current_settings==image_premier_plan_settings and pygame.mixer.get_busy()==0):
            music_choice.play()
            print("play music")
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if current_settings == mainmenu_settings_displayed or image_premier_plan_settings_displayed:
            if keys[pygame.K_ESCAPE]:
                running=False
        pygame.mixer.music.set_volume(current_volume)  # Définit le volume de la musique
    
        
        # Gestion du clic de la souris pour le slider
        if bob_number_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_bob.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_bob_number = True
                offset_x_BN=event.pos[0] - cursor_slider_bob.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_bob_number = False

        if map_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_map.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_map = True
                offset_x_MS=event.pos[0] - cursor_slider_map.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_map = False

        if newborn_energy_parth_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_newborn_energy_parth.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_newborn_energy_parth = True
                offset_x_NEP=event.pos[0] - cursor_slider_newborn_energy_parth.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_newborn_energy_parth = False

        if newborn_energy_sexual_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_newborn_energy_sexual.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_newborn_energy_sexual = True
                offset_x_NES=event.pos[0] - cursor_slider_newborn_energy_sexual.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_newborn_energy_sexual = False

        if default_energy_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_default_energy.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_default_energy = True
                offset_x_DE=event.pos[0] - cursor_slider_default_energy.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_default_energy = False

        if default_mass_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_default_mass.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_default_mass = True
                offset_x_DM=event.pos[0] - cursor_slider_default_mass.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_default_mass = False

        if default_memory_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_default_memory.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_default_memory = True
                offset_x_DMEM=event.pos[0] - cursor_slider_default_memory.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_default_memory = False

        if default_perception_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_default_perception.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_default_perception = True
                offset_x_DP=event.pos[0] - cursor_slider_default_perception.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_default_perception = False

        if default_speed_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_default_speed.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_default_speed = True
                offset_x_DS=event.pos[0] - cursor_slider_default_speed.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_default_speed = False

        if food_number_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_food_number.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_food_number = True
                offset_x_FN=event.pos[0] - cursor_slider_food_number.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_food_number = False

        if loose_of_energy_repr_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_loose_of_energy_repr.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_loose_of_energy_repr = True
                offset_x_LOER=event.pos[0] - cursor_slider_loose_of_energy_repr.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_loose_of_energy_repr = False

        if max_energy_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_max_energy.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_max_energy = True
                offset_x_ME=event.pos[0] - cursor_slider_max_energy.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_max_energy = False

        if max_framerate_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_max_framerate.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_max_framerate = True
                offset_x_MF=event.pos[0] - cursor_slider_max_framerate.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_max_framerate = False

        if reproducing_energy_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_reproducing_energy.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_reproducing_energy = True
                offset_x_RE=event.pos[0] - cursor_slider_reproducing_energy.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_reproducing_energy = False

        if tick_number_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_tick_number.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_tick_number = True
                offset_x_TN=event.pos[0] - cursor_slider_tick_number.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_tick_number = False

        if volume_settings_displayed and event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_slider_volume.collidepoint(event.pos):
            # L'utilisateur a cliqué sur le curseur du slider, active le glissement
                dragging_volume = True
                offset_x_V=event.pos[0] - cursor_slider_volume.x
        elif event.type == pygame.MOUSEBUTTONUP:
    # Désactive le glissement lorsque l'utilisateur relâche le clic
                dragging_volume = False

        
        ###AFFICHAGE DES SLIDERS. PEUT PEUT ETRE CHANGER LES FONCTIONS UTILISEES PAR LES SLIDERS ICI. POUR LINSTANT ILS SONT CALQUES
        ###LE GETVALUE DU SLIDER DE BOB, A EVENTUELLEMENT MODIFIER
                
        if dragging_bob_number and event.type == pygame.MOUSEMOTION:
            if current_settings ==bob_number_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_bob = event.pos[0] - offset_x_BN
                cursor_x_bob = max(min(cursor_x_bob, slider_x_bob + slider_length ), slider_x_bob)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_value_bob = (int)(current_settings.get_slider_value_bob(cursor_x_bob, slider_x_bob, slider_length, max_value))
                print("Nombre de bobs courants : ",current_value_bob)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_bob.x=cursor_x_bob
                text_bob = font_slider_bob.render(str(current_value_bob), True, (255, 255, 255))
                print("value bob : ",text_bob)
                text_rect_bob = text_bob.get_rect(center=(cursor_slider_bob.x + cursor_slider_bob.width / 2, cursor_slider_bob.y - 25))

        if dragging_max_energy and event.type == pygame.MOUSEMOTION:
            if current_settings ==max_energy_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_max_energy = event.pos[0] - offset_x_ME
                cursor_x_max_energy = max(min(cursor_x_max_energy, slider_x_max_energy + slider_length ), slider_x_max_energy)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_max_energy = (int)(current_settings.get_slider_value_max_energy(cursor_x_max_energy, slider_x_max_energy, slider_length, max_value))
                print("Energie max d'un bob : ",current_max_energy)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_max_energy.x=cursor_x_max_energy
                text_max_energy = font_slider_max_energy.render(str(current_max_energy), True, (255, 255, 255))
                text_rect_max_energy = text_max_energy.get_rect()

        if dragging_map and event.type == pygame.MOUSEMOTION:
            if current_settings == map_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_map = event.pos[0] - offset_x_MS
                cursor_x_map = max(min(cursor_x_map, slider_x_map+ slider_length ), slider_x_map)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_map = (int)(current_settings.get_slider_value_map(cursor_x_map, slider_x_map, slider_length, max_value))
                print("taille de la map : ",current_map)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_map.x=cursor_x_map
                text_map = font_slider_map.render(str(current_map), True, (255, 255, 255))
                text_rect_map = text_map.get_rect()

        if dragging_newborn_energy_parth and event.type == pygame.MOUSEMOTION:
            if current_settings == newborn_energy_parth_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_newborn_energy_parth = event.pos[0] - offset_x_NEP
                cursor_x_newborn_energy_parth = max(min(cursor_x_newborn_energy_parth, slider_x_newborn_energy_parth + slider_length ), slider_x_newborn_energy_parth)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_newborn_energy_parth = (int)(current_settings.get_slider_value_newborn_energy_parth(cursor_x_newborn_energy_parth, slider_x_newborn_energy_parth, slider_length, max_value))
                print("Energie des bébé fais par parthogenesis : ",current_newborn_energy_parth)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_newborn_energy_parth.x=cursor_x_newborn_energy_parth
                text_newborn_energy_parth = font_slider_newborn_energy_parth.render(str(current_newborn_energy_parth), True, (255, 255, 255))
                text_rect_newborn_energy_parth = text_newborn_energy_parth.get_rect()

        if dragging_newborn_energy_sexual and event.type == pygame.MOUSEMOTION:
            if current_settings ==newborn_energy_sexual_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_newborn_energy_sexual = event.pos[0] - offset_x_NES
                cursor_x_newborn_energy_sexual = max(min(cursor_x_newborn_energy_sexual, slider_x_newborn_energy_sexual + slider_length ), slider_x_newborn_energy_sexual)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_newborn_energy_sexual = (int)(current_settings.get_slider_value_newborn_energy_sexual(cursor_x_newborn_energy_sexual, slider_x_newborn_energy_sexual, slider_length, max_value))
                print("Energie des bébé fais par sex : ",current_newborn_energy_sexual)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_newborn_energy_sexual.x=cursor_x_newborn_energy_sexual
                text_newborn_energy_sexual = font_slider_newborn_energy_sexual.render(str(current_newborn_energy_sexual), True, (255, 255, 255))
                text_rect_newborn_energy_sexual = text_newborn_energy_sexual.get_rect()

        if dragging_default_energy and event.type == pygame.MOUSEMOTION:
            if current_settings ==default_energy_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_default_energy  = event.pos[0] - offset_x_DE
                cursor_x_default_energy  = max(min(cursor_x_default_energy , slider_x_default_energy  + slider_length ), slider_x_default_energy )  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_default_energy  = (int)(current_settings.get_slider_value_default_energy(cursor_x_default_energy , slider_x_default_energy , slider_length, max_value))
                print("Default energy : ",current_default_energy )
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_default_energy.x=cursor_x_default_energy 
                text_default_energy = font_slider_default_energy.render(str(current_default_energy ), True, (255, 255, 255))
                text_rect_default_energy = text_default_energy.get_rect()

        if dragging_default_mass and event.type == pygame.MOUSEMOTION:
            if current_settings ==default_mass_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_default_mass = event.pos[0] - offset_x_DM
                cursor_x_default_mass = max(min(cursor_x_default_mass, slider_x_default_mass + slider_length ), slider_x_default_mass)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_default_mass = (int)(current_settings.get_slider_value_default_mass(cursor_x_default_mass, slider_x_default_mass, slider_length, max_value))
                print("Masse des bob par defaut : ",current_default_mass)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_default_mass.x=cursor_x_default_mass
                text_default_mass = font_slider_default_mass.render(str(current_default_mass), True, (255, 255, 255))
                text_rect_default_mass = text_default_mass.get_rect()

        if dragging_default_memory and event.type == pygame.MOUSEMOTION:
            if current_settings ==default_memory_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_default_memory = event.pos[0] - offset_x_DMEM
                cursor_x_default_memory = max(min(cursor_x_default_memory, slider_x_default_memory + slider_length ), slider_x_default_memory)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_default_memory = (int)(current_settings.get_slider_value_default_memory(cursor_x_default_memory, slider_x_default_memory, slider_length, max_value))
                print("Memoire par defaut d'un bob : ",current_default_memory)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_default_memory.x=cursor_x_default_memory
                text_default_memory = font_slider_default_memory.render(str(current_default_memory), True, (255, 255, 255))
                text_rect_default_memory = text_default_memory.get_rect()

        if dragging_default_perception and event.type == pygame.MOUSEMOTION:
            if current_settings ==default_perception_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_default_perception = event.pos[0] - offset_x_DP
                cursor_x_default_perception = max(min(cursor_x_default_perception, slider_x_default_perception + slider_length ), slider_x_default_perception)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_default_perception = (int)(current_settings.get_slider_value_default_perception(cursor_x_default_perception, slider_x_default_perception, slider_length, max_value))
                print("Perception par defaut d'un bob : ",current_default_perception)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_default_perception.x=cursor_x_default_perception
                text_default_perception = font_slider_default_perception.render(str(current_default_perception), True, (255, 255, 255))
                text_rect_default_perception = text_default_perception.get_rect()

        if dragging_default_speed and event.type == pygame.MOUSEMOTION:
            if current_settings ==default_speed_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_default_speed = event.pos[0] - offset_x_DS
                cursor_x_default_speed = max(min(cursor_x_default_speed, slider_x_default_speed + slider_length ), slider_x_default_speed)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_default_speed = (int)(current_settings.get_slider_value_default_speed(cursor_x_default_speed, slider_x_default_speed, slider_length, max_value))
                print("Vitesse par defaut d'un bob : ",current_default_speed)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_default_speed.x=cursor_x_default_speed
                text_default_speed = font_slider_default_speed.render(str(current_default_speed), True, (255, 255, 255))
                text_rect_default_speed = text_default_speed.get_rect()

        if dragging_food_number and event.type == pygame.MOUSEMOTION:
            if current_settings ==food_number_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_food_number = event.pos[0] - offset_x_FN
                cursor_x_food_number = max(min(cursor_x_food_number, slider_x_food_number + slider_length ), slider_x_food_number)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_food_number = (int)(current_settings.get_slider_value_food_number(cursor_x_food_number, slider_x_food_number, slider_length, max_value))
                print("Nombre de nourriture sur la map max : ",current_food_number)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_food_number.x=cursor_x_food_number
                text_food_number = font_slider_food_number.render(str(current_food_number), True, (255, 255, 255))
                text_rect_food_number = text_food_number.get_rect()

        if dragging_loose_of_energy_repr and event.type == pygame.MOUSEMOTION:
            if current_settings ==loose_of_energy_repr_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_loose_of_energy_repr = event.pos[0] - offset_x_LOER
                cursor_x_loose_of_energy_repr = max(min(cursor_x_loose_of_energy_repr, slider_x_loose_of_energy_repr + slider_length ), slider_x_loose_of_energy_repr)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_loose_of_energy_repr = (int)(current_settings.get_slider_value_loose_of_energy_repr(cursor_x_loose_of_energy_repr, slider_x_loose_of_energy_repr, slider_length, max_value))
                print("Perte d'énergie après reproduction par défaut : ",current_loose_of_energy_repr)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_loose_of_energy_repr.x=cursor_x_loose_of_energy_repr
                text_loose_of_energy_repr = font_slider_loose_of_energy_repr.render(str(current_loose_of_energy_repr), True, (255, 255, 255))
                text_rect_loose_of_energy_repr = text_loose_of_energy_repr.get_rect()

        

        if dragging_max_framerate and event.type == pygame.MOUSEMOTION:
            if current_settings ==max_framerate_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_max_framerate = event.pos[0] - offset_x_MF
                cursor_x_max_framerate = max(min(cursor_x_max_framerate, slider_x_max_framerate + slider_length ), slider_x_max_framerate)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_max_framerate = (int)(current_settings.get_slider_value_max_framerate(cursor_x_max_framerate, slider_x_max_framerate, slider_length, max_value))
                print("Fps max : ",current_max_framerate)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_max_framerate.x=cursor_x_max_framerate
                text_max_framerate = font_slider_max_framerate.render(str(current_max_framerate), True, (255, 255, 255))
                text_rect_max_framerate = text_max_framerate.get_rect()

        if dragging_reproducing_energy and event.type == pygame.MOUSEMOTION:
            if current_settings ==reproducing_energy_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_reproducing_energy = event.pos[0] - offset_x_RE
                cursor_x_reproducing_energy = max(min(cursor_x_reproducing_energy, slider_x_reproducing_energy + slider_length ), slider_x_reproducing_energy)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_reproducing_energy = (int)(current_settings.get_slider_value_reproducing_energy(cursor_x_reproducing_energy, slider_x_reproducing_energy, slider_length, max_value))
                print("Energie necessaire pour se reproduire : ",current_reproducing_energy)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_reproducing_energy.x=cursor_x_reproducing_energy
                text_reproducing_energy = font_slider_reproducing_energy.render(str(current_reproducing_energy), True, (255, 255, 255))
                text_rect_reproducing_energy = text_reproducing_energy.get_rect()

        if dragging_tick_number and event.type == pygame.MOUSEMOTION:
            if current_settings ==tick_number_settings:
                # Mise à jour de la position du curseur du slider
                cursor_x_tick_number = event.pos[0] - offset_x_TN
                cursor_x_tick_number = max(min(cursor_x_tick_number, slider_x_tick_number + slider_length ), slider_x_tick_number)  # Assurez-vous que le curseur reste dans les limites du slider
                # Mise à jour de la valeur du slider en fonction de la position
                current_tick_number = (int)(current_settings.get_slider_value_tick_number(cursor_x_tick_number, slider_x_tick_number, slider_length, max_value))
                print("Nombre de bobs courants : ",current_tick_number)
                # Mise à jour du volume en fonction du curseur (représentation graphique du curseur modifiée en fonction de la position réelle du curseur)
                cursor_slider_tick_number.x=cursor_x_tick_number
                text_tick_number = font_slider_tick_number.render(str(current_tick_number), True, (255, 255, 255))
                text_rect_tick_number = text_tick_number.get_rect(center=(cursor_slider_tick_number.x + cursor_slider_tick_number.width / 2, cursor_slider_tick_number.y - 25))
        
        if dragging_volume and event.type == pygame.MOUSEMOTION:
            if current_settings == volume_settings:
                cursor_x_volume = event.pos[0] - offset_x_V
                cursor_x_volume = max(min(cursor_x_volume, slider_x_volume + slider_length ), slider_x_volume)
                current_volume = current_settings.get_slider_value_volume(cursor_x_volume, slider_x_volume, slider_length, max_value)
                print("Volume courant : ",current_volume)
                cursor_slider_volume.x = cursor_x_volume
                text_volume = font_slider_volume.render(str(current_volume), True, (255, 255, 255))
                text_rect_volume = text_volume.get_rect(center=(cursor_slider_volume.x + cursor_slider_volume.width + 30, cursor_slider_volume.y - 10))

        


    # Gestion des touches du clavier        
    if current_settings == main_menu_settings:
        if keys[pygame.K_DOWN]:
            if selection != 1:
                selection = 1
                main_menu_settings.rect_y = screen_height // 2 + 345
                main_menu_settings.rect_height = 85
                print("Flèche bas - Sélection 1")
        elif keys[pygame.K_UP]:
            if selection != 0:
                selection = 0
                main_menu_settings.rect_y = screen_height // 2 + 100
                main_menu_settings.rect_height=100
                print("Flèche haut - Sélection 0")
    
    if current_settings == music_settings:
            current_settings.rect_x = max(206, min(current_settings.rect_x, 716+510))
            if keys[pygame.K_RIGHT]:
                current_settings.rect_x = current_settings.rect_x + 510
                if current_settings.rect_x == 206:
                    print("playing deep in the chimney")
                    music_choice.stop()
                    music_choice =music_left
                if current_settings.rect_x == 716:
                    print("playing go green")
                    music_choice.stop()
                    music_choice = music_middle
                if current_settings.rect_x == 716+510:
                    print("playing ninja skills")
                    music_choice.stop()
                    music_choice = music_right
            if keys[pygame.K_LEFT]:      
                current_settings.rect_x = current_settings.rect_x - 510
                if current_settings.rect_x == 206:
                    print("playing deep in the chimney")
                    music_choice.stop()
                    music_choice = music_left
                elif current_settings.rect_x == 716:
                    print("playing go green")
                    music_choice.stop()
                    music_choice = music_middle
                elif current_settings.rect_x == 716 + 510:
                    print("playing ninja skills")
                    music_choice.stop()
                    music_choice = music_right
    elif current_settings == skin_choice_settings:
            current_settings.rect_x = max(206, min(current_settings.rect_x, 716+510))
            print("CURSEUR ICI", current_settings.rect_x)
            if keys[pygame.K_RIGHT]:
                current_settings.rect_x = current_settings.rect_x + 510
                if round(current_settings.rect_x) == 211:
                    print("set1")
                    set_skins_choisis=skin_paths_1
                if round(current_settings.rect_x) == 721:
                    print("set2")
                    set_skin_choisis=skin_paths_2
                if current_settings.rect_x == 1226:
                    print("set3")
                    set_skin_choisis=skin_paths_3
            if keys[pygame.K_LEFT]:
                current_settings.rect_x = current_settings.rect_x - 510
                if current_settings.rect_x == 206:
                    print("set1")
                    set_skins_choisis=skin_paths_1
                if current_settings.rect_x == 716:
                    print("set2")
                    set_skin_choisis=skin_paths_2
                if current_settings.rect_x == 716+510:
                    print("set3")
                    set_skin_choisis=skin_paths_3
            print("Le set de skin choisi est : ",set_skin_choisis)
    
    if pygame.mixer.get_busy()==0:
            music_choice.play()
            print("music play")

    music_left.set_volume(current_volume / 100)
    music_middle.set_volume(current_volume / 100)
    music_right.set_volume(current_volume / 100)

    # Gestion du changement d'image dans le menu (=ecriture play clignotante)
    current_time = pygame.time.get_ticks()
    elapsed_time_since_switch = current_time - last_switch_time

    if elapsed_time_since_switch >= switch_interval and current_settings == image_premier_plan_settings:
        last_switch_time = current_time
        current_settings.update_image("image_premier_plan_1.png" if current_settings.image_path == "image_premier_plan_0.png" else \
                                    "image_premier_plan_0.png",(default_width_image,default_height_image))

    if elapsed_time_since_switch >= switch_interval and current_settings == main_menu_settings:
        last_switch_time = current_time
        current_settings.update_image("start_menu_1.png" if current_settings.image_path == "start_menu_0.png" else \
                                    "start_menu_0.png",(default_width_image,default_height_image))

    # Gestion de la touche "Entrée"
    if keys[pygame.K_RETURN] and not enter_pressed:
        enter_pressed = True
        print("Touche Entrée - Pressée")
        if current_settings == image_premier_plan_settings:
            print("Sélection de main_menu_settings")
            if not mainmenu_settings_displayed:
                mainmenu_settings_displayed=True
                current_settings = main_menu_settings
                
        elif selection == 0 and current_settings == main_menu_settings:
            print("Sélection 0 et main_menu_settings")
            if not how_to_play_settings_displayed:
                print("How to play affiché")
                how_to_play_settings_displayed = True
                current_settings = how_to_play_settings
                print("how_to_play_settings affiché")
        elif selection == 1 and current_settings == main_menu_settings:
            print("Sélection 1 et main_menu_settings")
            if not volume_settings_displayed:
                print("Volume affiché")
                volume_settings_displayed = True
                current_settings = volume_settings
                print("Volume affiché:", volume_settings_displayed)
                print("Current settings:", current_settings)
        elif selection == 0 and current_settings == how_to_play_settings:
            print("Sélection 0 et how_to_play_settings")
            if not bob_number_settings_displayed:
                print("Bob number affiché")
                bob_number_settings_displayed = True
                current_settings = bob_number_settings
        elif current_settings == bob_number_settings:
            if not skin_choice_displayed:
                print("Skin choice affiché")
                skin_choice_displayed = True
                current_settings = skin_choice_settings
        elif current_settings == volume_settings:
            print("Sélection de la musique")
            if not music_settings_displayed:
                print("Musiques affichées")
                music_settings_displayed=True
                current_settings=music_settings        
        elif current_settings == skin_choice_settings:
            print("Sélection de skin_settings")
            if not default_energy_settings_displayed:
                default_energy_settings_displayed=True
                current_settings = default_energy_settings


        elif current_settings == default_energy_settings:
            print("Sélection de default_energy_settings")
            if not default_mass_settings_displayed:
                default_mass_settings_displayed=True
                current_settings = default_mass_settings
                print("Sélection de default_mass_settings")
        elif current_settings == default_mass_settings:
            print("Sélection de default_memory_settings")
            if not default_memory_settings_displayed:
                default_memory_settings_displayed=True
                current_settings = default_memory_settings
        elif current_settings == default_memory_settings:
            print("Sélection de default_perception_settings")
            if not default_perception_settings_displayed:
                default_perception_settings_displayed=True
                current_settings = default_perception_settings
        elif current_settings == default_perception_settings:
            print("Sélection de default_speed_settings")
            if not default_speed_settings_displayed:
                default_speed_settings_displayed=True
                current_settings = default_speed_settings
        elif current_settings == default_speed_settings:
            print("Sélection de food_number_settings")
            if not food_number_settings_displayed:
                food_number_settings_displayed=True
                current_settings = food_number_settings
        elif current_settings == food_number_settings:
            print("Sélection de loose_of_energy_settings")
            if not loose_of_energy_repr_settings_displayed:
                loose_of_energy_repr_settings_displayed=True
                current_settings = loose_of_energy_repr_settings
        elif current_settings == loose_of_energy_repr_settings:
            print("Sélection de max_energy_settings")
            if not max_energy_settings_displayed:
                max_energy_settings_displayed=True
                current_settings = max_energy_settings
        elif current_settings == max_energy_settings:
            print("Sélection de newborn_energy_parth_settings")
            if not newborn_energy_parth_settings_displayed:
                newborn_energy_parth_settings_displayed=True
                current_settings = newborn_energy_parth_settings
        elif current_settings == newborn_energy_parth_settings:
            print("Sélection de newborn_energy_sexual_settings")
            if not newborn_energy_sexual_settings_displayed:
                newborn_energy_sexual_settings_displayed=True
                current_settings = newborn_energy_sexual_settings
        elif current_settings == newborn_energy_sexual_settings:
            print("Sélection de reproducing_energy_settings")
            if not reproducing_energy_settings_displayed:
                reproducing_energy_settings_displayed=True
                current_settings = reproducing_energy_settings
        elif current_settings == music_settings:
            print("Sélection de max_framerate_settings")
            if not max_framerate_settings_displayed:
                max_framerate_settings_displayed=True
                current_settings = max_framerate_settings
        elif current_settings == reproducing_energy_settings:
            print("Sélection de tick_number_settings")
            if not tick_number_settings_displayed:
                tick_number_settings_displayed=True
                current_settings = tick_number_settings
                if (current_settings == tick_number_settings) :
                    print("On est dans settings de tick number !!!!!!")
        elif current_settings == tick_number_settings:
            print("Sélection de map_settings , ON EST BIEN A LINTERIEUR")
            if not map_settings_displayed:
                map_settings_displayed=True
                current_settings = map_settings
        
        
    # Gestion de la touche "Echap"
    if keys[pygame.K_ESCAPE] and not escape_pressed:
        print("Touche Echap - Retour")
        if current_settings == main_menu_settings:
            running = False
        if current_settings == how_to_play_settings:
            escape_pressed = True
            current_settings = main_menu_settings
            how_to_play_settings_displayed = False
            mainmenu_settings_displayed = True
            print("Retour à main_menu_settings depuis how_to_play_settings")
        elif current_settings == bob_number_settings:
            escape_pressed = True
            current_settings = how_to_play_settings
            bob_number_settings_displayed = False
            how_to_play_settings_displayed = True
            print("Retour à how_to_play_settings depuis bob_number_settings")
        elif current_settings == map_settings:
            escape_pressed = True
            current_settings = tick_number_settings
            map_settings_displayed= False
            tick_number_displayed = True
            print("Retour à tick_number depuis map settings")
        
        elif current_settings == skin_choice_settings:
            escape_pressed=True
            current_settings=bob_number_settings
            bob_number_settings_displayed=True
            skin_choice_displayed=False
        elif current_settings == volume_settings:
            escape_pressed = True
            current_settings = main_menu_settings
            volume_settings_displayed = False
            mainmenu_settings_displayed = True
            print("Retour à main_menu_settings depuis volume_settings")
        elif current_settings == music_settings:
            escape_pressed=True
            current_settings=volume_settings
            music_settings_displayed=False
            volume_settings_displayed=True
            print("Retour à volume_settings depuis music_settings")
        elif current_settings == reproducing_energy_settings:
            escape_pressed=True
            current_settings=newborn_energy_sexual_settings
            reproducing_energy_settings_displayed=False
            newborn_energy_sexual_settings_displayed=True
            print("Retour à newborn_energy_sexual_settings depuis reproducing_energy_settings")
        elif current_settings == newborn_energy_sexual_settings:
            escape_pressed=True
            current_settings=newborn_energy_parth_settings
            newborn_energy_sexual_settings_displayed=False
            newborn_energy_parth_settings_displayed=True
            print("Retour à newborn_energy_parth_settings depuis newborn_energy_sexual_settings")
        elif current_settings == newborn_energy_parth_settings:
            escape_pressed=True
            current_settings=max_energy_settings
            newborn_energy_parth_settings_displayed=False
            max_energy_settings_displayed=True
            print("Retour à max_energy_settings depuis newborn_energy_parth_settings")
        elif current_settings == loose_of_energy_repr_settings:
            escape_pressed=True
            current_settings=food_number_settings
            loose_of_energy_repr_settings_displayed=False
            food_number_settings_displayed=True
            print("Retour à food_number_settings depuis loose_of_energy_repr_settings")
        elif current_settings == food_number_settings:
            escape_pressed=True
            current_settings=default_speed_settings
            food_number_settings_displayed=False
            default_speed_settings_displayed=True
            print("Retour à default_speed_settings depuis food_number_settings")
        elif current_settings == default_speed_settings:
            escape_pressed=True
            current_settings=default_perception_settings
            default_speed_settings_displayed=False
            default_perception_settings_displayed=True
            print("Retour à default_perception_settings depuis default_speed_settings")
        elif current_settings == default_perception_settings:
            escape_pressed=True
            current_settings=default_memory_settings
            default_perception_settings_displayed=False
            default_memory_settings_displayed=True
            print("Retour à default_memory_settings depuis default_perception_settings")
        elif current_settings == tick_number_settings:
            escape_pressed=True
            current_settings=reproducing_energy_settings
            tick_number_settings_displayed=False
            reproducing_energy_settings_displayed=True
            print("Retour à default_memory_settings depuis default_perception_settings")
        elif current_settings == default_memory_settings:
            escape_pressed=True
            current_settings=default_mass_settings
            default_memory_settings_displayed=False
            default_mass_settings_displayed=True
            print("Retour à default_mass_settings depuis default_memory_settings")
        elif current_settings == default_mass_settings:
            escape_pressed=True
            current_settings=default_energy_settings
            default_mass_settings_displayed=False
            default_energy_settings_displayed=True
            print("Retour à default_energy_settings depuis default_mass_settings")
        elif current_settings == max_energy_settings:
            escape_pressed=True
            current_settings=loose_of_energy_repr_settings
            max_energy_settings_displayed=False
            loose_of_energy_repr_settings_displayed=True
            print("Retour à loose_of_energy_repr_settings depuis max_energy_settings")
        elif current_settings == default_energy_settings:
            escape_pressed=True
            current_settings=skin_choice_settings
            default_energy_settings_displayed=False
            skin_choice_displayed=True
            print("Retour à skin_choice_settings depuis default_energy_settings")
        elif current_settings == max_framerate_settings:
            escape_pressed=True
            current_settings=music_settings
            max_framerate_settings_displayed=False
            music_settings_displayed=True
            print("Retour à music_settings depuis max_framerate_settings")
        

    # Réinitialisation des états des touches
    if not keys[pygame.K_RETURN]:
        enter_pressed = False
    if not keys[pygame.K_ESCAPE]:
        escape_pressed = False
        
    # Dessin de l'image de fond
        screen.blit(current_settings.current_image,
            ((current_res_x - current_settings.current_image.get_width()) // 2,
            (current_res_y - current_settings.current_image.get_height()) // 2))

    


    # Dessin du slider, après l'image
    if bob_number_settings_displayed and current_settings == bob_number_settings:
        # Dessin de la barre du slider
        bob_number_settings.draw_slider(screen, slider_x_bob, slider_y_bob, slider_length, \
                                        slider_height, cursor_offset_y, current_value_bob, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_bob)
        text_volume_bob = font_slider_bob.render(f"{(int)(current_value_bob)} bobs", True, \
                                                (255, 255, 255))
        text_rect_volume_bob = text_volume_bob.get_rect(center=(cursor_slider_bob.x + \
                                                                cursor_slider_bob.width + 30, cursor_slider_bob.y - 20))
        
        print("ici pour bob : ",text_volume_bob,current_value_bob)
        screen.blit(text_volume_bob, text_rect_volume_bob)
    else:
        update_slider_position_bob()  # Met à jour la position du curseur

    if tick_number_settings_displayed and current_settings == tick_number_settings:
        # Dessin de la barre du slider
        tick_number_settings.draw_slider(screen, slider_x_tick_number, slider_y_tick_number, slider_length, \
                                        slider_height, cursor_offset_y, current_tick_number, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_tick_number)
        text_volume_tick_number = font_slider_tick_number.render(f"{(int)(current_tick_number)} ", True, \
                                                (255, 255, 255))
        text_rect_volume_tick_number= text_volume_tick_number.get_rect(center=(cursor_slider_tick_number.x + \
                                                                cursor_slider_tick_number.width + 30, cursor_slider_tick_number.y - 20))
        screen.blit(text_volume_tick_number, text_rect_volume_tick_number)

    

    # Dessin du slider, après l'image
    if newborn_energy_parth_settings_displayed and current_settings == newborn_energy_parth_settings:
        # Dessin de la barre du slider
        newborn_energy_parth_settings.draw_slider(screen, slider_x_newborn_energy_parth, slider_y_newborn_energy_parth, slider_length, \
                                        slider_height, cursor_offset_y, current_newborn_energy_parth, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_newborn_energy_parth)
        text_volume_newborn_energy_parth = font_slider_newborn_energy_parth.render(f"{(int)(current_newborn_energy_parth)} ", True, (255, 255, 255))
    
        text_rect_volume_newborn_energy_parth = text_volume_newborn_energy_parth.get_rect(center=(cursor_slider_newborn_energy_parth.x + \
                                                                cursor_slider_newborn_energy_parth.width + 30, cursor_slider_newborn_energy_parth.y - 20))
        print("debug :", text_volume_newborn_energy_parth,text_rect_volume_newborn_energy_parth)
        print("ici pour parth : ",text_volume_newborn_energy_parth,text_rect_volume_newborn_energy_parth)

        screen.blit(text_volume_newborn_energy_parth, text_rect_volume_newborn_energy_parth)
    else:
        update_slider_position_newborn_energy_parth()  # Met à jour la position du curseur

    # Dessin du slider, après l'image
    if newborn_energy_sexual_settings_displayed and current_settings == newborn_energy_sexual_settings:
        # Dessin de la barre du slider
        newborn_energy_sexual_settings.draw_slider(screen, slider_x_newborn_energy_sexual, slider_y_newborn_energy_sexual, slider_length, \
                                        slider_height, cursor_offset_y, current_newborn_energy_sexual, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_newborn_energy_sexual)
        text_volume_newborn_energy_sexual = font_slider_newborn_energy_sexual.render(f"{(int)(current_newborn_energy_sexual)} ", True, \
                                                (255, 255, 255))
        text_rect_volume_newborn_energy_sexual = text_volume_newborn_energy_sexual.get_rect(center=(cursor_slider_newborn_energy_sexual.x + \
                                                                cursor_slider_newborn_energy_sexual.width + 30, cursor_slider_newborn_energy_sexual.y - 20))
        screen.blit(text_volume_newborn_energy_sexual, text_rect_volume_newborn_energy_sexual)
    else:
        update_slider_position_newborn_energy_sexual()  # Met à jour la position du curseur

    
    # Dessin du slider, après l'image
    if default_energy_settings_displayed and current_settings == default_energy_settings:
        # Dessin de la barre du slider
        default_energy_settings.draw_slider(screen, slider_x_default_energy, slider_y_default_energy, slider_length, \
                                        slider_height, cursor_offset_y, current_default_energy, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_default_energy)
        text_volume_default_energy = font_slider_default_energy.render(f"{(int)(current_default_energy)} ", True, \
                                                (255, 255, 255))
        text_rect_volume_default_energy = text_volume_default_energy.get_rect(center=(cursor_slider_default_energy.x + \
                                                                cursor_slider_default_energy.width + 30, cursor_slider_default_energy.y - 20))
        screen.blit(text_volume_default_energy, text_rect_volume_default_energy)
    else:
        update_slider_position_default_energy()  # Met à jour la position du curseur

    # Dessin du slider, après l'image
    if default_mass_settings_displayed and current_settings == default_mass_settings:
        # Dessin de la barre du slider
        default_mass_settings.draw_slider(screen, slider_x_default_mass, slider_y_default_mass, slider_length, \
                                        slider_height, cursor_offset_y, current_default_mass, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_default_mass)
        text_volume_default_mass = font_slider_default_mass.render(f"{(int)(current_default_mass)} ", True, \
                                                (255, 255, 255))
        text_rect_volume_default_mass = text_volume_default_mass.get_rect(center=(cursor_slider_default_mass.x + \
                                                                cursor_slider_default_mass.width + 30, cursor_slider_default_mass.y - 20))
        screen.blit(text_volume_default_mass, text_rect_volume_default_mass)
    else:
        update_slider_position_default_mass()  # Met à jour la position du curseur

    # Dessin du slider, après l'image
    if default_memory_settings_displayed and current_settings == default_memory_settings:
        # Dessin de la barre du slider
        default_memory_settings.draw_slider(screen, slider_x_default_memory, slider_y_default_memory, slider_length, \
                                        slider_height, cursor_offset_y, current_default_memory, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_default_memory)
        text_volume_default_memory = font_slider_default_memory.render(f"{(int)(current_default_memory)} ", True, \
                                                (255, 255, 255))
        text_rect_volume_default_memory = text_volume_default_memory.get_rect(center=(cursor_slider_default_memory.x + \
                                                                cursor_slider_default_memory.width + 30, cursor_slider_default_memory.y - 20))
        screen.blit(text_volume_default_memory, text_rect_volume_default_memory)
    else:
        update_slider_position_default_memory()  # Met à jour la position du curseur

    # Dessin du slider, après l'image
    if default_perception_settings_displayed and current_settings == default_perception_settings:
        # Dessin de la barre du slider
        default_perception_settings.draw_slider(screen, slider_x_default_perception, slider_y_default_perception, slider_length, \
                                        slider_height, cursor_offset_y, current_default_perception, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_default_perception)
        text_volume_default_perception = font_slider_default_perception.render(f"{(int)(current_default_perception)} ", True, \
                                                (255, 255, 255))
        text_rect_volume_default_perception = text_volume_default_perception.get_rect(center=(cursor_slider_default_perception.x + \
                                                                cursor_slider_default_perception.width + 30, cursor_slider_default_perception.y - 20))
        screen.blit(text_volume_default_perception, text_rect_volume_default_perception)
    else:
        update_slider_position_default_perception()  # Met à jour la position du curseur

    # Dessin du slider, après l'image
    if default_speed_settings_displayed and current_settings == default_speed_settings:
        # Dessin de la barre du slider
        default_speed_settings.draw_slider(screen, slider_x_default_speed, slider_y_default_speed, slider_length, \
                                        slider_height, cursor_offset_y, current_default_speed, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_default_speed)
        text_volume_default_speed = font_slider_default_speed.render(f"{(int)(current_default_speed)} ", True, \
                                                (255, 255, 255))
        text_rect_volume_default_speed = text_volume_default_speed.get_rect(center=(cursor_slider_default_speed.x + \
                                                                cursor_slider_default_speed.width + 30, cursor_slider_default_speed.y - 20))
        screen.blit(text_volume_default_speed, text_rect_volume_default_speed)
    else:
        update_slider_position_default_speed()  # Met à jour la position du curseur

    # Dessin du slider, après l'image
    if food_number_settings_displayed and current_settings == food_number_settings:
        # Dessin de la barre du slider
        food_number_settings.draw_slider(screen, slider_x_food_number, slider_y_food_number, slider_length, \
                                        slider_height, cursor_offset_y, current_food_number, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_food_number)
        text_volume_food_number = font_slider_food_number.render(f"{(int)(current_food_number)} ", True, \
                                                (255, 255, 255))
        text_rect_volume_food_number = text_volume_food_number.get_rect(center=(cursor_slider_food_number.x + \
                                                                cursor_slider_food_number.width + 30, cursor_slider_food_number.y - 20))
        screen.blit(text_volume_food_number, text_rect_volume_food_number)
    else:
        update_slider_position_food_number()  # Met à jour la position du curseur

    # Dessin du slider, après l'image
    if loose_of_energy_repr_settings_displayed and current_settings == loose_of_energy_repr_settings:
        # Dessin de la barre du slider
        loose_of_energy_repr_settings.draw_slider(screen, slider_x_loose_of_energy_repr, slider_y_loose_of_energy_repr, slider_length, \
                                        slider_height, cursor_offset_y, current_loose_of_energy_repr, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_loose_of_energy_repr)
        text_volume_loose_of_energy_repr = font_slider_loose_of_energy_repr.render(f"{(int)(current_loose_of_energy_repr)} ", True, \
                                                (255, 255, 255))
        text_rect_volume_loose_of_energy_repr = text_volume_loose_of_energy_repr.get_rect(center=(cursor_slider_loose_of_energy_repr.x + \
                                                                cursor_slider_loose_of_energy_repr.width + 30, cursor_slider_loose_of_energy_repr.y - 20))
        screen.blit(text_volume_loose_of_energy_repr, text_rect_volume_loose_of_energy_repr)
    else:
        update_slider_position_loose_of_energy_repr()  # Met à jour la position du curseur

    # Dessin du slider, après l'image
    if max_energy_settings_displayed and current_settings == max_energy_settings:
        # Dessin de la barre du slider
        max_energy_settings.draw_slider(screen, slider_x_max_energy, slider_y_max_energy, slider_length, \
                                        slider_height, cursor_offset_y, current_max_energy, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_max_energy)
        text_volume_max_energy= font_slider_max_energy.render(f"{(int)(current_max_energy)} ", True, \
                                                (255, 255, 255))
        print("debug : ", current_max_energy)
        text_rect_volume_max_energy = text_volume_max_energy.get_rect(center=(cursor_slider_max_energy.x + \
                                                                cursor_slider_max_energy.width + 30, cursor_slider_max_energy.y - 20))
        screen.blit(text_volume_max_energy, text_rect_volume_max_energy)
    else:
        update_slider_position_max_energy()  # Met à jour la position du curseur

    # Dessin du slider, après l'image
    if max_framerate_settings_displayed and current_settings == max_framerate_settings:
        # Dessin de la barre du slider
        max_framerate_settings.draw_slider(screen, slider_x_max_framerate, slider_y_max_framerate, slider_length, \
                                        slider_height, cursor_offset_y, current_max_framerate, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_max_framerate)
        text_volume_max_framerate = font_slider_max_framerate.render(f"{(int)(current_max_framerate)}", True, \
                                                (255, 255, 255))
        text_rect_volume_max_framerate = text_volume_max_framerate.get_rect(center=(cursor_slider_max_framerate.x + \
                                                                cursor_slider_max_framerate.width + 30, cursor_slider_max_framerate.y - 20))
        screen.blit(text_volume_max_framerate, text_rect_volume_max_framerate)
    else:
        update_slider_position_max_framerate()  # Met à jour la position du curseur

    # Dessin du slider, après l'image
    if reproducing_energy_settings_displayed and current_settings == reproducing_energy_settings:
        # Dessin de la barre du slider
        reproducing_energy_settings.draw_slider(screen, slider_x_reproducing_energy, slider_y_reproducing_energy, slider_length, \
                                        slider_height, cursor_offset_y, current_reproducing_energy, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_reproducing_energy)
        text_volume_reproducing_energy = font_slider_bob.render(f"{(int)(current_reproducing_energy)} ", True, \
                                                (255, 255, 255))
        text_rect_volume_reproducing_energy= text_volume_reproducing_energy.get_rect(center=(cursor_slider_reproducing_energy.x + \
                                                                cursor_slider_reproducing_energy.width + 30, cursor_slider_reproducing_energy.y - 20))
        screen.blit(text_volume_reproducing_energy, text_rect_volume_reproducing_energy)
    else:
        update_slider_position_reproducing_energy()  # Met à jour la position du curseur


########################################################END MENU################
    
    # Dessin du slider, après l'image
    if map_settings_displayed and current_settings == map_settings:
        # Dessin de la barre du slider
        map_settings.draw_slider(screen, slider_x_map, slider_y_map, slider_length, \
                                        slider_height, cursor_offset_y, current_map, max_value)
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_map)
        text_map = font_slider_tick_number.render(f"{(int)(current_map)} ", True, \
                                                (255, 255, 255))
        text_rect_map= text_map.get_rect(center=(cursor_slider_map.x + \
                                                                cursor_slider_map.width + 30, cursor_slider_map.y - 20))
        screen.blit(text_map, text_rect_map)
        
        if doonce == True:
            enter_pressed = False
            doonce = False
        
        if enter_pressed:
            #tab_settings = [current_food_number,current_value_bob,current_max_framerate,current_tick_number,20,32/2,current_default_energy,current_reproducing_energy,current_loose_of_energy_repr,current_newborn_energy_sexual,current_newborn_energy_parth,current_max_energy,current_default_perception,current_default_speed,current_default_mass,current_default_memory]
            #game_setting = my_Settings(tab_settings)
            file_path = 'constant/settings.json'
            with open(file_path, 'r') as file:
                settings = json.load(file)
            
            settings['BOB_IMAGE'] = set_skin_choisis
            settings['NUMBER_FOOD'] = current_food_number
            settings['NUMBER_BOB'] = current_value_bob
            settings['FRAME_RATE'] = current_max_framerate
            settings['TICK'] = current_tick_number

            settings['GRID_SIZE'] = current_map
            #settings['CELL_SIZE'] = -8/33*current_map + 1328/33
            settings['CELL_SIZE'] = 32/2

            settings['DEFAULT_ENERGY'] = current_default_energy
            settings['ENERGY_TO_REPRODUCE'] = current_reproducing_energy
            settings['LOSE_ENERGY_AFTER_SEX'] = current_loose_of_energy_repr
            settings['NEW_ENERGY_SEXUAL_REPRODUCE'] = current_newborn_energy_sexual
            settings['NEW_ENERGY_PARTH_REPRODUCE'] = current_newborn_energy_parth
            settings['MAX_ENERGY'] = current_max_energy

            settings['DEFAULT_PERCEPTION'] = current_default_perception
            settings['DEFAULT_SPEED'] = current_default_speed
            settings['DEFAULT_MASS'] = current_default_mass
            settings['DEFAULT_MEMORY']=current_default_memory

            with open(file_path, 'w') as file:
                json.dump(settings, file, indent=4)

            running = False
            

    else:
        update_slider_position_map()  # Met à jour la position du curseur

########################################################END MENU################

    if volume_settings_displayed and current_settings == volume_settings:
        # Dessin de la barre du slider
        volume_settings.draw_slider(screen, slider_x_volume, slider_y_volume, slider_length, \
                                    slider_height, cursor_offset_y, current_volume, max_value)
        # Dessin du curseur du slider
        pygame.draw.rect(screen, (255, 0, 0), cursor_slider_volume)
        text_volume = font_slider_volume.render(f"{current_volume} %", True, (255, 255, 255))
        text_rect_volume = text_volume.get_rect(center=(cursor_slider_volume.x + \
                                                        cursor_slider_volume.width + 30, cursor_slider_volume.y - 20))
        screen.blit(text_volume, text_rect_volume)
    else:
        update_slider_position_volume()  # Met à jour la position du curseur
    
    print("VOICI LES VALEURS CHOISIES , newborn energy parth:",current_newborn_energy_parth,"newborn energy sexual :",current_newborn_energy_sexual,"default energy:",current_default_energy,"default mass:",current_default_mass,"default_memory:",current_default_memory,"default perception :",current_default_perception,"default speed :",current_default_speed,"food number :",current_food_number,"loose of energy repr :",current_loose_of_energy_repr,"max energy :",current_max_energy,"max framerate : ",current_max_framerate,"reproducing energy:" ,current_reproducing_energy,"tick number : ",current_tick_number,"volume :",current_volume,"bob number :",current_value_bob,"TAILLE MAP :",current_map, "SET SKINS : ",set_skin_choisis)

    # Dessin du CURSEUR DE SELECTION
    pygame.draw.rect(screen, current_settings.rect_color, (current_settings.rect_x, current_settings.rect_y, \
                                                        current_settings.rect_width, current_settings.rect_height), 2)
    
    if current_settings!=main_menu_settings:
        screen.blit(text_surface_settings, text_hitbox_settings)
    else:
        screen.blit(text_surface_main_menu,text_hitbox_main_menu)
        screen.blit(text_credits,text_hitbox_credits)
        # Rafraîchissement de l'écran

    
    pygame.display.flip()
    
    # Limite de 60 FPS
    pygame.time.Clock().tick(60)

# Fermeture de Pygame et sortie du programme

#pygame.quit()
pygame.time.delay(1000)
pygame.display.quit()
#main.launch()


