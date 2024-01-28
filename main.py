import pygame
import sys
from constant.settings import *
import analyses.global_var_analyse
from object.game import Game
import analyses.mainAnalyses as analyse
import constant.settings as sett

running = True
playing = True

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((0, 0))
    clock = pygame.time.Clock()

    # implement menus

    # implement game
    game = Game(screen, clock)
    
    while running:
        clock.tick(FRAME_RATE)
        # start menu goes here

        while playing:
            # game loop here
            game.run()
            break
        break

    pygame.display.quit()
    analyse.show_analyses()

def launch():
    #if __name__ == "__main__":
    
    main()
launch()