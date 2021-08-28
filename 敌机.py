import pygame
from pygame.sprite import Sprite

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
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.rect.w=self.rect.width
        self.rect.h=int(self.rect.height/2)
        self.x=float(self.rect.x)
    
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
        self.x+=(self.setting.eplane_speed*self.setting.fleet_direction)
        self.rect.x=self.x

