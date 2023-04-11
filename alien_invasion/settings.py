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

        # bullet settings
        self.bullets_allowed = 3
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 14
        self.bullet_color = (60, 60, 60)
