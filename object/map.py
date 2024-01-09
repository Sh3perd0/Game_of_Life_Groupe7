import pygame
from .cell import Cell
from constant.settings import *
from .common import *

class Map:
    # (grid_length_x, grid_length_y): number of cells each rows and columns
    # (width, height) : the dimensions of screen
    def __init__(self, screen, grid_length_x, grid_length_y):
        self.block_tiles = None
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.map_dict = {}

        self.width = screen.get_width()
        self.height = screen.get_height()

    @staticmethod
    def get_map_dimensions(grid_length_x, grid_length_y):
        # width_cells_size, height_cells_size = Cell.get_pixel_cells_size()
        return (grid_length_x * CELL_SIZE * 4, grid_length_y * CELL_SIZE * 4)

    def render_map(self):
        scaled_blocks = get_scaled_image(get_assets_img(CELL_IMAGE), Cell.get_pixel_cells_size())
        map_dimensions = Map.get_map_dimensions(self.grid_length_x, self.grid_length_y)
        blit_world = pygame.Surface(map_dimensions).convert_alpha()
        blit_world.fill((0, 0, 0))

        blit_world_width_half = blit_world.get_width() / 2
        blit_world_height_quarter = blit_world.get_height() / 4

        for grid_x in range(self.grid_length_x):
            for grid_y in range(self.grid_length_y):
                map_tile = Cell(grid_x, grid_y)
                self.map_dict[(grid_x, grid_y)] = map_tile

                render_pos = map_tile.render_pos
                blit_world.blit(
                    scaled_blocks,
                    (
                        render_pos[0] + blit_world_width_half,
                        render_pos[1] + blit_world_height_quarter,
                    ),
                )

        self.block_tiles = blit_world

    # def render_map_camera(self, camera):
    #     visible_cells = self.get_visible_cells(camera)
    #     for cell in visible_cells:
    #         scroll = camera.scroll
    #         p = cell.iso_poly
    #         p = [(x + self.block_tiles.get_width() / 2 + scroll.x, y + self.block_tiles.get_height() / 4 + scroll.y) for x, y in p]

    # def get_visible_cells(self, camera):
    #     visible_cells = []

    #     # Calculate the range of grid coordinates that are currently visible
    #     start_x = max(0, int(camera.scroll.x / CELL_SIZE))
    #     end_x = min(self.grid_length_x, start_x + self.width / CELL_SIZE + 1)
    #     start_y = max(0, int(camera.scroll.y / CELL_SIZE))
    #     end_y = min(self.grid_length_y, start_y + self.height / CELL_SIZE + 1)

    #     # Add all cells in this range to the list of visible cells
    #     for x in range(int(start_x), int(end_x)):
    #         for y in range(int(start_y), int(end_y)):
    #             visible_cells.append(self.map_dict[(x,y)])

    # return visible_cells
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
