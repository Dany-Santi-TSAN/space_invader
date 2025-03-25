import pygame
import sys

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock() #speed in fps

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30,30,30)) # fill with rbg color

    pygame.display.flip()
    clock.tick(60) # speed with 60 fps
