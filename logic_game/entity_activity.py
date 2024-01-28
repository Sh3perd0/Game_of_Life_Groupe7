from entity.bob import Bob
from entity.food import Food
import random
import pygame
import bisect 
from constant.settings import *
import analyses.global_var_analyse as gva

class EntityActivity:
    def __init__ (self):
        reload_settings()
        # since Bob's priority order of action depends on speed
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
    

    def create_list_bob(self):
        self.list_bob = [Bob() for _ in range(NUMBER_BOB)]
    
    def create_dict_food (self):
        dict_food = {}
        for _ in range (NUMBER_FOOD):
            food = Food()
            food.set_position()
            position = (food.grid_x, food.grid_y)
            if  position in dict_food:
                dict_food[position].energy += 100
            else:
                dict_food[position] = food
        self.dict_food = dict_food.copy()

    
    # append bob to list_bob in order
    def append_bob_to_list(self, bob):
        #bisect.insort(self.list_bob, bob, key=lambda x: x.total_speed)
        # Créer une liste des vitesses pour trouver la position d'insertion
        speeds = [x.speed for x in self.list_bob]
        # Trouver l'index où bob doit être inséré
        index = bisect.bisect_right(speeds, bob.speed)
        # Insérer bob à cet index dans la liste originale
        self.list_bob.insert(index, bob)

    def bob_eat_food(self):
        keys_to_remove = []
        for bob in self.list_bob:
            for grid, food in self.dict_food.items():
                if EntityActivity.check_collision(bob, food):
                    keys_to_remove.append(grid)
                    bob.energy += min(food.energy, 200 - bob.energy)
                    gva.nb_food_eat+=1

            for key in keys_to_remove:
                if key in self.dict_food:
                    del self.dict_food[key]

    # Implement logic for reproduction via parthenogenesis:
    def parthenogenesis_reproduce(self):
            for bob in self.list_bob:
                if bob.energy >= MAX_ENERGY:
                    bob.energy = NEW_ENERGY_PARTH_REPRODUCE
                    speed = max(
                        0, round((random.uniform(bob.speed - 0.1, bob.speed + 0.1)))
                    )
                    mass = max(0, round((random.uniform(bob.mass - 0.1, bob.mass + 0.1))))
                    memory = max(0, (bob.memory + random.randint(-1, 1)))
                    perception = bob.perception
                    if perception > 0:
                        rand_num = random.randint(-1, 1)
                        perception += rand_num
                    elif perception <= 0:
                        perception += random.choice([0, 1])
                    baby = Bob(
                        speed=speed,
                        energy=NEW_ENERGY_PARTH_REPRODUCE,
                        perception=perception,
                        true_perception=perception,
                        mass=mass,
                        memory=memory,
                    )
                    baby.set_position(bob.grid_x, bob.grid_y)
                    self.append_bob_to_list(baby)
                    print(f"Baby born SINGLE with perception = {baby.perception}")
                gva.nb_descendant+=1
        

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
                                true_perception=(
                                    bob1.true_perception + bob2.true_perception
                                )
                                / 2,
                                perception=round(
                                    (bob1.perception + bob2.perception) / 2
                                ),
                                mass=(bob1.mass + bob2.mass) / 2,
                                memory=int((bob1.memory + bob2.memory) / 2),
                            )
                            baby.set_position(bob1.grid_x, bob1.grid_y)
                            print(
                                f"Baby born SEXUAL with perception = {baby.perception}"
                            )
                            self.append_bob_to_list(baby)
                            gva.nb_descendant+=1
    

    def bob_die(self):
        # Implement logic for Bob dying:
        for bob in self.list_bob:
            if bob.energy <= 0:
                # print(f"Bob is dead at energy = {bob.energy}")
                gva.bob_time_life.append(gva.time - bob.birthTick)
                self.list_bob.remove(bob)

                
                
    # Bob eat food and prey
    def bob_eat_food(self):
        keys_to_remove = []
        for bob in self.list_bob:
            if self.dict_food.get((bob.grid_x, bob.grid_y)):
                food = self.dict_food.get((bob.grid_x, bob.grid_y))
                keys_to_remove.append((food.grid_x, food.grid_y))
                bob.energy += min(food.energy, 200 - bob.energy)
                print("Bob eat food")
            else:
                for prey in self.list_bob:
                    if bob.is_predator(prey) and bob != prey:
                        bob.energy += min(
                            200, 1 / 2 * prey.energy * (1 - prey.mass / bob.mass)
                        )
                        prey.energy = 0
                        print("Bob eat prey")
            for key in keys_to_remove:
                if key in self.dict_food:
                    del self.dict_food[key]

    # Set up vision area
    def vision_area(self, bob):
        vision_area = []
        # Determine the range of left and right boundaries
        min_x = max(0, bob.grid_x - bob.perception)
        max_x = min(GRID_SIZE - 1, bob.grid_x + bob.perception)
        # Determine the limit range of the upper and lower boundaries
        min_y = max(0, bob.grid_y - bob.perception)
        max_y = min(GRID_SIZE - 1, bob.grid_y + bob.perception)
        # Loop through the coordinates within the bounded range and add them to vision_area
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if abs(bob.grid_x - x) + abs(bob.grid_x - x) <= bob.perception:
                    vision_area.append((x, y))
        return vision_area

    
    # Find prey
    def find_prey(self, area, bob):
        # Extract coordinates of rectangle corners
        prey_target = None
        min_distance = float("inf")

        for prey in self.list_bob:
            if (prey.grid_x, prey.grid_y) in area and bob.is_predator(prey):
                distance = bob.distance_to(prey)

                if distance < bob.perception:
                    if distance < min_distance or (
                        distance == min_distance and prey.mass < prey_target.mass
                    ):
                        min_distance = distance
                        prey_target = prey
        return prey_target

    # Find food
    def find_food(self, area, bob):
        # Extract coordinates of rectangle corners
        min_distance = float("inf")
        food_target = None

        for food_position in area:
            food = self.dict_food.get(food_position)
            if food:
                distance = bob.distance_to(food)
                # Here: when bob is in the same position with food, distance = 0
                # since the function find_food is called before eat_food
                # so he set this current food as food_target and then new_target = food_target
                # so after eating this food in the next tick he will station at this position 
                # So we add 2 lines of code below to avoid this situation
                if distance == 0:
                    continue

                if distance <= bob.perception:
                    if distance < min_distance or (
                        distance == min_distance and food.energy > food_target.energy
                    ):
                        min_distance = distance
                        food_target = food
        return food_target

    # Find predator
    def find_predator(self, area, bob):
        # Extract coordinates of rectangle corners
        min_distance = float("inf")  # Initialize min_distance to infinity
        predator_target = None

        for predator in self.list_bob:
            if bob.is_prey(predator) and (predator.grid_x, predator.grid_y) in area:
                distance = bob.distance_to(predator)
                if distance <= bob.perception:
                    if distance < min_distance:
                        min_distance = distance
                        predator_target = [predator]  # Found a closer predator
                    elif distance == min_distance:
                        predator_target.append(
                            predator
                        )  # Found another predator at the same minimum distance
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
                    bob.energy - ((bob.speed**2) * bob.mass + 1 / 5 * bob.perception + 1 / 5 * bob.memory),
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
                        
                        # print(f"{(bob.grid_x, bob.grid_y)} move to {bob.target}")

                        # Check if Bob meets food at the new position
                        if self.dict_food.get((bob.grid_x, bob.grid_y)):
                            # print(f"Bob found food at {(bob.grid_x, bob.grid_y)}")
                            break

                        outer_loop = False
                        # Check if Bob meets prey at the new position
                        for other_bob in self.list_bob[i+1:]:
                            if EntityActivity.check_collision(bob, other_bob) and bob.is_predator(other_bob) and bob != other_bob:
                                outer_loop = True
                                break
                        if outer_loop:
                            break
                    # else:
                    #     print("station")
             
            else:
                bob.energy = max( 0, bob.energy - 0.5)
                self.set_new_target()
                # print ("station")

            bob.update_speed()


    def newAnalyse(self):
        gva.time+=1
        masse=0
        energy=0
        speed=0
        perception = 0
        pop_bob = len(self.list_bob)
        if pop_bob!=0:
            for bob in self.list_bob:
                masse += bob.mass
                energy += bob.energy
                speed+= bob.speed
                perception += bob.perception
            masse = masse/pop_bob
            energy = energy/pop_bob
            speed = energy/pop_bob
            perception = perception/pop_bob
            gva.newValue(gva.time, masse,energy,speed,pop_bob, perception)
            return 0
        else:
            return -1


    
    # Set new target each unit of movement
    def set_new_target(self):
        for bob in self.list_bob:
            target = None
            food_target = self.find_food(self.vision_area(bob), bob)
            prey_target = self.find_prey(self.vision_area(bob), bob)
            predator_target = self.find_predator(self.vision_area(bob), bob)

            bob.set_perceived_food(set([f for f in self.dict_food.values() if bob.distance_to(f) <= bob.perception]))
            
            if not predator_target:
                if food_target:
                    target = pygame.Vector2(food_target.grid_x, food_target.grid_y)
                elif prey_target:
                    target = pygame.Vector2(prey_target.grid_x, prey_target.grid_y)
                else:
                    target = bob.target_from_memory()
            else:
                area = []

                for x, y in self.vision_area(bob):
                    cell_visible = True
                    for bob_predator in predator_target:
                        if (bob.grid_y - bob_predator.grid_y) * (
                            bob.grid_y - y
                        ) > 0 or (bob.grid_x - bob_predator.grid_x) * (
                            bob.grid_x - x
                        ) > 0:
                            cell_visible = False
                            break  # No need to check further if one predator is in this area
                    if cell_visible:
                        area.append((x, y))
                target = random((x, y) in area)

            if target is not None:
                bob.target = pygame.Vector2(target[0], target[1])
            else:
                # bob.target = pygame.Vector2(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
                bob.target = pygame.Vector2(
                    random.randint(
                        max(0, bob.grid_x - 1), min(bob.grid_x + 1, GRID_SIZE - 1)
                    ),
                    random.randint(
                        max(0, bob.grid_y - 1), min(bob.grid_y + 1, GRID_SIZE - 1)
                    ),
                )
                # print (f"Random target {bob.target}")
            # print (food_target)
            # print (prey_target)
