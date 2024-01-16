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


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.camera = Camera(self.width, self.height)
        self.map = Map(screen, GRID_SIZE, GRID_SIZE)
        self.map.render_map()
        # since Bob's priority order of action depends on velocity 
        # we use the data structure of priority queue  (velocity) to store the bob
        # priority queue  : pq_bob
        self.pq_bob = self.create_pq_bob()
        self.dict_food = self.create_dict_food()
        self.entity_activity = EntityActivity(self.list_bob, self.dict_food)
        self.tick = 0
        self.day = 0

        # Set key repeat and event filter
        pygame.key.set_repeat(400, 30)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

    # MAIN LOOP
    def run(self):
        self.playing = True
        # pygame.display.set_window_position(, )
        while self.playing:
            self.clock.tick(FRAME_RATE)
            self.events()
            self.camera.update()
            self.draw()
            self.update_render_tick()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update_render_tick(self):
        self.update_move_bob()
        self.eat_food()
        self.parthenogenesis_reproduce()
        self.sexual_reproduction()
        self.die()
        self.set_new_target()
        self.update_perception()

        self.tick += 1
        if self.tick == TICK:
            self.tick = 0
            self.increment_day()

    def increment_day(self):
        self.dict_food = self.create_dict_food().copy()
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

        for bob in self.list_bob:
            render_pos = get_render_pos(bob.grid_x, bob.grid_y)
            self.screen.blit(
                get_scaled_image(image_bob, bob.get_pixel_bob_size()),
                (
                    render_pos[0] + map_block_tiles.get_width() / 2 + scroll.x,
                    render_pos[1] + map_block_tiles.get_height() / 4 + scroll.y,
                ),
            )
            # energy_text = bob.font.render(f'E: {bob.energy}, P: {bob.perception}, T: {bob.target}, IV: {bob.speed}, TV:{bob.total_speed:.2f}', True, (255, 255, 255))
            # text_rect = energy_text.get_rect(center=(render_pos[0] + map_block_tiles.get_width()/2 + scroll.x,
            #                                       render_pos[1] + map_block_tiles.get_height()/4 + scroll.y - 20))
            # self.screen.blit(energy_text, text_rect)



    def create_pq_bob(self):
        self.pq_bob = PriorityQueue()
        for bob in self.pq_bob:
            # Use a tuple with priority as the first element, and Bob as the second
            # Higher values have higher priority
            heapq.heappush(self.pq_bob, (-bob.priority, bob))

    def update_move_bob(self):
        for bob in self.list_bob:
            bob.move_towards_target()

    def create_dict_food(self):
        dict_food = {}
        for _ in range(NUMBER_FOOD):
            food = Food()
            food.set_position()
            position = (food.grid_x, food.grid_y)
            if position in dict_food:
                dict_food[position].energy += DEFAULT_ENERGY
            else:
                dict_food[position] = food
        return dict_food

    # This version is for food with same size (faster)
    def draw_food(self):
        map_block_tiles = self.map.block_tiles
        scroll = self.camera.scroll

        image_food = get_assets_img(FOOD_IMAGE)
        scaled_food_image = get_scaled_image(image_food, Food.get_pixel_food_size())

        for food in self.dict_food.values():
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

    def set_new_target(self):
        self.entity_activity.set_new_target()

    def update_perception(self):
        self.entity_activity.update_perception()

    def bob_eat_bob(self):
        self.entity_activity.bob_eat_bob()
