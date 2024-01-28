import pygame
import random

from constant.settings import *
from object.common import *
from entity.entity import Entity
from collections import deque

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
        self.path_memory = deque([])
        self.perceived_food = set([])
        self.food_memory = []
        self.available_memory =  2 * self.memory

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

    # Takes a list of all food in bob perception
    def set_perceived_food(self, visiblefoods):
        size_before = len(self.food_memory)
        #Remove all food from memory that are in sight now but were already consumed by another bob
        self.food_memory = [f for f in self.food_memory if self.distance_to(f) <= self.perception and f.energy == 0]
        #Clear memory from food that are in sight now
        self.food_memory = [f for f in self.food_memory if f not in visiblefoods]
        size_after = len(self.food_memory)
        self.available_memory+=((size_before-size_after)*2)
        #Remember all foods that went out of sight
        foods_to_remember = self.perceived_food.difference(visiblefoods)
        self.perceived_food = visiblefoods
        self.remember_foods(list(foods_to_remember))

    def remember_foods(self, foods_to_remember):
        if(not foods_to_remember):
            return
        foods_to_remember.sort(key=lambda f: f.energy)
        while(self.available_memory >= 2 and foods_to_remember):
            self.food_memory.append(foods_to_remember.pop())
            self.available_memory-=2
        while(foods_to_remember and len(self.path_memory) >= 2):
            self.path_memory.pop()
            self.path_memory.pop()
            self.food_memory.append(foods_to_remember.pop())

    def target_from_memory(self):
        if(self.food_memory):
            # Go to food stored in memory
            return pygame.Vector2(self.food_memory[0].grid_x, self.food_memory[0].grid_y)
        elif(self.path_memory):
            # Should go to a non visited neighbor cell 
            possible_target = [(self.grid_x-1,self.grid_y), (self.grid_x+1, self.grid_y),
                               (self.grid_x,self.grid_y-1), (self.grid_x,self.grid_y+1)]
            possible_target = [p for p in possible_target if p not in self.path_memory and p[0] >=0 and p[1]>=0 and p[0] < GRID_SIZE and p[1] < GRID_SIZE]
            if(possible_target):
                not_visited_cell = possible_target[random.randint(0,len(possible_target)-1)]
                return pygame.Vector2(not_visited_cell[0], not_visited_cell[1])
    
    def distance_to(self, entity):
        return abs(entity.grid_x - self.grid_x) + abs(entity.grid_y - self.grid_y)

    def set_position(self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y

    def move(self, dx, dy):
        if(self.available_memory == 0 and self.path_memory):
            # can clear 1 memory point to remember position
            self.path_memory.appendleft((self.grid_x, self.grid_y))
            self.path_memory.pop()
        elif(self.available_memory > 0):
            self.path_memory.appendleft((self.grid_x, self.grid_y))
            self.available_memory-=1
        
        self.grid_x += dx
        self.grid_y += dy

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