import pygame 
import sys
from .map import Map
from .camera import Camera

class Game:
    
    def __init__ (self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.map = Map(50, 50, self.width, self.height)

        #Camera
        self.camera = Camera (self.width, self.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick (60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    
    def update(self):
        self.camera.update()

    def draw (self):
        self.screen.fill ((0, 0, 0))
        
        self.screen.blit(self.map.ground, (self.camera.scroll.x, self.camera.scroll.y))

        for x in range(self.map.grid_length_x):
            for y in range(self.map.grid_length_y):


                ground = self.map.ground
                scroll = self.camera.scroll
 
                p = self.map.map[x][y].iso_poly
                p = [(x + ground.get_width()/2 + scroll.x, y + ground.get_height()/4 + scroll.y) for x, y in p]
                
                pygame.draw.polygon(self.screen, (30, 144, 255), p, 1)

        pygame.display.flip()


    

        