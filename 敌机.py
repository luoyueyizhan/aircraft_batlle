import pygame
from pygame.sprite import Sprite
import random

class Eplane(Sprite):
    """

    The definition of eplane of the game.

    Args:
        screen(Any):the values and function of the game screen.
        setting(Settings):the basic values of the game.
        image(Any):the image of the eplane.
        rect(Any):the size and position of the image and some funtion
        x(float):value of the next vertical direction of the eplane.

    """
    def __init__(self,setting,screen):
        super(Eplane,self).__init__()
        self.screen=screen
        self.setting=setting
        self.image=pygame.image.load('images\敌机一1.png')
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0, setting.screen_width- self.rect.w)
        self.rect.y=self.rect.height
        self.rect.w=self.rect.width
        self.rect.h=int(self.rect.height/2)
        self.y=float(self.rect.y)
    
    def blitme(self):
        """

        draw the eplane.

        """
        self.screen.blit(self.image,self.rect)
    
    def check_edges(self):
        """

        check if the eplane touch the edge of the screen

        """
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
    
    def update(self):
        """

        update the position of the eplane.
        
        """
        self.y+=self.setting.eplane_speed
        self.rect.y=self.y

