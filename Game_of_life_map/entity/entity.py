import pygame
import random
from constant.settings import *
from object.common import *


class Entity:
    def __init__(self, energy=100):
        self.grid_x = 0
        self.grid_y = 0
        self.energy = 100
        self.font = pygame.font.Font(None, 36)
