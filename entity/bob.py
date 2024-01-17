import pygame
import random

from constant.settings import *
from object.common import *
from entity.entity import Entity


class Bob(Entity):
    def __init__(self, speed=DEFAULT_SPEED, energy=DEFAULT_ENERGY, perception=DEFAULT_PERCEPTION, mass=DEFAULT_MASS):
        super().__init__(energy)
        self.set_initial_position()
        self.speed = speed
        self.total_speed = self.speed
        self.target = (
            random.randint(0, GRID_SIZE - 1),
            random.randint(0, GRID_SIZE - 1),
        )
        self.perception = perception
        self.mass = mass
        self.volume = self.mass ** (1 / 3)
        self.speed_buffer = float(self.total_speed - int(self.total_speed))

    def set_mass_volume(self, mass):
        self.mass = mass
        self.volume = self.mass ** (1 / 3)

    def set_speed(self, speed):
        self.speed = speed

    def set_perception(self, perception):
        self.perception = perception

    def set_energy(self, energy=DEFAULT_ENERGY):
        self.energy = energy

    def set_initial_position(self):
        self.grid_x = random.randint(0, GRID_SIZE - 1)
        self.grid_y = random.randint(0, GRID_SIZE - 1)

    def set_position(self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y

    def move(self, dx, dy):
        self.grid_x += dx
        self.grid_y += dy
        # Keep track of the movement history
        # self.history.append((self.grid_x, self.grid_y))

    def update_speed(self):
        self.total_speed = self.speed + self.speed_buffer
        self.speed_buffer = self.total_speed - int(self.total_speed)

    # the given bob is the prey
    def is_predator (self, bob):
        if self.mass > 3/2 * bob.mass:
            return True
        else:
            return False
        
    def is_prey (self, bob):
        if self.mass < 2/3 * bob.mass:
            return True
        else:
            return False

    # def get_pixel_bob_size(self):
    #     return 321 / 8 * self.volume, 25 / 2 * self.volume
    
    def get_pixel_bob_size(self):
        return 321 / 8 * self.mass, 25 / 2 * self.mass
    



