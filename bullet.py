from sys import path
import pygame
from pygame import rect
from pygame.sprite import Sprite

class Bullet(Sprite):
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
        self.y-=self.speed
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)