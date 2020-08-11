import math
from time import sleep

import pygame
from pygame.sprite import Sprite
vec = pygame.math.Vector2


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship_angle = ai_game.ship.ship_orientation_angle
        self.color = self.settings.bullet_color
        self.transparent_color = pygame.Color(255, 255, 255)

        # Create a bullet rect at (0, 0) and then set correct position.
        self.image = pygame.image.load('images/mars.jpg').convert(24)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image.set_colorkey(self.transparent_color)
        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.vec_ship_rotated_midtop = vec(ai_game.ship.rect.center) - vec(ai_game.ship.rect.midtop)
        self.vec_ship_rotated_midtop = vec(self.vec_ship_rotated_midtop).rotate(-self.ship_angle)
        self.vec_ship_rotated_midtop = vec(ai_game.ship.rect.center) - vec(self.vec_ship_rotated_midtop)
        self.rect.midtop = (self.vec_ship_rotated_midtop.x, self.vec_ship_rotated_midtop.y)

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed*math.cos((self.ship_angle*(2*math.pi)/360))
        self.x -= self.settings.bullet_speed*math.sin(((self.ship_angle*(2*math.pi)/360)))

        # Update the bullet rect image position.
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
