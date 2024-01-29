import random
import json
# Name_file_image
def load_settings():
    with open('constant/settings.json', 'r') as file:
        settings = json.load(file)
    return settings


settings = load_settings()

BOB_IMAGE = settings['BOB_IMAGE'][random.randint(0,2)]
#BOB_IMAGE = settings['BOB_IMAGE'][2]
FOOD_IMAGE = settings['FOOD_IMAGE']
CELL_IMAGE = settings['CELL_IMAGE']

NUMBER_FOOD = settings['NUMBER_FOOD']
NUMBER_BOB = settings['NUMBER_BOB']
FRAME_RATE = settings['FRAME_RATE']
TICK = settings['TICK']

GRID_SIZE = settings['GRID_SIZE']
CELL_SIZE = settings['CELL_SIZE']

DEFAULT_ENERGY = settings['DEFAULT_ENERGY']
ENERGY_TO_REPRODUCE = settings['ENERGY_TO_REPRODUCE']
LOSE_ENERGY_AFTER_SEX = settings['LOSE_ENERGY_AFTER_SEX']
NEW_ENERGY_SEXUAL_REPRODUCE = settings['NEW_ENERGY_SEXUAL_REPRODUCE']
NEW_ENERGY_PARTH_REPRODUCE = settings['NEW_ENERGY_PARTH_REPRODUCE']
MAX_ENERGY = settings['MAX_ENERGY']

DEFAULT_PERCEPTION = settings['DEFAULT_PERCEPTION']
DEFAULT_SPEED = settings['DEFAULT_SPEED']
DEFAULT_MASS = settings['DEFAULT_MASS']
DEFAULT_MEMORY=settings['DEFAULT_MEMORY']

def reload_settings():
    settings = load_settings()
    global BOB_IMAGE
    global FOOD_IMAGE
    global CELL_IMAGE
    global NUMBER_FOOD 
    global NUMBER_BOB
    global FRAME_RATE
    global TICK
    global GRID_SIZE
    global CELL_SIZE
    global DEFAULT_ENERGY
    global ENERGY_TO_REPRODUCE
    global LOSE_ENERGY_AFTER_SEX
    global NEW_ENERGY_SEXUAL_REPRODUCE
    global NEW_ENERGY_PARTH_REPRODUCE
    global MAX_ENERGY
    global DEFAULT_PERCEPTION
    global DEFAULT_SPEED 
    global DEFAULT_MASS
    global DEFAULT_MEMORY

    BOB_IMAGE = settings['BOB_IMAGE']
    FOOD_IMAGE = settings['FOOD_IMAGE']
    CELL_IMAGE = settings['CELL_IMAGE']

    NUMBER_FOOD = settings['NUMBER_FOOD']
    NUMBER_BOB = settings['NUMBER_BOB']
    FRAME_RATE = settings['FRAME_RATE']
    TICK = settings['TICK']

    GRID_SIZE = settings['GRID_SIZE']
    CELL_SIZE = settings['CELL_SIZE']

    DEFAULT_ENERGY = settings['DEFAULT_ENERGY']
    ENERGY_TO_REPRODUCE = settings['ENERGY_TO_REPRODUCE']
    LOSE_ENERGY_AFTER_SEX = settings['LOSE_ENERGY_AFTER_SEX']
    NEW_ENERGY_SEXUAL_REPRODUCE = settings['NEW_ENERGY_SEXUAL_REPRODUCE']
    NEW_ENERGY_PARTH_REPRODUCE = settings['NEW_ENERGY_PARTH_REPRODUCE']
    MAX_ENERGY = settings['MAX_ENERGY']

    DEFAULT_PERCEPTION = settings['DEFAULT_PERCEPTION']
    DEFAULT_SPEED = settings['DEFAULT_SPEED']
    DEFAULT_MASS = settings['DEFAULT_MASS']
    DEFAULT_MEMORY=settings['DEFAULT_MEMORY']
