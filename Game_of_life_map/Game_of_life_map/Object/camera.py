import pygame


class Camera: 
    def __init__(self, width, height):

        # If window is not None:
        #The dimensions of the window
        self.width = width
        self.height = height
        
        self.scroll = pygame.Vector2(0,0)
        self.dx = 0
        self.dy = 0
        
        self.speed = 25
 

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
        self.scroll.x += self.dx
        self.scroll.y += self.dy