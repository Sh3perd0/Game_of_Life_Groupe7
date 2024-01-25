import pygame
import random

from constant.settings import *
from object.common import *
from entity.entity import Entity


class Bob(Entity):
    def __init__(
        self,
        speed=DEFAULT_SPEED,
        energy=DEFAULT_ENERGY,
        perception=DEFAULT_PERCEPTION,
        true_perception=DEFAULT_PERCEPTION,
        mass=DEFAULT_MASS,
        memory=DEFAULT_MEMORY,
    ):
        super().__init__(energy)
        self.set_initial_position()
        self.speed = speed
        self.total_speed = self.speed
        self.target = pygame.Vector2(
            random.randint(max(0, self.grid_x - 1), min(self.grid_x + 1, GRID_SIZE - 1)),
            random.randint(max(0, self.grid_y - 1), min(self.grid_y + 1, GRID_SIZE - 1)),
        )
        self.perception = perception
        self.true_perception = true_perception
        self.mass = mass
        self.volume = self.mass ** (1 / 3)
        self.speed_buffer = float(self.total_speed - int(self.total_speed))
        self.memory = memory
        self.food_memory = []

    def set_mass_volume(self, mass):
        self.mass = mass
        self.volume = self.mass ** (1 / 3)

    def set_speed(self, speed):
        self.speed = speed

    def set_perception(self, perception):
        self.perception = perception

    def set_true_perception(self, true_perception):
        self.true_perception = true_perception

    def set_energy(self, energy=DEFAULT_ENERGY):
        self.energy = energy

    def set_memory(self, memory=DEFAULT_MEMORY):
        self.memory = memory

    def set_initial_position(self):
        self.grid_x = random.randint(0, GRID_SIZE - 1)
        self.grid_y = random.randint(0, GRID_SIZE - 1)

    def forget_food(self, food):
        self.food_memory = list(filter(lambda f: f != food, self.food_memory))

    # Remember list of foods
    def remember_food(self, foods):
        self.food_memory = list(set(self.food_memory + foods))
        self.food_memory.sort(key=lambda f: (self.distance_to(f), f.energy))
        self.food_memory = self.food_memory[: (self.memory)]

    def target_from_memory(self):
        if self.food_memory:
            food = self.food_memory.pop(0)
            if food.grid_x != self.grid_x or food.grid_y != self.grid_y:
                return pygame.Vector2(food.grid_x, food.grid_y)
        return None

    def distance_to(self, entity):
        return abs(entity.grid_x - self.grid_x) + abs(entity.grid_y - self.grid_y)

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
    def is_predator(self, bob):
        if self.mass > 3 / 2 * bob.mass:
            return True
        else:
            return False

    def is_prey(self, bob):
        if self.mass < 2 / 3 * bob.mass:
            return True
        else:
            return False

    def get_pixel_bob_size(self):
        return 321 / 8 * self.volume, 25 / 2 * self.volume
