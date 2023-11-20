import pygame
import random
from constant.grid_size import GRID_SIZE
import os
from constant.cell_size import CELL_SIZE
from object.common import *
from entity.entity import Entity

class Bob (Entity):
    def __init__(self):
        super().__init__()
        self.set_initial_position()
        self.speed = 1  
        self.target = self.get_target()

    
    def set_energy(self, energy = 100):
        self.energy = energy

    def set_initial_position (self):
        self.grid_x = random.randint(0, GRID_SIZE - 1)
        self.grid_y = random.randint(0, GRID_SIZE - 1)
    
    def set_position (self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y
        
    def get_target(self):
        target = pygame.Vector2(0, 0)
        return target
    
    def move(self, dx, dy):
        self.grid_x += dx
        self.grid_y += dy
        # Keep track of the movement history
        # self.history.append((self.grid_x, self.grid_y))


    def move_towards_target(self):
        # Calculate the difference between Bob's position and the target position
        dx = self.target.x - self.grid_x
        dy = self.target.y - self.grid_y
        
        dx_direction=0
        dy_direction=0
        if dx==0:
            dy_direction = 1 if dy > 0 else -1
        if dy==0:
            dx_direction = 1 if dx > 0 else -1
        if (dx!=0 and dy!=0):
            dir=random.randint(0,1)
            if dir==0:
                dx_direction = 1 if dx > 0 else -1
            if dir==1:
                dy_direction = 1 if dy > 0 else -1
        # Adjust Bob's position based on speed
        dx_move = min(abs(dx), self.speed) * dx_direction
        dy_move = min(abs(dy), self.speed) * dy_direction
        # Move Bob
        self.move(dx_move, dy_move)

    
    @staticmethod
    def get_assets_img():

        tile = pygame.image.load (
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "..", "assets", "Bob.png")
                )).convert_alpha()

        return tile 
    
    @staticmethod  
    def get_pixel_bob_size():
        return 321/4, 30
         
    @staticmethod
    def get_scaled_bob(
        width_pixel_size=None, height_pixel_size=None
    ):  # pragma: no cover
        if width_pixel_size is None or height_pixel_size is None:
            width_pixel_size, height_pixel_size = Bob.get_pixel_bob_size()
        return pygame.transform.smoothscale(Bob.get_assets_img(),(width_pixel_size, height_pixel_size)).convert_alpha()
    
        

           

