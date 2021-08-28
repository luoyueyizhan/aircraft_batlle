class GameStats():
    """

    Track game statistics

    Args:
        setting(Settings):the basic values of the game.
        game_active(bool):The game state
        self.high_score(int):The highest score
    """
    def __init__(self,setting):
        self.setting=setting
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
    
    def reset_stats(self):
        """

        Initialize statistics that may change with the game
        
        """
        self.planes_left=self.setting.plane_limit
        self.score = 0
        self.level=0