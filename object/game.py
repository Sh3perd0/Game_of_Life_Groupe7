import pygame
import sys
import random
from queue import PriorityQueue
from .map import Map
from camera.camera import Camera
from constant.settings import *
from entity.bob import Bob
from .common import *
from entity.food import Food
from entity.entity import Entity
from logic_game.entity_activity import EntityActivity
import pickle
import codecs
import analyses.global_var_analyse as gva
import constant.settings


class Game:
    def __init__(self, screen, clock):
        settings = load_settings()

        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.camera = Camera(self.width, self.height)
        self.map = Map(screen, GRID_SIZE, GRID_SIZE)
        self.map.render_map()
        self.entity_activity = EntityActivity()
        self.tick = 0
        self.day = 0

        # Set key repeat and event filter
        pygame.key.set_repeat(400, 30)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

    def load_settings():
        with open("constant/settings.json", "r") as file:
            settings = json.load(file)
        return settings

    # MAIN LOOP
    def run(self):
        self.playing = True
        # pygame.display.set_window_position(, )
        while self.playing:
            self.events()

            # display fps in title
            # pygame.display.set_caption('Game of Life - FPS: ' + str(int(self.clock.get_fps())))
            self.camera.update()
            self.draw()
            self.update_render_tick()
            self.clock.tick(FRAME_RATE)
            # self.clock.tick(1)

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
                    self.playing = False
                
    def load(self):
        with open("save.pkl", "rb") as file:
            self.entity_activity = pickle.load(file)

    def save(self):
        with open("save.pkl", "wb") as file:
            pickle.dump(self.entity_activity, file)

    def update_render_tick(self):
        # print(len(self.entity_activity.list_bob))
        self.update_list_bob()
        self.update_move_bob()
        self.eat_food()
        self.parthenogenesis_reproduce()
        self.sexual_reproduction()
        self.die()
        if self.newAnalyse() == -1:  # si on retourne 1, il n'y a plus de bob
            self.playing = False

        self.tick += 1
        if self.tick == TICK:
            self.tick = 0
            self.increment_day()

    def increment_day(self):
        self.entity_activity.create_dict_food()
        self.day += 1

    def draw(self):
        scroll = self.camera.scroll
        # self.screen.fill((0,0,0))
        self.screen.blit(self.map.block_tiles, (scroll.x, scroll.y))
        self.draw_food()
        self.draw_bob()
        self.draw_text()
        # self.map.render_map_camera(self.camera)
        pygame.display.update()

    def draw_bob(self):
        map_block_tiles = self.map.block_tiles
        scroll = self.camera.scroll

        image_bob = get_assets_img(BOB_IMAGE)
        # scaled_bob_image = get_scaled_image(image_bob, bob.get_pixel_bob_size())
        for bob in self.entity_activity.list_bob:
            render_pos = get_render_pos(bob.grid_x, bob.grid_y)
            self.screen.blit(
                get_scaled_image(image_bob, bob.get_pixel_bob_size()),
                (
                    render_pos[0] + map_block_tiles.get_width() / 2 + scroll.x,
                    render_pos[1] + map_block_tiles.get_height() / 4 + scroll.y,
                ),
            )

            # energy_text = bob.font.render(f'Position: {(bob.grid_x, bob.grid_y)}, Target: {bob.target}, Speed:{bob.total_speed:.2f}', True, (255, 255, 255))
            # text_rect = energy_text.get_rect(center=(render_pos[0] + map_block_tiles.get_width()/2 + scroll.x,
            #                                       render_pos[1] + map_block_tiles.get_height()/4 + scroll.y - 20))
            # self.screen.blit(energy_text, text_rect)
            # print(f'Position: {(bob.grid_x, bob.grid_y)}, Target: {bob.target}, Speed:{bob.total_speed:.2f}')

    # This version is for food with same size (faster)
    def draw_food(self):
        map_block_tiles = self.map.block_tiles
        scroll = self.camera.scroll

        image_food = get_assets_img(FOOD_IMAGE)
        scaled_food_image = get_scaled_image(image_food, Food.get_pixel_food_size())

        for food in self.entity_activity.dict_food.values():
            render_pos = get_render_pos(food.grid_x, food.grid_y)
            # Use the pre-rendered scaled food image
            self.screen.blit(
                scaled_food_image,
                (
                    render_pos[0] + map_block_tiles.get_width() / 2 + scroll.x,
                    render_pos[1] + map_block_tiles.get_height() / 4 + scroll.y,
                ),
            )

            # # Display the text of position to the screen
            # energy_text = food.font.render(f'P: {food.grid_x, food.grid_y}', True, (255, 255, 255))
            # text_rect = energy_text.get_rect(center=(render_pos[0] + map_block_tiles.get_width() / 2 + scroll.x,
            #                                         render_pos[1] + map_block_tiles.get_height() / 4 + scroll.y - 20))
            # self.screen.blit(energy_text, text_rect)

    # This version is for food with different size (slower)
    # def draw_food(self):
    #     map_block_tiles = self.map.block_tiles
    #     scroll = self.camera.scroll
    #     image_food = get_assets_img(FOOD_IMAGE)

    #     for food in self.dict_food.values() :
    #         render_pos = get_render_pos(food.grid_x, food.grid_y)
    #         self.screen.blit(get_scaled_image(image_food, food.get_pixel_food_size()),  (render_pos[0] + map_block_tiles.get_width()/2 + scroll.x,
    #                                                  render_pos[1] + map_block_tiles.get_height()/4 + scroll.y))

    def draw_text(self):
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render("tick={}".format(self.tick), True, (255, 255, 255))
        text_surface_day = font.render("day={}".format(self.day), True, (255, 255, 255))
        text_surface_fps = font.render(
            "fps={}".format(round(self.clock.get_fps())), True, (255, 255, 255)
        )
        # text_surface_game_tick = font.render('game_tick={}'.format(self.game_tick), True, (255,255,255))
        text_rect = text_surface.get_rect(topleft=(0, 0))
        text_rect_day = text_surface.get_rect(topleft=(0, 100))
        text_rect_fps = text_surface.get_rect(topleft=(0, 200))
        # text_rect_game_tick = text_surface.get_rect(topleft=(0, 100))
        self.screen.blit(text_surface, text_rect)
        self.screen.blit(text_surface_day, text_rect_day)
        self.screen.blit(text_surface_fps, text_rect_fps)
        # self.screen.blit (text_surface_game_tick, text_rect_game_tick)

    # bob parthenogenesis_reproduces when the energy>=200
    def parthenogenesis_reproduce(self):
        self.entity_activity.parthenogenesis_reproduce()

    # sexual reproduction when both energy >= 150
    def sexual_reproduction(self):
        self.entity_activity.sexual_reproduction()

    # bob eat food
    def eat_food(self):
        self.entity_activity.bob_eat_food()

    # bob die : lost all of energy
    def die(self):
        self.entity_activity.bob_die()

    def update_move_bob(self):
        self.entity_activity.move_towards_target()

    def newAnalyse(self):
        self.entity_activity.newAnalyse()

    def update_list_bob(self):
        self.entity_activity.list_bob = sorted(
            self.entity_activity.list_bob, key=lambda bob: bob.total_speed, reverse=True
        )
