import pygame

class Player(pygame.sprite.Sprite):
    # Contains configuration for player
    def __init__(self, pos, max_screen, speed):
        # Call the initializer of the parent class
        super().__init__()

        # Load the player image from path and convert it with alpha transparency
        self.image = pygame.image.load('png/space_ship_image/space_ship.png').convert_alpha()

        # Define the desired size for the space ship
        new_width = 60
        new_height = 40

        # Scale the image to the new dimensions
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

        # Get rectangle object that represents the image and set its midbottom to the given position
        self.rect = self.image.get_rect(midbottom = pos)

        self.speed = speed
        self.limit_screen = max_screen #add limit screen size

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

    def update(self):
        self.move()
