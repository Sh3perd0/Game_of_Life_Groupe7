import pygame 
from .cell import Cell
from .cell_size import CELL_SIZE

class Map:

    #(grid_length_x, grid_length_y): number of cells each rows and columns
    #(width, height) : the dimensions of screen   
    def __init__ (self, grid_length_x, grid_length_y, width, height):
        
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.ground = pygame.Surface((grid_length_x * CELL_SIZE * 2 , grid_length_y * CELL_SIZE * 2)).convert_alpha()
        self.map = self.create_map()


    def create_map(self):
        
        map = []

        for grid_x in range (self.grid_length_x):
            map.append([])
            for grid_y in range (self.grid_length_y):
                map_tile = Cell(CELL_SIZE, grid_x, grid_y)
                map[grid_x].append (map_tile)

                render_pos = map_tile.render_pos
                self.ground.blit (map_tile.tile, (render_pos[0] + self.ground.get_width()/2, render_pos[1] + self.ground.get_height()/4))
            
        return map