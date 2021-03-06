# %%
from time import time
from bullet import Bullet
import pygame
from setting import Settings
from plane import Plane
import game_func as gf
from pygame.sprite import Group
from 敌机 import Eplane
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import time



def run_game():
    """

    Run the game

    Args:
        air_setting(Settings):The basic values of the game.
        screen(Any):The values of screen.
        play_button(Button):the play button
        bullets(Group):the bullets of the plane.
        eplanes(Group):the group of eplane
        plane(Plane):some values and fuctions of plane.
        eplane(Eplane):Enemy plane
        stats=(GameStats):data of the game
        score_board(Scoreboard):The scoring
    """
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('resources/sound/game_music.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)
    air_settings=Settings()
    screen=pygame.display.set_mode((air_settings.screen_width,air_settings.screen_height))
    pygame.display.set_caption("Aircraft Battle")
    play_button = Button(air_settings, screen, "Play")
    bullets=Group()
    eplanes=Group()
    plane=Plane(screen,air_settings)
    eplane=Eplane(air_settings,screen)
    enemy_frequency=0
    stats=GameStats(air_settings)
    score_board = Scoreboard(air_settings, screen, stats)

    while True:
        gf.check_events(plane,air_settings,screen,bullets, stats, play_button,eplanes,score_board)
        if stats.game_active:
            if enemy_frequency % 200 == 0:    
                gf.creat_eplane(air_settings,screen,eplanes)
            enemy_frequency += 1
            if enemy_frequency >= 100:
                enemy_frequency = 0            
            plane.update()
            gf.update_bullets(bullets,eplanes,air_settings, screen, plane, stats, score_board)
            gf.update_eplanes(air_settings,eplanes,plane,stats,screen,bullets, score_board)
        gf.update_screen(screen,air_settings.bg_color,plane,bullets,eplanes, stats, play_button, score_board)
run_game()
