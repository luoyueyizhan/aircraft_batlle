import pygame.font
from pygame.sprite import Group
from plane import Plane

class Scoreboard:
    """

    Display score information

    Args:
        screen(Any):the basic values of screen.
        screen_rect:the size of the screen and some function.
        setting(Settings):the basic values of the game.
        stats(GameStats):data of the game
        text_color(tuple):color of the text
        font(Any):Font size and type
      
    """
    def __init__(self, setting, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting=setting
        self.stats = stats
        self.text_color = (20, 20, 20)
        self.font = pygame.font.SysFont(None, 40)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_planes()

    def prep_planes(self):
        """

        Display the number of remaining ships
        
        """
        self.planes=Group()
        for plane_number in range(self.stats.planes_left):
            plane=Plane(self.screen,self.setting)
            plane.rect.x=10+plane_number*plane.rect.width
            plane.rect.y=10
            self.planes.add(plane)

    def prep_level(self):
        """

        According to grade

        """
        self.level_image=self.font.render(str(self.stats.level),True,self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom+10

    def prep_score(self):
        """

        Prepare the initial score image

        """
        rounded_score=int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """

        Prepare an image containing the highest score and the current score

        """
        high_score=int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10


    def show_score(self):
        """
        
        Display the score on the screen

        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.planes.draw(self.screen)