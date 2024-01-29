import pygame
pygame.init()

class Settings:
    def __init__(self, rect_x, rect_y, rect_width, rect_height, rect_color, image_path, res_image):
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.rect_color = rect_color
        self.image_path = image_path
        self.res_image=res_image
        self.current_image = pygame.transform.scale(pygame.image.load(self.image_path),res_image)

    def update_image(self, new_image_path, res_image):
        self.image_path = new_image_path
        self.current_image = pygame.transform.scale(pygame.image.load(self.image_path),res_image)
        print(f"Image mise à jour: {self.image_path}")

    def draw_slider(self, screen, slider_x, slider_y, slider_length, slider_height, cursor_offset_y, current_value, max_value):
        #dessin du slider qui sera ensuite utilisé deux fois différemment
        pygame.draw.rect(screen, (255, 255, 255), (slider_x, slider_y, slider_length, slider_height))
       
    def get_slider_value_bob(self, slider_x_bob, slider_x_start, slider_length, max_value):
        slider_difference_bob = slider_x_bob - slider_x_start       
        return slider_difference_bob
        
    
    def get_slider_value_volume(self, slider_x_volume, slider_x_start, slider_length, max_value):
    # Calculez la différence entre la position actuelle du curseur et la position initiale
        slider_difference_volume = slider_x_volume - slider_x_start
        return slider_difference_volume
    
    def get_slider_value_map(self, slider_x_map, slider_x_start, slider_length, max_value):
    # Calculez la différence entre la position actuelle du curseur et la position initiale
        slider_difference_map = slider_x_map - slider_x_start
        return slider_difference_map
    
    def get_slider_value_newborn_energy_parth(self, slider_x_newborn_energy_parth, slider_x_start, slider_length, max_value):
        slider_difference_newborn_energy_parth = slider_x_newborn_energy_parth - slider_x_start       
        return slider_difference_newborn_energy_parth
    
    
    
    def get_slider_value_newborn_energy_sexual(self, slider_x_newborn_energy_sexual, slider_x_start, slider_length, max_value):
        slider_difference_newborn_energy_sexual = slider_x_newborn_energy_sexual - slider_x_start       
        return slider_difference_newborn_energy_sexual
    
    def get_slider_value_default_energy(self, slider_x_default_energy, slider_x_start, slider_length, max_value):
        slider_difference_default_energy = slider_x_default_energy - slider_x_start       
        return slider_difference_default_energy
    
    def get_slider_value_default_mass(self, slider_x_default_mass, slider_x_start, slider_length, max_value):
        slider_difference_default_mass = slider_x_default_mass - slider_x_start       
        return slider_difference_default_mass
    
    def get_slider_value_default_memory(self, slider_x_default_memory, slider_x_start, slider_length, max_value):
        slider_difference_default_memory = slider_x_default_memory - slider_x_start       
        return slider_difference_default_memory
    
    def get_slider_value_default_perception(self, slider_x_default_perception, slider_x_start, slider_length, max_value):
        slider_difference_default_perception = slider_x_default_perception - slider_x_start       
        return slider_difference_default_perception
    
    def get_slider_value_default_speed(self, slider_x_default_speed, slider_x_start, slider_length, max_value):
        slider_difference_default_speed = slider_x_default_speed - slider_x_start       
        return slider_difference_default_speed
    
    def get_slider_value_food_number(self, slider_x_food_number, slider_x_start, slider_length, max_value):
        slider_difference_food_number = slider_x_food_number - slider_x_start        
        return slider_difference_food_number
    
    def get_slider_value_loose_of_energy_repr(self, slider_x_loose_of_energy_repr, slider_x_start, slider_length, max_value):
        slider_difference_loose_of_energy_repr = slider_x_loose_of_energy_repr - slider_x_start             
        return slider_difference_loose_of_energy_repr
    
    def get_slider_value_max_energy(self, slider_x_max_energy, slider_x_start, slider_length, max_value):
        slider_difference_max_energy = slider_x_max_energy - slider_x_start     
        print("valeur avant la normalisation",slider_difference_max_energy)    
        return slider_difference_max_energy
    
    def get_slider_value_max_framerate(self, slider_x_max_framerate, slider_x_start, slider_length, max_value):
        slider_difference_max_framerate = slider_x_max_framerate - slider_x_start       
        return slider_difference_max_framerate
    
    def get_slider_value_reproducing_energy(self, slider_x_reproducing_energy, slider_x_start, slider_length, max_value):
        slider_difference_reproducing_energy = slider_x_reproducing_energy - slider_x_start       
        return slider_difference_reproducing_energy
    
    def get_slider_value_tick_number(self, slider_x_tick_number, slider_x_start, slider_length, max_value):
        slider_difference_tick_number = slider_x_tick_number - slider_x_start       
        return slider_difference_tick_number