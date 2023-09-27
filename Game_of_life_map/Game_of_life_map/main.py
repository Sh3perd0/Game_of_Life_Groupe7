
import pygame 
import sys

from Object.game import Game


def main():

    running = True
    playing = True

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((0, 0))
    clock = pygame.time.Clock()

    # implement menus

    # implement game
    game = Game(screen, clock)

    while running:

        # start menu goes here

        while playing:
            # game loop here
            game.run()

if __name__ == "__main__":
    main()

