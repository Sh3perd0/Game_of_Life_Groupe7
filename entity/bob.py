import pygame
import random

from constant.settings import *
from object.common import *
from entity.entity import Entity


class Bob(Entity):
    def __init__(self, speed=DEFAULT_SPEED, energy=DEFAULT_ENERGY, perception=DEFAULT_PERCEPTION, mass=DEFAULT_MASS):
        super().__init__(energy)
        self.set_initial_position()
        self.speed = speed
        self.total_speed = self.speed
        self.target = (
            random.randint(0, GRID_SIZE - 1),
            random.randint(0, GRID_SIZE - 1),
        )
        self.perception = perception
        self.mass = mass
        self.volume = self.mass ** (1 / 3)
        self.speed_buffer = float(self.total_speed - int(self.total_speed))

    def set_mass_volume(self, mass):
        self.mass = mass
        self.volume = self.mass ** (1 / 3)

    def set_speed(self, speed):
        self.speed = speed

    def set_perception(self, perception):
        self.perception = perception

    def set_energy(self, energy=DEFAULT_ENERGY):
        self.energy = energy

    def set_initial_position(self):
        self.grid_x = random.randint(0, GRID_SIZE - 1)
        self.grid_y = random.randint(0, GRID_SIZE - 1)

    def set_position(self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y

    def move(self, dx, dy):
        self.grid_x += dx
        self.grid_y += dy
        # Keep track of the movement history
        # self.history.append((self.grid_x, self.grid_y))

    def update_speed(self):
        self.total_speed = self.speed + self.speed_buffer
        self.speed_buffer = self.total_speed - int(self.total_speed)

    # the given bob is the prey
    def is_predator (self, bob):
        if self.mass > 3/2 * bob.mass:
            return True
        else:
            return False
        
    def is_prey (self, bob):
        if self.mass < 2/3 * bob.mass:
            return True
        else:
            return False
    # def move_towards_target(self):
    #     # Calculate the difference between Bob's position and the target position
    #     dx = self.target[0] - self.grid_x
    #     dy = self.target[1] - self.grid_y

    #     if dx != 0 or dy != 0:
    #         self.energy = max(
    #             0,
    #             self.energy - ((self.speed**2) * self.mass + 1 / 5 * self.perception)
    #         )

    #         # Adjust Bob's position based on speed
    #         for _ in range(int(self.total_speed)):
    #             dx_direction = 0
    #             dy_direction = 0

    #             if dx != 0 or dy != 0:
    #                 if dx == 0:
    #                     dy_direction = 1 if dy > 0 else -1
    #                 elif dy == 0:
    #                     dx_direction = 1 if dx > 0 else -1
    #                 else:
    #                     dir = random.randint(0, 1)
    #                     if dir == 0:
    #                         dx_direction = 1 if dx > 0 else -1
    #                     else:
    #                         dy_direction = 1 if dy > 0 else -1

    #                 dx -= dx_direction
    #                 dy -= dy_direction

    #                 # Move Bob
    #                 self.move(dx_direction, dy_direction)
    #     else:
    #         self.energy = max( 0, self.energy - 0.5)

    #     self.update_speed()

    # @staticmethod
    # def get_assets_img():

    #     tile = pygame.image.load (
    #             os.path.abspath(
    #                 os.path.join(os.path.dirname(__file__), "..", "assets", "Bob.png")
    #             )).convert_alpha()

    #     return tile

    def get_pixel_bob_size(self):
        return 321 / 8 * self.volume, 25 / 2 * self.volume

    # def get_scaled_bob(self,
    #     width_pixel_size=None, height_pixel_size=None
    # ):  # pragma: no cover
    #     if width_pixel_size is None or height_pixel_size is None:
    #         width_pixel_size, height_pixel_size = self.get_pixel_bob_size()
    #     return pygame.transform.smoothscale(self.get_assets_img(),(width_pixel_size, height_pixel_size)).convert_alpha()
