import sys

import pygame

class AlienInvasion:
    """manage game resources and behavior"""

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """main game loop"""
        while True:
            # monitor keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make recently drawn graphics visible
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()