import pygame

class Player(pygame.sprite.Sprite):
    # Contains configuration for player
    def __init__(self, pos):
        # Call the initializer of the parent class
        super().__init__()

        # Load the player image from path and convert it with alpha transparency
        self.image = pygame.image.load('png').convert_alpha()
        # Get rectangle object that represents the image and set its midbottom to the given position
        self.rect = self.image.get_rect(midbottom = pos)
