from entity.bob import Bob
from entity.food import Food
import random
import pygame
from constant.grid_size import GRID_SIZE


class EntityActivity :
    def __init__ (self, list_bob, dict_food):
        self.list_bob = list_bob
        self.dict_food = dict_food
    
    @staticmethod
    def check_collision (entity_1, entity_2):
        if (entity_1.grid_x == entity_2.grid_x and entity_1.grid_y == entity_2.grid_y):
            return True
        return False
    
    # def check_food (bob, entity):
    #     if EntityActivity.check_collision(bob, entity):
    #         if entity is Food :
    #             return True
    #         else:
    #             if 
    def bob_eat_food(self):
        keys_to_remove = []
        for bob in self.list_bob:
            for grid, food in self.dict_food.items():
                if EntityActivity.check_collision(bob, food):
                    keys_to_remove.append(grid)
                    bob.energy += min(food.energy, 200 - bob.energy)

            for key in keys_to_remove:
                if key in self.dict_food:
                    del self.dict_food[key]

    # def bob_eat_bob(self):
    #     for bob1 in self.list_bob:
    #         for bob2 in self.list_bob:
                
    def reproduce(self):
        # Implement logic for reproduction
        for bob in self.list_bob:
            if bob.energy >= 200:
                bob.energy = 50
                bob1 = Bob()
                bob1.set_position(bob.grid_x, bob.grid_y)
                self.list_bob.append(bob1)
                bob1.energy = 50
                bob1.perception = bob.perception
                bob1.speed = round((random.uniform(bob.speed - 0.1, bob.speed + 0.1)), 2)
                bob1.mass = round((random.uniform(bob.speed - 0.1, bob.speed + 0.1)), 2)

    def die(self):
        # Implement logic for Bob dying
        for bob in self.list_bob:
            if bob.energy <= 0:
                self.list_bob.remove(bob)
                
    def get_target_new(self):
        for bob in self.list_bob:
            target = None
            min_distance = float('inf')

            for food_key in self.dict_food.keys():
                food = self.dict_food[food_key]
                distance_x = abs(food.grid_x - bob.grid_x)
                distance_y = abs(food.grid_y - bob.grid_y)
                
                if distance_x + distance_y < bob.perception and distance_x + distance_y < min_distance:
                    min_distance = distance_x + distance_y
                    target = (food.grid_x, food.grid_y)

            if target is not None:
                bob.target = pygame.Vector2(target[0], target[1])
            else:
                bob.target = pygame.Vector2(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            
    def update_perception(self):
        for bob in self.list_bob:
            match random.randint(1,3):
                case 1:
                    bob.perception+=1
                case 2:
                    if bob.perception > 0:
                        bob.perception-=1      
                        
                                     

                
            