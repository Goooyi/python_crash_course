class Settings:
    """store all settings for alien invasion"""

    def __init__(self):
        """initialize the game's settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # ship settings
        self.ship_speed = 1.5
        self.bg_color = (246, 240, 234)
        self.ship_limit = 3

        # bullet settings
        self.bullets_allowed = 5
        self.bullet_speed = 3.0
        self.bullet_width = 300
        self.bullet_height = 14
        self.bullet_color = (60, 60, 60)

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # speed scale
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # score
        self.alien_points = 50

        # fleet direction, 1 is right
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
