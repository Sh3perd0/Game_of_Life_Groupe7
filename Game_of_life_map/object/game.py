import pygame 
import sys
import random
from .map import Map
from camera.camera import Camera
from constant.settings import*
from entity.bob import Bob
from .common import *
from entity.food import Food
from entity.entity import Entity
from logic_game.entity_activity import EntityActivity
import pickle
import codecs

class Game:


    def __init__ (self, screen, clock):
        self.BOB_FONT = pygame.font.Font(None, 36)
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.camera = Camera(self.width, self.height)
        self.map = Map(GRID_SIZE, GRID_SIZE)
        self.map.render_map()
        self.entity_activity = EntityActivity()
        self.tick = 0
        self.day = 0

#MAIN LOOP
    def run(self):
        self.playing = True
        # pygame.display.set_window_position(, )
        while self.playing:
            self.clock.tick (2)
            self.events()
            self.camera.update()
            self.update_move_bob()
            self.draw()
            self.eat_food()
            #self.reproduce()
            self.sexual_reproduction()
            self.die()
            self.get_target_new()
            self.update_perception()
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
                if event.key == pygame.K_s:
                    self.save()
                if event.key == pygame.K_l:
                    self.load()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def load(self):
         file = open('save.txt', 'rb')
         s = file.read()
         self.entity_activity = pickle.loads(codecs.decode(s,"base64"))

    def save(self):
        s = codecs.encode(pickle.dumps(self.entity_activity), "base64").decode()
        file = open('save.txt', 'w')
        file.write(s)
        file.close()

    
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
        for bob in self.entity_activity.list_bob :
            render_pos = get_render_pos(bob.grid_x, bob.grid_y)
            self.screen.blit(bob.get_scaled_bob(), (render_pos[0] + map_block_tiles.get_width()/2 + scroll.x,
                                                     render_pos[1] + map_block_tiles.get_height()/4 + scroll.y))
            energy_text = self.BOB_FONT.render(f'E: {bob.energy}, P: {bob.perception}', True, (255, 255, 255))
            text_rect = energy_text.get_rect(center=(render_pos[0] + map_block_tiles.get_width()/2 + scroll.x,
                                                  render_pos[1] + map_block_tiles.get_height()/4 + scroll.y - 20))
            self.screen.blit(energy_text, text_rect)
        
    def update_move_bob (self):
        self.entity_activity.update_move_bob()
    
    def draw_food(self):
        map_block_tiles = self.map.block_tiles
        scroll = self.camera.scroll
        for food in self.entity_activity.dict_food.values():
            render_pos = get_render_pos (food.grid_x, food.grid_y)
            self.screen.blit (food.get_scaled_food(), (render_pos[0] + map_block_tiles.get_width()/2 + scroll.x, render_pos[1] + map_block_tiles.get_height()/4 + scroll.y))
    
    # bob reproduces when the energy>=200                                                
    def reproduce(self): 
        self.entity_activity.reproduce()
    
    #sexual reproduction when both energy >= 150
    def sexual_reproduction(self):
        self.entity_activity.sexual_reproduction()

    # bob eat food
    def eat_food(self) :
        self.entity_activity.bob_eat_food()

    # bob die : lost all of energy
    def die(self):
        self.entity_activity.die()
    
    def draw_text(self):
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render('tick={}'.format(self.tick), True, (255,255,255))
        text_surface_day = font.render('day={}'.format(self.day), True, (255,255,255))
        text_rect = text_surface.get_rect(topleft=(0,0))
        text_rect_day = text_surface.get_rect(topleft=(1000,0))
        self.screen.blit (text_surface, text_rect)
        self.screen.blit (text_surface_day, text_rect_day)

    def get_target_new(self):
        self.entity_activity.get_target_new()
        
    def update_perception(self):
        self.entity_activity.update_perception()