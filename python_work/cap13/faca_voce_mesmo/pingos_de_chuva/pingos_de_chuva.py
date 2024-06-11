import sys
import pygame
from settings import Settings

class PingosDeChuva:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicia e cria recursos de pingo de chuva"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_widht, self.settings.screen_height)
        )
        pygame.display.set_caption("Pingo de chuva")

    def run_game(self):
        """Inicia o loop principal de pingo de chuva"""
        while True:
            # Observa eventos de teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event == pygame.K_q:
                    sys.exit()
            # Redesenha cor de fundo de tela durante cadas passagem ao loop
            self.screen.fill(self.settings.bg_color)

            # Deixa a tela desenhada mais recente visível
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # Cria uma instancia de pingo de chuva e executa-o
    pc = PingosDeChuva()
    pc.run_game()

