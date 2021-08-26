# %%
import sys
import pygame
from setting import Settings
from plane import Plane

def run_game():
    pygame.init()
    air_settings=Settings()
    screen=pygame.display.set_mode((air_settings.screen_width,air_settings.screen_height))
    pygame.display.set_caption("Aircraft Battle")
    planet=Plane(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        planet.blitme()
        screen.fill(air_settings.bg_color)
        pygame.display.flip()

run_game()
# %%
