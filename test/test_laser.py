import unittest
import pygame
from game.laser import Laser

'''''
Explanations:

Importation: Import the Laser class from the laser.py file located in the game folder.

Unit Tests:

test_laser_initialization: Checks that the laser is correctly initialized with the expected values.
test_laser_movement: Checks that the laser moves upwards correctly.
test_laser_removal: Checks that the laser is removed when it goes out of the screen bounds.

Behavior Simulation:
In test_laser_removal, we simulate the laser going out of bounds to check that self.kill() is called.
We may need to adjust the Laser class to track if kill has been called, as unittest cannot directly verify this.
'''''

class TestLaser(unittest.TestCase):

    def setUp(self):
        #Set up the test environment before each test.
        pygame.init()

    def tearDown(self):
        #Clean up the test environment after each test.
        pygame.quit()

    def test_laser_initialization(self):
        pos = (100, 200)
        speed = 5
        screen_height = 600
        laser = Laser(pos, speed, screen_height)

        self.assertEqual(laser.rect.center, pos)
        self.assertEqual(laser.speed, speed)
        self.assertEqual(laser.screen_y_limit, screen_height)

    def test_laser_movement(self):
        pos = (100, 200)
        speed = 5
        screen_height = 600
        laser = Laser(pos, speed, screen_height)
        initial_y = laser.rect.y

        laser.update()
        self.assertEqual(laser.rect.y, initial_y - speed)

    def test_laser_removal(self):
        pos = (100, 200)
        speed = 5
        screen_height = 600
        laser = Laser(pos, speed, screen_height)

        # Simulate laser moving out of bounds
        laser.rect.y = -100
        laser.update()

        self.assertTrue(laser.kill_called, "Laser should be removed when out of bounds")

if __name__ == '__main__':
    unittest.main()
