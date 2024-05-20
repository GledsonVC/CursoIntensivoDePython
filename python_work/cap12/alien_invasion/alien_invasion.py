import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        

        #self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Define a cor do background.
        #self.bg_color = (230, 230, 230)


    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            # Observa eventos de teclado e mouse
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            self._check_events()
            self.ship.update()
            
            # # Redesenha a tela durante cada passagem pelo loop
            # #self.screen.fill(self.bg_color)
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()

            # # Deixa a tela desenhada mais recente visível
            # pygame.display.flip()
            self._update_screen()
            self.clock.tick(60)
    
    
    def _check_events(self):
        """Responde as teclas pressionadas e a eventos de mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_RIGHT:
                    # # Move a espaçonave para a direita
                    # self.ship.rect.x += 1
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

                
    

    def _update_screen(self):
        """Atualiza as imagens na tela e mude para a nova tela"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    ai = AlienInvasion()
    ai.run_game()
