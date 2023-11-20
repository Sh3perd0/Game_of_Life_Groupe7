import pygame
import random
from constant.grid_size import GRID_SIZE
import os
from constant.cell_size import CELL_SIZE
from object.common import *

class Entity :
    def __init__ (self):
        self.grid_x = 0
        self.grid_y = 0
        self.energy = 0
        self.set_energy()
    
    def set_energy(self, energy):
        self.energy = energy
    
