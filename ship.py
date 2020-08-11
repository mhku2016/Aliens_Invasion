import math
import pygame
# from openpyxl.styles.colors import BLACK
from pygame.sprite import Sprite

# from pygame import math
vec = pygame.math.Vector2


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.transparent_color = pygame.Color(0, 0, 0)

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket-black-background.jpg').convert(24)
        # self.image = pygame.image.load('images/space_rocket.png')
        # self.image.set_alpha(156)  # Set transparent level -- transparent decrease as value increase.
        self.image.set_colorkey(self.transparent_color)
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.ship_orientation_angle = 0
        self.image_rotated = pygame.transform.rotate(self.image, self.ship_orientation_angle)  # image rotation
        self.rect = self.image_rotated.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.ship_pos_vec = vec(self.x, self.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.moving_vec = vec(0, 0)

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x and y value, not the rect.
        if self.moving_right and self.ship_orientation_angle >= -90:  # self.rect.right < self.screen_rect.right:
            # self.x += self.settings.ship_speed
            # self.moving_vec = vec(self.settings.ship_speed, 0)
            self.moving_right = False
            self.ship_orientation_angle -= 5
            self.image_rotated = pygame.transform.rotate(self.image, self.ship_orientation_angle)  # image rotation
            self.rect = self.image_rotated.get_rect()

        if self.moving_left and self.ship_orientation_angle <= 90:  # self.rect.left > 0:
            # self.x -= self.settings.ship_speed
            # self.moving_vec = vec(-self.settings.ship_speed, 0)
            self.moving_left = False
            self.ship_orientation_angle += 5
            self.image_rotated = pygame.transform.rotate(self.image, self.ship_orientation_angle)  # image rotation
            self.rect = self.image_rotated.get_rect()

        if self.moving_up and self.rect.top > 0:
            # self.y -= self.settings.ship_speed
            # self.ship_angle_rad = 2*math.pi*self.ship_orientation_angle/360
            # self.moving_vec = vec(self.settings.ship_speed * math.sin(self.ship_angle_rad), -self.settings.ship_speed * math.cos(
            #     self.ship_angle_rad))
            self.moving_vec = vec(0, -self.settings.ship_speed)

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # self.y += self.settings.ship_speed
            # ship_angle_rad = math.radians(self.ship_orientation_angle)
            # self.ship_angle_rad = 2 * math.pi * self.ship_orientation_angle / 360
            # self.moving_vec = vec(self.settings.ship_speed * math.sin(self.ship_angle_rad), self.settings.ship_speed * math.cos(
            #     self.ship_angle_rad))
            self.moving_vec = vec(0, self.settings.ship_speed)

        self.ship_pos_vec += self.moving_vec
        self.moving_vec = vec(0, 0)

        # Update rect object from self.x and self.y.
        # self.rect.x = self.x
        # self.rect.y = self.y
        self.rect.x = self.ship_pos_vec.x
        self.rect.y = self.ship_pos_vec.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image_rotated, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
