import pygame 
from .cell import Cell
from constant.settings import *

class Map:

    #(grid_length_x, grid_length_y): number of cells each rows and columns
    #(width, height) : the dimensions of screen   
    def __init__ (self, grid_length_x, grid_length_y):
        self.block_tiles = None
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.map_list = []
        
    @staticmethod
    def get_map_dimensions (grid_length_x, grid_length_y):
        # width_cells_size, height_cells_size = Cell.get_pixel_cells_size()
        return (grid_length_x * CELL_SIZE * 2, 
                grid_length_y * CELL_SIZE * 2)
    
    def render_map (self):
        
        scaled_blocks = Cell.get_scaled_blocks()
        blit_world = pygame.Surface(Map.get_map_dimensions(self.grid_length_x, self.grid_length_y)).convert_alpha()
        blit_world.fill((0, 0, 0))

        for grid_x in range (self.grid_length_x):
            self.map_list.append([])
            for grid_y in range (self.grid_length_y):
                map_tile = Cell(grid_x, grid_y)
                self.map_list[grid_x].append (map_tile)

                render_pos = map_tile.render_pos
                #Install cells at the center of the surface
                blit_world.blit (scaled_blocks, (render_pos[0] + blit_world.get_width()/2, 
                                                  render_pos[1] + blit_world.get_height()/4))
            
        self.block_tiles = blit_world
    
    def render_map_camera(self, screen, camera):
        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                scroll = camera.scroll
 
                p = self.map_list[x][y].iso_poly
                p = [(x + self.block_tiles.get_width()/2 + scroll.x   , y + self.block_tiles.get_height()/4 + scroll.y) for x, y in p]
                
                #pygame.draw.polygon(screen, (255,255,255), p, 1)
        

    # def blit_world (self):
    #     scaled_blocks = Cell.get_scaled_blocks()
    #     width_cells_size, height_cells_size = Cell.get_pixel_cells_size()
    #     width_map_size = (width_cells_size*self.grid_length_x)
    #     height_map_size = (height_cells_size*self.grid_length_y)
    #     blit_world = pygame.Surface ((width_map_size * 2, height_map_size * 2)).convert_alpha()

    #     map = []

    #     for grid_x in range (self.grid_length_x):
    #         map.append([])
    #         for grid_y in range (self.grid_length_y):
    #             map_tile = Cell(CELL_SIZE, grid_x, grid_y)
    #             map[grid_x].append (map_tile)

    #             render_pos = map_tile.render_pos
    #             blit_world.blit (map_tile.tile, (render_pos[0] + self.ground.get_width()/2, render_pos[1] + self.ground.get_height()/4))
            
    #     return map

