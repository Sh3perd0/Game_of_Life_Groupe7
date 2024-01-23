from entity.bob import Bob
from entity.food import Food
import random
import pygame
import bisect
from constant.settings import *
from object.map import Map

class EntityActivity:
    def __init__ (self, map):
        self.map = map
        # since Bob's priority order of action depends on spped
        # we need to sort the list according to speed
        self.list_bob = []
        self.create_list_bob()
        self.dict_food = []
        self.create_dict_food()
        

    @staticmethod
    def check_collision(entity_1, entity_2):
        if entity_1.grid_x == entity_2.grid_x and entity_1.grid_y == entity_2.grid_y:
            return True
        return False
    
    # After a day: reset all the cell as not occupied by food
    def reset_occupied_by_food(self):
        if self.dict_food:
            for food in self.dict_food.values():
                self.map.map_dict[(food.grid_x, food.grid_y)].occupied_by_food = False

    def create_list_bob(self):
        list_bob = [Bob() for _ in range(NUMBER_BOB)]
        # Sort the list in descending order by bob.speed
        self.list_bob = sorted(list_bob, key=lambda bob: bob.speed, reverse=True)
    
    def create_dict_food (self):
        self.reset_occupied_by_food()
        dict_food = {}
        for _ in range (NUMBER_FOOD):
            food = Food()
            food.set_position()
            position = (food.grid_x, food.grid_y)
            self.map.map_dict[position].occupied_by_food = True
            if  position in dict_food:
                dict_food[position].energy += 100
            else:
                dict_food[position] = food
        self.dict_food = dict_food.copy()

    
    # append bob to list_bob in order
    def append_bob_to_list(self, bob):
        bisect.insort(self.list_bob, bob, key=lambda x: x.speed)

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

    # Implement logic for reproduction via parthenogenesis:
    def parthenogenesis_reproduce(self):
        for bob in self.list_bob:
            if bob.energy >= MAX_ENERGY:
                bob.energy = NEW_ENERGY_PARTH_REPRODUCE
                speed = max(0, round((random.uniform(bob.speed - 0.1, bob.speed + 0.1))))
                mass = max(0, round((random.uniform(bob.mass - 0.1, bob.mass + 0.1))))
                perception = bob.perception
                if perception > 0:
                    rand_num = random.randint(-1, 1)
                    perception += rand_num
                elif perception <= 0:
                    perception += random.choice([0, 1])
                baby = Bob(speed=speed, energy= NEW_ENERGY_PARTH_REPRODUCE, perception=perception, mass=mass)
                baby.set_position(bob.grid_x, bob.grid_y)
                self.append_bob_to_list(baby)
                # print(f"Baby born SINGLE with perception = {baby.perception}")
        

    def sexual_reproduction(self):
        for bob1 in self.list_bob:
            for bob2 in self.list_bob:
                if bob1 != bob2:
                    if self.check_collision(bob1, bob2):
                        if (bob1.energy >= ENERGY_TO_REPRODUCE) and (
                            bob2.energy >= ENERGY_TO_REPRODUCE
                        ):
                            bob2.set_energy(bob2.energy - LOSE_ENERGY_AFTER_SEX)
                            bob1.set_energy(bob1.energy - LOSE_ENERGY_AFTER_SEX)
                            baby = Bob(
                                speed=(bob1.speed + bob2.speed) / 2,
                                energy=NEW_ENERGY_SEXUAL_REPRODUCE,
                                perception=(bob1.perception + bob2.perception) / 2,
                                mass=(bob1.mass + bob2.mass) / 2,
                            )
                            baby.set_position(bob1.grid_x, bob1.grid_y)
                            print(f"Baby born SEXUAL with perception = {baby.perception}")
                            self.append_bob_to_list(baby)
    

    def bob_die(self):
        # Implement logic for Bob dying:
        for bob in self.list_bob:
            if bob.energy <= 0:
                # print(f"Bob is dead at energy = {bob.energy}")
                self.list_bob.remove(bob)
                
                
    def bob_eat_prey(self):
        for bob in self.list_bob:
            for prey in self.list_bob:
                if EntityActivity.check_collision(bob, prey) and bob.is_predator(prey)  and bob != prey:
                    print ("Bob eat prey")
                    bob.energy += 1 / 2 * prey.energy * (
                        1 - prey.mass / bob.mass
                    )
                    prey.energy = 0
                    
    
    
    def vision_area (self, bob):
        vision_area = (max(0, bob.grid_x - int(bob.perception)), 
                      min(GRID_SIZE, bob.grid_x + int(bob.perception)), 
                      max(0, bob.grid_y - int(bob.perception)), 
                      min(GRID_SIZE, bob.grid_y + int(bob.perception)))
        return vision_area
    
    #Find prey
    def find_prey(self,rectangle_corners, bob):
        # Extract coordinates of rectangle corners
        x1, y1, x2, y2 = rectangle_corners
        prey_target=None
        min_distance = float('inf')
        # Filter preys within the specified rectangle
        preys_in_rectangle = (prey for prey in self.list_bob if (bob.is_predator(prey) and x1 <= prey.grid_x <= x2 and y1 <= prey.grid_y <= y2))
        if not preys_in_rectangle:
            return None  # No prey in the specified rectangle
        for prey in preys_in_rectangle:
            distance = abs(prey.grid_x - bob.grid_x) + abs(prey.grid_y - bob.grid_y)

            if distance < bob.perception:
                if distance < min_distance or (distance == min_distance and 
                    prey.mass < prey_target.mass):

                    min_distance = distance
                    prey_target = prey
        return prey_target

    # Find food
    def find_food(self, rectangle_corners, bob):
        # Extract coordinates of rectangle corners
        x1, y1, x2, y2 = rectangle_corners
        min_distance = float('inf')
        food_target = None
        # Filter foods within the specified rectangle
        foods_in_rectangle = (food for food in self.dict_food.values() if (x1 <= food.grid_x <= x2 and y1 <= food.grid_y <= y2))
        if not foods_in_rectangle:
            return None  # No food in the specified rectangle
        for food in foods_in_rectangle:
            distance = abs(food.grid_x - bob.grid_x) + abs(food.grid_y - bob.grid_y)

            if distance <= int(bob.perception):
                if distance < min_distance or (distance == min_distance and 
                    food.energy > food_target.energy):
                    
                    min_distance = distance
                    food_target = food
        return food_target

    # Find predator
    def find_predator(self, rectangle_corners, bob):
        # Extract coordinates of rectangle corners
        x1, y1, x2, y2 = rectangle_corners
        min_distance = float('inf')  # Initialize min_distance to infinity
        predator_target = []
        # Filter predators within the specified rectangle
        predators_in_rectangle = [predator for predator in self.list_bob if (bob.is_prey(predator) and x1 <= predator.grid_x <= x2 and y1 <= predator.grid_y <= y2)]
        if not predators_in_rectangle:
            return None  # No predator in the specified rectangle
        for predator in predators_in_rectangle:
            distance = abs(predator.grid_x - bob.grid_x) + abs(predator.grid_y - bob.grid_y)
            if distance <= int(bob.perception):
                if distance < min_distance:
                    min_distance = distance
                    predator_target = [predator]  # Found a closer predator
                elif distance == min_distance:
                    predator_target.append(predator)  # Found another predator at the same minimum distance
        return predator_target
    
    
    #move_towards_target
    def move_towards_target(self):
        for i, bob in enumerate(self.list_bob):
            
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
                        
                        outer_loop_break = False

                        # Check if Bob meets food at the new position
                        if self.map.map_dict[(bob.grid_x, bob.grid_y)].occupied_by_food:
                            outer_loop_break = True
                            print (f"Bob with current speed = {bob.total_speed} eat food and stop moving")
                        # Check if Bob meets prey at the new position
                        for other_bob in self.list_bob[i+1:]:
                            if EntityActivity.check_collision(bob, other_bob) and bob.is_predator(other_bob) and bob != other_bob:
                                outer_loop_break = True
                                print(f"Bob with current speed = {bob.total_speed} eat prey and stop moving")
                                break
                        if outer_loop_break:
                            break
                        
            else:
                bob.energy = max( 0, bob.energy - 0.5)
                self.set_new_target()

            bob.update_speed()


        
    
    # Set new target each unit of movement
    def set_new_target(self):
        for bob in self.list_bob:
            target = None
            food_target = self.find_food(self.vision_area(bob), bob)
            prey_target = self.find_prey(self.vision_area(bob), bob)
            predator_target = self.find_predator(self.vision_area(bob),bob) 
            
            if not predator_target:
                if food_target:
                    target = pygame.Vector2(food_target.grid_x, food_target.grid_y)
                elif prey_target:
                    target = pygame.Vector2(prey_target.grid_x, prey_target.grid_y)
            else:
                pass
            
            if target is not None:
                bob.target = pygame.Vector2(target[0], target[1])
            else:
                # bob.target = pygame.Vector2(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
                bob.target = pygame.Vector2(random.randint(max(0, bob.grid_x - 1), min(bob.grid_x + 1, GRID_SIZE - 1)), 
                                                           random.randint(max(0, bob.grid_y - 1), min(bob.grid_y + 1, GRID_SIZE - 1)))
                # print (bob.target)
            