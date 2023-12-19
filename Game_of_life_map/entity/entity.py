import pygame
import random
from constant.settings import*
from object.common import *

class Entity :
    def __init__ (self):
        self.grid_x = 0
        self.grid_y = 0
        self.energy = 0
        self.set_energy()
    
    
