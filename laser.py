import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height):
        super().__init__()
        # Create a surface for the laser with the desired dimensions
        self.image = pygame.Surface((4,20))
        print(f"Laser created at position: {pos}")  # Debug print for position

        # Fill the surface with neon green color
        self.image.fill('#00ff1a')
        print("Laser color set to neon green")  # Debug print for color

        self.rect = self.image.get_rect(center = pos)
        print(f"Laser rectangle: {self.rect}")  # Debug print for rectangle

        self.speed = speed
        print(f"Laser speed set to: {speed}")  # Debug print for speed

        self.height_y_limit = screen_height
        print(f"Screen height constraint set to: {screen_height}")  # Debug print for screen height

    def remove_laser(self):
        # Check if the laser is out of screen bounds
        if not (-50 <= self.rect.y < self.height_y_limit +50):
            print("Laser out of bounds, removing laser")
            self.kill()

    def update(self):
        # Create a function for spaceship to shoot the lasers up
        self.rect.y -= self.speed
        print('shooting the laser up')
        self.remove_laser()
