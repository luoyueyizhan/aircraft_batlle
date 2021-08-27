#%%
class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.plane_speed=2.5
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
        self.plane_speed = 2.5
        self.bullet_speed = 3
        self.eplane_speed = 2
        self.fleet_direction = 1
        self.eplane_points = 10
        
    def increase_speed(self):
        self.plane_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.eplane_speed *= self.speedup_scale
        self.eplane_points = int(self.eplane_points * self.score_scale)
        print(self.eplane_points)

# %%
