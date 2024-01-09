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

    def parthenogenesis_reproduce(self):
        # Implement logic for reproduction via parthenogenesis:
        for bob in self.list_bob:
            if bob.energy >= 200:
                bob.energy = 50
                speed = max(
                    0, round((random.uniform(bob.speed - 0.1, bob.speed + 0.1)), 2)
                )
                mass = max(
                    0, round((random.uniform(bob.mass - 0.1, bob.mass + 0.1)), 2)
                )
                bob1 = Bob(speed=speed, energy=50, perception=bob.perception, mass=mass)
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

    def bob_die(self):
        # Implement logic for Bob dying:
        for bob in self.list_bob:
            if bob.energy <= 0:
                self.list_bob.remove(bob)

    # Set new target each tick
    def set_new_target(self):
        for bob in self.list_bob:
            target = None
            min_distance = float("inf")
            min_mass = float("inf")

            # Find the nearest food
            for food in self.dict_food.values():
                distance = abs(food.grid_x - bob.grid_x) + abs(food.grid_y - bob.grid_y)
                if distance < bob.perception:
                    if distance < min_distance:
                        min_distance = distance
                        target = pygame.Vector2(food.grid_x, food.grid_y)
                        food_target_energy = food.energy

                    # Greater food preference
                    if distance == min_distance:
                        if food.energy > food_target_energy:
                            target = pygame.Vector2(food.grid_x, food.grid_y)
                            food_target_energy = food.energy

            # Find the smallest bob
            if min_distance == float("inf"):
                for bob1 in self.list_bob:
                    distance_1 = abs(bob1.grid_x - bob.grid_x) + abs(
                        bob1.grid_y - bob.grid_y
                    )
                    if bob.mass > 3 / 2 * bob1.mass and distance_1 < bob.perception:
                        if bob1.mass < min_mass:
                            min_mass = bob1.mass
                            target = pygame.Vector2(bob1.grid_x, bob1.grid_y)

            if target is not None:
                bob.target = pygame.Vector2(target[0], target[1])
            else:
                bob.target = pygame.Vector2(
                    random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
                )

    # Update perception each tick
    def update_perception(self):
        for bob in self.list_bob:
            if bob.perception > 0:
                rand_num = random.randint(-1, 1)
                bob.perception += rand_num
            elif bob.perception <= 0:
                bob.perception += random.choice([0, 1])

    def bob_eat_bob(self):
        for bob1 in self.list_bob:
            for bob2 in self.list_bob:
                if bob1.mass > 3 / 2 * bob2.mass:
                    bob1.energy = bob1.energy + 1 / 2 * bob2 * (
                        1 - bob2.mass / bob1.mass
                    )
                    bob2.energy = 0
