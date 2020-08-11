from time import sleep

import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, point_of_explosion=(600, 400)):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.active_count = 0
        self.image_scale = 50
        self.transparent_color = pygame.Color(246, 246, 246)  # RGB white => 255, 255, 255

        # Create an explosion image
        self.image = pygame.image.load('images/dust-explosion.png').convert(24)
        self.image = pygame.transform.scale(self.image, (self.image_scale, self.image_scale))
        self.image.set_colorkey(self.transparent_color)
        self.explosion_rect = self.image.get_rect()
        self.explosion_rect.center = point_of_explosion

    def update(self):
        """explosion lifetime count."""
        self.active_count += 1
        # self.image_scale += 2
        # self.image = pygame.transform.scale(self.image, (self.image_scale, self.image_scale))

    def show_explosion(self):
        """Draw the explosion to the screen."""
        self.screen.blit(self.image, self.explosion_rect)
        invader_killed_sound = pygame.mixer.Sound('sounds/invaderkilled.wav')
        invader_killed_sound.play()
        # sleep(0.5)
