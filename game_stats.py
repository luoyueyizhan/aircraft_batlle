class GameStats():
    def __init__(self,setting):
        self.setting=setting
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
    
    def reset_stats(self):
        self.planes_left=self.setting.plane_limit
        self.score = 0
        self.level=0