import pygame
from constant.settings import *
import os
from .common import *
from constant.settings import *


class Cell:
    def __init__(self, grid_x, grid_y):
        self.iso_poly = self.create_cell(grid_x, grid_y)["iso_poly"]
        self.render_pos = self.create_cell(grid_x, grid_y)["render_pos"]

    def create_cell(self, grid_x, grid_y):
        rect = get_cart_rect_pos(grid_x, grid_y)

        iso_poly = [cart_to_iso(x, y) for x, y in rect]

        render_pos = get_render_pos(grid_x, grid_y)

        out = {
            # "grid": [grid_x, grid_y],#The order[][] of cell
            "cart_rect": rect,  # The position of cell in cart (Can remove)
            "iso_poly": iso_poly,  # The position of cell in iso
            "render_pos": render_pos,  # The position to insert image
        }

        return out

    # @staticmethod
    # def get_assets_img():
    #     tile = pygame.image.load(
    #         os.path.abspath(
    #             os.path.join(os.path.dirname(__file__), "..", "assets", "grass.png")
    #         )
    #     ).convert_alpha()

    #     return tile

    # @staticmethod
    def get_pixel_cells_size():
        return 321 / 8, 161 / 8
        #return CELL_SIZE*(321/8/16), (CELL_SIZE/2)*(321/8/16)

    # # Transform the size of block's asset as standard
    # @staticmethod
    # def get_scaled_blocks(
    #     width_pixel_size=None, height_pixel_size=None
    # ):  # pragma: no cover
    #     if width_pixel_size is None or height_pixel_size is None:
    #         width_pixel_size, height_pixel_size = Cell.get_pixel_cells_size()
    #     return pygame.transform.smoothscale(
    #         Cell.get_assets_img(), (width_pixel_size, height_pixel_size)
    #     ).convert_alpha()
