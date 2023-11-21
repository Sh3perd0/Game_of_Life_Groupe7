from entity.bob import Bob
from entity.food import Food
import random

class EntityActivity :
    def __init__ (self, list_bob, dict_food):
        self.list_bob = list_bob
        self.dict_food = dict_food
    
    @staticmethod
    def check_collision (entity_1, entity_2):
        if (entity_1.grid_x == entity_2.grid_x and entity_1.grid_y == entity_2.grid_y):
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




    def reproduce(self):
        # Implement logic for reproduction
        for bob in self.list_bob:
            if bob.energy >= 200:
                bob.energy = 50
                bob1 = Bob()
                bob1.set_position(bob.grid_x, bob.grid_y)
                self.list_bob.append(bob1)
                bob1.energy = 50
                bob1.speed = round((random.uniform(bob.speed - 0.1, bob.speed + 0.1)), 2)

    def die(self):
        # Implement logic for Bob dying
        for bob in self.list_bob:
            if bob.energy <= 0:
                self.list_bob.remove(bob)