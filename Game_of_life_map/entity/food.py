import pygame
import random
import os
from object.common import *
from constant.settings import*
from entity.entity import Entity

class Food(Entity):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 36)
    
    def set_energy(self, energy = 100):
        self.energy = 100

    def set_position (self):
        self.grid_x = random.randint(0, GRID_SIZE - 1)
        self.grid_y = random.randint(0, GRID_SIZE - 1)
    
    
    # @staticmethod
    # def get_assets_img():

    #     tile = pygame.image.load (
    #             os.path.abspath(
    #                 os.path.join(os.path.dirname(__file__), "..", "assets", "apple.png")
    #             )).convert_alpha()

    #     return tile 
     
    def get_pixel_food_size(self):
        return 321/8 * self.energy/100, 25/2 * self.energy/100
    
    
    # def get_scaled_food(self,
    #     width_pixel_size=None, height_pixel_size=None
    # ):  # pragma: no cover
    #     if width_pixel_size is None or height_pixel_size is None:
    #         width_pixel_size, height_pixel_size = self.get_pixel_food_size()
    #     return pygame.transform.smoothscale(self.get_assets_img(),(width_pixel_size, height_pixel_size)).convert_alpha()
    
