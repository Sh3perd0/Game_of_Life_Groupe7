import pygame
from object.map import Map
from constant.grid_size import GRID_SIZE
class Camera: 
    def __init__(self, width, height):

        # If window is not None:
        #The dimensions of the window
        self.width = width
        self.height = height
        #The dimensions of the map
        self.map_width, self.map_height = Map.get_map_dimensions(GRID_SIZE, GRID_SIZE)
        self.scroll = pygame.Vector2(-self.map_width/4,-self.map_height/4)
        # self.scroll = pygame.Vector2(0,0)
        self.dx = 0
        self.dy = 0
        
        self.speed = 30
 

    def update(self):

        mouse_pos = pygame.mouse.get_pos()
        
        # x movement
        if mouse_pos[0] > self.width * 0.95:
            self.dx = -self.speed
        elif mouse_pos[0] < self.width * 0.05:
            self.dx = self.speed
        else:
            self.dx = 0

        # y movement
        if mouse_pos[1] > self.height * 0.95:
            self.dy = -self.speed
        elif mouse_pos[1] < self.height * 0.05:
            self.dy = self.speed
        else:
            self.dy = 0


        #Update camera scroll
        
        # new_scroll_x = self.scroll.x + self.dx
        # new_scroll_y = self.scroll.y + self.dy

        # if (abs (new_scroll_x) < self.map_width - self.width):
        #     self.scroll.x = new_scroll_x
        # else:
        #     self.scroll.x = self.scroll.x
        
        # if (abs (new_scroll_y) < self.map_height - self.height):
        #     self.scroll.y = new_scroll_y
        # else:
        #     self.scroll.y = self.scroll.y       
        # self.scroll.x = max(0, min(new_scroll_x, map_width - self.width))
        # self.scroll.y = max(0, min(new_scroll_y, map_height - self.height))
        # if (abs(mouse_pos[0]) < self.map_width):
        #     self.scroll.x += self.dx
        # if (abs(mouse_pos[1]) < self.map_height):
        #     self.scroll.y += self.dy
        self.scroll.x += self.dx
        self.scroll.y += self.dy
