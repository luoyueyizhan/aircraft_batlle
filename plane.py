# %%
import pygame
from pygame.sprite import Sprite

class Plane(Sprite):
    """

    the basic value and fuction of the plane.
    
    Args:
        screen(Any):the basic values of screen.
        setting(Settings):the basic values of the game.
        image(Any):the image of the plane.
        rect(Any):the size and position of the image and some funtion
        screen_rect:the size of the screen and some function.
        center(float):the position of the plane
        mv_right(bool):hint the plane need to move right.
        mv_left(bool):hint the plane need to move left.

    """
    
    def __init__(self,screen,setting):
        super(Plane,self).__init__()
        self.screen=screen
        self.setting=setting

        self.image=pygame.image.load("./images/aircraft1.png")
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.center=float(self.rect.centerx)

        self.mv_right=False
        self.mv_left=False

    def update(self):
        """

        update the position of the plane.
        
        """
        if self.mv_right and self.rect.right<self.screen_rect.right:
            self.center+=self.setting.plane_speed
        
        if self.mv_left and self.rect.left>0:
            self.center-=self.setting.plane_speed
        
        self.rect.centerx=self.center
        
    def center_plane(self):
        """

        put the plane into the center of screen.

        """
        self.center = self.screen_rect.centerx


    def blitme(self):
        """

        draw the plane.

        """
        self.screen.blit(self.image,self.rect)


# %%
