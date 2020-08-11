import pygame


class Background:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting positon."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the background image and get its rect.
        self.image = pygame.image.load('images/desert_background.jpg')
        # self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()

        # Attach the background image at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
