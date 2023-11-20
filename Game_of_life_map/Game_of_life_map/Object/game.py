import pygame 
import sys
import random
from .map import Map
from camera.camera import Camera
from constant.grid_size import GRID_SIZE
from constant.number_Bob import NUMBER_BOB
from constant.number_food import NUMBER_FOOD
from entity.bob import Bob
from .common import *
from entity.food import Food
from entity.entity import Entity

class Game:
    
    def __init__ (self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.camera = Camera(self.width, self.height)
        self.map = Map(GRID_SIZE, GRID_SIZE)
        self.map.render_map()
        self.list_bob = self.create_list_bob()
        self.list_food = self.create_list_food()
        self.tick = 0
        self.day = 0

    def run(self):
        self.playing = True
        
        # pygame.display.set_window_position(, )
        while self.playing:
            self.clock.tick (5)
            self.events()
            self.camera.update()
            self.update_move_bob()
            self.draw()
            self.eat_food()
            self.reproduce()
            self.die()
            self.tick +=1
            if self.tick == 100:
                self.tick=0
                self.day+=1
    

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    


    def draw (self):
        scroll = self.camera.scroll
        self.screen.fill((0,0,0))
        self.screen.blit(self.map.block_tiles, (scroll.x, scroll.y))
        self.draw_food()
        self.draw_bob()
        self.draw_text()
        self.map.render_map_camera(self.screen, self.camera)
        pygame.display.flip()

    def draw_bob(self):
        map_block_tiles = self.map.block_tiles
        scroll = self.camera.scroll
        for bob in self.list_bob :
            render_pos = get_render_pos(bob.grid_x, bob.grid_y)
            self.screen.blit(Bob.get_scaled_bob(), (render_pos[0] + map_block_tiles.get_width()/2 + scroll.x,
                                                     render_pos[1] + map_block_tiles.get_height()/4 + scroll.y))

    def create_list_bob (self):
        bob_list = []
        for _ in range(NUMBER_BOB):
            bob = Bob()
            bob_list.append(bob) 
        return bob_list  

    def update_move_bob (self):
        for bob in self.list_bob:
            bob.move_towards_target()

        
    def create_list_food (self):
        food_list = []
        for _ in range (NUMBER_FOOD):
            food = Food()
            food.set_position()
            food_list.append(food)
        return food_list
    
    def draw_food(self):
        map_block_tiles = self.map.block_tiles
        scroll = self.camera.scroll
        for food in self.list_food:
            render_pos = get_render_pos (food.grid_x, food.grid_y)
            self.screen.blit (Food.get_scaled_food(), (render_pos[0] + map_block_tiles.get_width()/2 + scroll.x, render_pos[1] + map_block_tiles.get_height()/4 + scroll.y))
    
    # bob reproduces when the energy>=200                                                
    def reproduce(self): 
        for bob in self.list_bob:
            if bob.energy>=200:
                bob.energy=50
                bob1=Bob()
                bob1.set_position(bob.grid_x, bob.grid_y)
                self.list_bob.append(bob1) 
                bob1.energy = 50
                bob1.speed = round((random.uniform(bob.speed-0.1,bob.speed+0.1)), 2)

    # bob eat food
    def eat_food(self) :
        for bob in self.list_bob:
            for food in self.list_food:
                if (food.grid_x==bob.grid_x) and (food.grid_y==bob.grid_y):
                    self.list_food.remove(food)
                    bob.energy+=min(100,200-bob.energy)

    # bob die : lost all of energy
    def die(self):
        for bob in self.list_bob:
            if bob.energy<=0:
                self.list_bob.remove(bob)

    
    def draw_text(self):

        font = pygame.font.SysFont(None, 50)
        text_surface = font.render('tick={}'.format(self.tick), True, (255,255,255))
        text_surface_day = font.render('day={}'.format(self.day), True, (255,255,255))
        text_rect = text_surface.get_rect(topleft=(0,0))
        text_rect_day = text_surface.get_rect(topleft=(1000,0))
        self.screen.blit (text_surface, text_rect)
        self.screen.blit (text_surface_day, text_rect_day)
