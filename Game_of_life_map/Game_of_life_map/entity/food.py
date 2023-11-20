import pygame
import random
import os
from object.common import *
from constant.grid_size import GRID_SIZE
from entity.entity import Entity

class Food(Entity):
    def __init__(self):
        super().__init__()
    
    def set_energy(self, energy = 100):
        self.energy = energy

    def set_position (self):
        self.grid_x = random.randint(0, GRID_SIZE - 1)
        self.grid_y = random.randint(0, GRID_SIZE - 1)
    
    
    @staticmethod
    def get_assets_img():

        tile = pygame.image.load (
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "..", "assets", "apple.png")
                )).convert_alpha()

        return tile 
    
    @staticmethod  
    def get_pixel_food_size():
        return 321/4, 30
    
    @staticmethod
    def get_scaled_food(
        width_pixel_size=None, height_pixel_size=None
    ):  # pragma: no cover
        if width_pixel_size is None or height_pixel_size is None:
            width_pixel_size, height_pixel_size = Food.get_pixel_food_size()
        return pygame.transform.smoothscale(Food.get_assets_img(),(width_pixel_size, height_pixel_size)).convert_alpha()
    
