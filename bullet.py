from sys import path
import pygame
from pygame import rect
from pygame.sprite import Sprite

class Bullet(Sprite):
    """

    The definition of bullets of the game.

    Args:
        setting(Settings):the basic values of the game.
        screen(Any):the values and function of the game screen.
        plane(Plane):values and fuctions of Plane.
    
    """
    def __init__(self, setting,screen,plane):
        super().__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
        self.rect.centerx=plane.rect.centerx
        self.rect.top=plane.rect.top
        self.y=float(self.rect.y)
        self.color=setting.bullet_color
        self.speed=setting.bullet_speed
    def update(self) :
        """

        update values of the position of the bullet

        Args:
            y(Bullet):value of the next vertical direction of the bullet.
            rect(Rect|None):value of the vertical direction of the bullet.

        """
        self.y-=self.speed
        self.rect.y=self.y
    def draw_bullet(self):
        """

        draw bullet on the screen.
        
        """
        pygame.draw.rect(self.screen,self.color,self.rect)