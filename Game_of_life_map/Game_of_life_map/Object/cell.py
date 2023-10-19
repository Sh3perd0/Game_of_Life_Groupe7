import pygame 


class Cell:
    def __init__ (self, size, grid_x, grid_y):
        self.size = size

        self.tile = self.load_images()
        self.iso_poly = self.create_cell(grid_x, grid_y)["iso_poly"]
        self.render_pos = self.create_cell(grid_x,grid_y)["render_pos"] 
        
    def create_cell(self, grid_x, grid_y):
        
        rect = [
            (grid_x * self.size, grid_y * self.size),
            (grid_x * self.size + self.size, grid_y * self.size),
            (grid_x * self.size + self.size, grid_y * self.size + self.size),
            (grid_x * self.size, grid_y * self.size + self.size)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])


        out = {
           # "grid": [grid_x, grid_y],#The order[][] of cell 
            "cart_rect": rect,#The position of cell in cart (Can remove)
            "iso_poly": iso_poly,#The position of cell in iso
            "render_pos": [minx, miny],#The position to insert image 
        }

        return out
    
    @staticmethod
    def cart_to_iso(x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y
   

    def load_images(self):

        tile = pygame.image.load ("assets/block.png").convert_alpha()

        return tile