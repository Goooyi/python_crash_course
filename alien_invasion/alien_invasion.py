import sys

import pygame

from settings import Settings
from bullet import Bullet

class Ship:
    """initialize rocket ship"""
    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect =ai_game.screen.get_rect()
        self.image = pygame.image.load('images/rocket.png')
        self.image= pygame.transform.scale_by(self.image, (0.03, 0.03))

        self.rect = self.image.get_rect()

        # store float point for ship
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement state settings
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # update rect.x according to self.x
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class AlienInvasion:
    """manage game resources and behavior"""

    def __init__(self) -> None:
        # ship
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')

        # init bullet
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _check_event(self):
        """check for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _fire_bullet(self):
        """fire a bullet"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_bullet(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print((len(self.bullets)))

    def _update_screen(self):
        """update the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # make recently drawn graphics visible
        pygame.display.flip()

    def run_game(self):
        """main game loop"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullet()
            self._update_screen()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
