#%%
class Settings:
    """

    some basic value of the game.
    
    Args:
        screen_width(int):the width of the screen.
        screen_height(int):the height of the screen.
        bg_color(tuple):the color of the screen.
        plane_speed(float):the speed of the plane.
        bullet_speed(float):the speed of the bullet.
        bullet_width(int):the width of the bullet.
        bullet_height(int):the height of the bullet.
        bullet_color(tuple): the color of the bullet.
        bullet_allowed(int): the maximum quaitity of the bullets.
        eplane_speed(int):Enemy aircraft speed
        fleet_drop_speed(int):The falling speed of the fleet
        fleet_direction(int):Direction of movement
        plane_limit(int):Life value
        speedup_scale(float):Speed up the pace of the game
        score_scale(float):Increased speed of enemy aircraft scoring

    """
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.plane_speed=5
        self.bullet_speed=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(100,0,50)
        self.bullet_allowed=5
        self.eplane_speed=1
        self.fleet_drop_speed=10
        self.fleet_direction=1
        self.plane_limit=3
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """

        Initialize Settings that change as the game progresses

        """
        self.plane_speed = 2.5
        self.bullet_speed = 3
        self.eplane_speed = 2
        self.fleet_direction = 1
        self.eplane_points = 50
        
    def increase_speed(self):
        """
        
        Increased speed and enemy aircraft scoring
        
        """
        self.plane_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.eplane_speed *= self.speedup_scale
        self.eplane_points = int(self.eplane_points * self.score_scale)

# %%
