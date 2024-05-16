import sys
import pygame

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo"""
        pygame.init()
        #self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
    
    def rum_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            # Observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Deixa a tela desenhada mais recente visível
            pygame.display.flip()


if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    ai = AlienInvasion()
    ai.rum_game()
