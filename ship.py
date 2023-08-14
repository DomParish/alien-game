import pygame

class Ship:
    """Class to handle ship interactions"""
    
    
    def __init__(self, ai_game):
        """Initialize ship to starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # load ship and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #statrs each ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw ship at current position"""
        self.screen.blit(self.image, self.rect)
    