import pygame
from laser import Laser

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
        # Implement a shooting cooldown
        self.cooldown = True
        self.shoot_time = 0 # how many time spaceship is shot
        self.shoot_cooldown = 500 # 500 milliseconds cooldown
        self.lasers = pygame.sprite.Group()


    def move(self):
        # Rule : only move left and right
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            print(f"Moving right to position: {self.rect.x}")
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            print(f"Moving left to position: {self.rect.x}")

        if keys[pygame.K_a] and self.cooldown:
            self.shooting()
            self.cooldown = False
            self.shoot_time = pygame.time.get_ticks()
            print(f"Shot fired at time: {self.shoot_time}")

    def update_shoot(self):
        # Check if enough time has passed to allow shooting again
        if not self.cooldown:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.shoot_cooldown:
                self.cooldown = True
                print(f"Ready to shoot again at time: {current_time}")


    def apply_screen_limits(self):
    # Define the frame of max screen on x

    # Check when spaceship hit left screen
        if self.rect.left < 0:
            self.rect.left = 0
            print("Hit left screen boundary")

    # Check when spaceship hit right screen
        elif self.rect.right > self.limit_screen:
             self.rect.right = self.limit_screen
             print("Hit right screen boundary")


    def shooting(self):
    # Logic for shooting
        laser_speed = 10  # Define the speed of the laser
        screen_height = self.limit_screen  # Assuming limit_screen is the screen height
        self.lasers.add(Laser(self.rect.center, laser_speed, screen_height))
        print('You shot me down bang bang')

    def update(self):
        self.move()
        self.apply_screen_limits() # Apply screen limits after moving
        self.update_shoot()
        self.lasers.update()
