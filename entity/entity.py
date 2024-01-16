import pygame
import random
from constant.settings import *
from object.common import *


class Entity:
    def __init__(self, energy=DEFAULT_ENERGY):
        self.grid_x = 0
        self.grid_y = 0
        self.energy = energy
        self.font = pygame.font.Font(None, 36)
