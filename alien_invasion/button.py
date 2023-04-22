import pygame.font

class Button:

    def __init__(self, ai_game, msg) -> None:
        """initialize button feature"""
        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect()
        # TODO