from entity.bob import Bob
from entity.food import Food
import random
import pygame
from constant.settings import *


class EntityActivity:
    def __init__(self, list_bob, dict_food):
        self.list_bob = list_bob
        self.dict_food = dict_food

    @staticmethod
    def check_collision(entity_1, entity_2):
        if entity_1.grid_x == entity_2.grid_x and entity_1.grid_y == entity_2.grid_y:
            return True
        return False

    # def bob_eat_food(self):
    #     keys_to_remove = []
    #     for bob in self.list_bob:
    #         for grid, food in self.dict_food.items():
    #             if EntityActivity.check_collision(bob, food):
    #                 keys_to_remove.append(grid)
    #                 bob.energy += min(food.energy, 200 - bob.energy)

    #         for key in keys_to_remove:
    #             if key in self.dict_food:
    #                 del self.dict_food[key]
    # Implement logic for reproduction via parthenogenesis:
    def parthenogenesis_reproduce(self):
        for bob in self.list_bob:
            if bob.energy >= 200:
                bob.energy = 50
                speed = max(0, round((random.uniform(bob.speed - 0.1, bob.speed + 0.1)), 2))
                mass = max(0, round((random.uniform(bob.mass - 0.1, bob.mass + 0.1)), 2))
                perception = bob.perception
                if perception > 0:
                    rand_num = random.randint(-1, 1)
                    perception += rand_num
                elif perception <= 0:
                    perception += random.choice([0, 1])
                bob1 = Bob(speed=speed, energy=50, perception=perception, mass=mass)
                bob1.set_position(bob.grid_x, bob.grid_y)
                self.list_bob.append(bob1)

    def sexual_reproduction(self):
        for bob1 in self.list_bob:
            for bob2 in self.list_bob:
                if bob1 != bob2:
                    if self.check_collision(bob1, bob2):
                        if (bob1.energy >= ENERGY_TO_REPRODUCE) and (
                            bob2.energy >= ENERGY_TO_REPRODUCE
                        ):
                            print("naissance")
                            bob2.set_energy(bob2.energy - LOSE_ENERGY_AFTER_SEX)
                            baby = Bob(
                                speed=(bob1.speed + bob2.speed) / 2,
                                energy=NEW_ENERGY_REPRODUCE,
                                perception=(bob1.perception + bob2.perception) / 2,
                                mass=(bob1.mass + bob2.mass) / 2,
                            )
                            baby.set_position(bob1.grid_x, bob1.grid_y)
                            self.list_bob.append(baby)

    # def bob_die(self):
    #     # Implement logic for Bob dying:
    #     for bob in self.list_bob:
    #         if bob.energy <= 0:
    #             self.list_bob.remove(bob)
                
    
    
    # # Set new target each unit of movement
    # def set_new_target(self):
    #     for bob in self.list_bob:
    #         target = None
    #         food_target = self.find_food((0,0,GRID_SIZE,GRID_SIZE), bob)
    #         bob_target = self.find_smallest_bob((0,0,GRID_SIZE,GRID_SIZE), bob)
    #         big_bob = self.find_biggest_bob((0,0,GRID_SIZE,GRID_SIZE),bob) 
            
    #         if not big_bob:
    #             if food_target:
    #                 target = pygame.Vector2(food_target.grid_x, food_target.grid_y)
    #             elif bob_target:
    #                 target = pygame.Vector2(bob_target.grid_x, bob_target.grid_y)
    #         else:
    #             pass
            
    #         if target is not None:
    #             bob.target = pygame.Vector2(target[0], target[1])
    #         else:
    #             bob.target = pygame.Vector2(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))


    # def bob_eat_bob(self):
    #     for bob1 in self.list_bob:
    #         for bob2 in self.list_bob:
    #             if bob1.mass > 3 / 2 * bob2.mass:
    #                 bob1.energy = bob1.energy + 1 / 2 * bob2 * (
    #                     1 - bob2.mass / bob1.mass
    #                 )
    #                 bob2.energy = 0
    
    # #find smallest_bob
    # def find_smallest_bob(self,rectangle_corners, bob):
    #     # Extract coordinates of rectangle corners
    #     x1, y1, x2, y2 = rectangle_corners
    #     bob_target=None
    #     # Filter foods within the specified rectangle
    #     bobs_in_rectangle = (bob for bob in self.list_bob if (x1 <= bob.grid_x <= x2 and y1 <= bob.grid_y <= y2))
    #     if not bobs_in_rectangle:
    #         return None  # No food in the specified rectangle
    #     for bob1 in bobs_in_rectangle:
    #         distance_1 = abs(bob1.grid_x - bob.grid_x) + abs(bob1.grid_y - bob.grid_y)
    #         if bob.mass > 3/2 * bob1.mass and distance_1 < bob.perception:
    #             if not bob_target:
    #                 distance_to_target = distance_1
    #                 bob_target = bob1
    #             elif bob1.mass < bob_target.mass:
    #                 distance_to_target = distance_1
    #                 bob_target = bob1
    #             elif bob1.mass == bob_target.mass:
    #                 if distance_1 < distance_to_target:
    #                     distance_to_target = distance_1
    #                     bob_target=bob1
    #     return bob_target

    # #find food in area 
    # def find_food(self, rectangle_corners, bob):
    #     # Extract coordinates of rectangle corners
    #     x1, y1, x2, y2 = rectangle_corners
    #     min_distance = float('inf')
    #     food_target = None
    #     # Filter foods within the specified rectangle
    #     foods_in_rectangle = (food for food in self.dict_food.values() if (x1 <= food.grid_x <= x2 and y1 <= food.grid_y <= y2))
    #     if not foods_in_rectangle:
    #         return None  # No food in the specified rectangle
    #     for food in foods_in_rectangle:
    #         distance = abs(food.grid_x - bob.grid_x) + abs(food.grid_y - bob.grid_y)
    #         if distance < bob.perception:
    #             if distance < min_distance:
    #                 min_distance = distance
    #                 food_target = food
    #             if distance == min_distance:
    #                 if food.energy > food_target.energy:
    #                     food_target = food
    #     return food_target
    
                    
    
    # #find biggest bob
    # def find_biggest_bob(self,rectangle_corners, bob):
    #     # Extract coordinates of rectangle corners
    #     x1, y1, x2, y2 = rectangle_corners
    #     bob_biggest=None
    #     # Filter foods within the specified rectangle
    #     bobs_in_rectangle = (bob for bob in self.list_bob if (x1 <= bob.grid_x <= x2 and y1 <= bob.grid_y <= y2))
    #     if not bobs_in_rectangle:
    #         return None  # No food in the specified rectangle
    #     for bob1 in bobs_in_rectangle:
    #         distance_1 = abs(bob1.grid_x - bob.grid_x) + abs(bob1.grid_y - bob.grid_y)
    #         if bob1.mass > 3/2 * bob.mass and distance_1 < bob.perception:
    #             if not bob_biggest:
    #                 bob_biggest = bob1
    #             elif bob1.mass > bob_biggest.mass:
    #                 bob_biggest = bob1
    #     return bob_biggest
    
    
    #move_towards_target
    def move_towards_target(self):
        for bob in self.list_bob:
            
            # Calculate the difference between Bob's position and the target position
            dx = bob.target[0] - bob.grid_x
            dy = bob.target[1] - bob.grid_y

            if dx != 0 or dy != 0:
                bob.energy = max(
                    0,
                    bob.energy - ((bob.speed**2) * bob.mass + 1 / 5 * bob.perception),
                )

                # Adjust Bob's position based on speed
                for _ in range(int(bob.total_speed)):
                    dx = bob.target[0] - bob.grid_x
                    dy = bob.target[1] - bob.grid_y
                    
                    dx_direction = 0
                    dy_direction = 0

                    if dx != 0 or dy != 0:
                        if dx == 0:
                            dy_direction = 1 if dy > 0 else -1
                        elif dy == 0:
                            dx_direction = 1 if dx > 0 else -1
                        else:
                            dir = random.randint(0, 1)
                            if dir == 0:
                                dx_direction = 1 if dx > 0 else -1
                            else:
                                dy_direction = 1 if dy > 0 else -1

                        dx -= dx_direction
                        dy -= dy_direction

                        # Move Bob
                        bob.move(dx_direction, dy_direction)
                        
                        self.set_new_target()
            else:
                bob.energy = max( 0, bob.energy - 0.5)

            bob.update_speed()

    
    #set new target
    def set_new_target(self):
        for bob in self.list_bob:
            