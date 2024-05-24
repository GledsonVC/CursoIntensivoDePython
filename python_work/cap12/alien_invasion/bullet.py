import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe para gerenciar os projéteis disparados da espaçonave"""

    def __init__(self, ai_game):
        """Cria um objeto bullet na posição atual da espaçonave"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria um bullet rect em (0, 0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Armazena a posição do projétil com um float
        self.y = float(self.rect.y)
        
        
