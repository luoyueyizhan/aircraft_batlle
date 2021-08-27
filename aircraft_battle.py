# %%
from bullet import Bullet
import pygame
from setting import Settings
from plane import Plane
import game_func as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    air_settings=Settings()
    screen=pygame.display.set_mode((air_settings.screen_width,air_settings.screen_height))
    pygame.display.set_caption("Aircraft Battle")
    bullets=Group()
    plane=Plane(screen,air_settings)

    while True:
        gf.check_events(plane,air_settings,screen,bullets)
        plane.update()
        gf.update_bullets(bullets)
        gf.update_screen(screen,air_settings.bg_color,plane,bullets)
run_game()
# %%
