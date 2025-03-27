import pygame
import sys
from alien import Alien
from player import Player
from laser import Laser

class Game:
    # Contains all variables and functions necessary for the smooth gameplay
    def __init__(self):
        space_ship = Player((screen_width / 2,screen_height),screen_width, 5) # start in bottom center of the screen
        self.player = pygame.sprite.GroupSingle(space_ship)

    def run(self):
        # update and draw all sprite groups
        self.player.update()
        self.player.sprite.lasers.draw(screen) # run and draw laser when press shooting
        self.player.draw(screen) # draw player into screen width



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

        screen.fill((30,30,30)) # fill with rbg color, here is black
        game.run() # our game logic setup into the loop

        pygame.display.flip()
        clock.tick(60) # speed with 60 fps
