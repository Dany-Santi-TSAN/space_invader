import pygame
import sys
from alien import Alien

class Game:
    # Contains all variables and functions necessary for the smooth gameplay
    def __init__(self):
        #Player setup



        #Alien setup
        self.alien = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)

    def alien_setup(self, rows, cols):
        for row_index, row in enumerate(rows):
            for col_index, col in enumerate(cols) :
                x = col_inedx
                y = row_index
                alien_sprite = Alien('red',x,y)
                self.aliens.add(alien_sprite)

    def run(self):
        # update and draw all sprite groups
        pass
    

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space Invader') # title
    clock = pygame.time.Clock() #speed in fps
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30)) # fill with rbg color
        game.run() # our game logic setup into the loop

        pygame.display.flip()
        clock.tick(60) # speed with 60 fps
