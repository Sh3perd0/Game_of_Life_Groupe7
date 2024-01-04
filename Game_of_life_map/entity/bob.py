import pygame
import random
import os
from constant.settings import*
from object.common import *
from entity.entity import Entity

class Bob (Entity):
    def __init__(self):
        super().__init__()
        self.set_initial_position()
        self.speed = 1
        self.target = self.get_target()
        self.font = pygame.font.Font(None, 36)
        self.perception = 0
        self.mass = 1

    def set_mass(self, mass):
        self.mass = mass

    def set_speed(self, speed):
        self.speed = speed

    def set_perception(self, perception):
        self.perception = perception
    
    def set_energy(self, energy = 100):
        self.energy = energy

    def set_initial_position (self):
        self.grid_x = random.randint(0, GRID_SIZE - 1)
        self.grid_y = random.randint(0, GRID_SIZE - 1)
    
    def set_position (self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y

    def get_target(self):
        target = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        return target
    
    def move(self, dx, dy):
        self.grid_x += dx
        self.grid_y += dy
        # Keep track of the movement history
        # self.history.append((self.grid_x, self.grid_y))


    def move_towards_target(self):
        # Calculate the difference between Bob's position and the target position
        dx = self.target[0] - self.grid_x
        dy = self.target[1] - self.grid_y

        if dx != 0 or dy != 0:
            self.energy -= 1
        else:
            self.energy -= 0.5
            return

        # Adjust Bob's position based on speed
        for _ in range(self.speed):
            dx_direction = 0
            dy_direction = 0

            if dx != 0 or dy != 0:
                if dx == 0:
                    dy_direction = 1 if dy > 0 else -1
                elif dy == 0:
                    dx_direction = 1 if dx > 0 else -1
                else:
                    dir = random.randint(0, 1)
                    if dir == 0:
                        dx_direction = 1 if dx > 0 else -1
                    else:
                        dy_direction = 1 if dy > 0 else -1

                dx -= dx_direction
                dy -= dy_direction

                # Move Bob
                self.move(dx_direction, dy_direction)

    
    @staticmethod
    def get_assets_img():

        tile = pygame.image.load (
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "..", "assets", "Bob.png")
                )).convert_alpha()

        return tile 
      
    def get_pixel_bob_size(self):
        return 321/4 * self.energy/100, 30*self.energy/100
         
    def get_scaled_bob(self,
        width_pixel_size=None, height_pixel_size=None
    ):  # pragma: no cover
        if width_pixel_size is None or height_pixel_size is None:
            width_pixel_size, height_pixel_size = self.get_pixel_bob_size()
        return pygame.transform.smoothscale(self.get_assets_img(),(width_pixel_size, height_pixel_size)).convert_alpha()
    
        