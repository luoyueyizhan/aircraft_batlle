# %%
import pygame


class Plane:
    def __init__(self,screen,setting):
        self.screen=screen
        self.setting=setting

        self.image=pygame.image.load("./images/aircraft.png")
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.center=float(self.rect.centerx)

        self.mv_right=False
        self.mv_left=False

    def update(self):
        if self.mv_right and self.rect.right<self.screen_rect.right:
            self.center+=self.setting.plane_speed
        
        if self.mv_left and self.rect.left>0:
            self.center-=self.setting.plane_speed
        
        self.rect.centerx=self.center
        


    def blitme(self):
        self.screen.blit(self.image,self.rect)


# %%
