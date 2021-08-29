from setting import Settings
import pygame
import sys
from bullet import Bullet
from 敌机 import Eplane
from time import sleep
import random

pygame.mixer.init()
bullet_sound = pygame.mixer.Sound('resources/sound/bullet.wav')
enemy1_down_sound = pygame.mixer.Sound('resources/sound/enemy1_down.wav')
game_over_sound = pygame.mixer.Sound('resources/sound/game_over.wav')
bullet_sound.set_volume(0.3)
enemy1_down_sound.set_volume(0.3)
game_over_sound.set_volume(0.3)

def check_keydown_events(event,plane,setting,screen,bullets):
    """

    control the plane through checking down Keyboard.

    Args:
        event(Any):What keyboard do.
        plane(Plane):the values and function of plane.
        setting(Settings):the basic value of the game.
        screen(Any):values of the screen.
        bullets(Any):the gruop of bullet.
    """
    if event.key == pygame.K_RIGHT:
        plane.mv_right=True
    elif event.key==pygame.K_LEFT:
        plane.mv_left=True
    elif event.key==pygame.K_SPACE:
        if len(bullets)<setting.bullet_allowed:
            new_bullet=Bullet(setting,screen,plane)
            bullets.add(new_bullet)

def check_keyup_events(event,plane):
    """

    control the plane through checking up keyboard.

    Args:
        event(Any):what keyboard do.
        plane(Plane):the values and function of plane.
    """
    if event.key==pygame.K_RIGHT:
        plane.mv_right=False
    elif event.key==pygame.K_LEFT:
        plane.mv_left=False


def check_events(plane, setting, screen, bullets, stats, play_button, eplanes,score_board):
    """

    control the plane through checking the keyboard

    Args:
        plane(Plane):the values and function of plane.
        setting(Settings):the basic value of the game.
        screen(Any):values of the screen.
        bullets(Any):the gruop of bullet.
        stats(GameStats):data of the game
        play_button(Button):Start button
        eplanes(Group):A group of enemy planes
        score_board(Scoreboard):The scoring

    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            bullet_sound.play()
            check_keydown_events(event,plane,setting,screen,bullets)       
        elif event.type ==pygame.KEYUP:
            check_keyup_events(event,plane)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(plane, setting, screen, bullets, stats, play_button, mouse_x, mouse_y,eplanes,score_board)

def check_play_button(plane, setting, screen, bullets, stats, play_button, mouse_x, mouse_y,eplanes,score_board):
    """

    check the play button

    Args:
        plane(Plane):the values and function of plane.
        setting(Settings):the basic value of the game.
        screen(Any):values of the screen.
        bullets(Any):the gruop of bullet.
        stats(GameStats):data of the game
        play_button(Button):Start button
        mouse_x(int):The cursor position
        mouse_y(int):The cursor position
        eplanes(Group):A group of enemy planes
        score_board(Scoreboard):The scoring

    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        bullet_sound.play()
        setting.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.game_active = True
        stats.reset_stats()
        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_level()
        score_board.prep_planes()
        eplanes.empty()
        bullets.empty()
        plane.center_plane()


def update_screen(screen,bg_color,plane,bullets,eplanes,stats,play_button,score_board):
    """

    update the screen

    Args:
        screen(Any):values of the screen. 
        bg_color(Any):the color of screen.
        plane(Plane):the values and function of plane.
        bullets(Any):the gruop of bullet.
        eplanes(Group):A group of enemy planes
        stats(GameStats):data of the game
        play_button(Button):Start button
        score_board(Scoreboard):The scoring
    """
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    plane.blitme()
    eplanes.draw(screen)
    score_board.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(bullets,eplanes,setting, screen, plane, stats,score_board):
    """

    update bullets

    Args:
        bullets(Any):the gruop of bullet.
        eplanes(Group):A group of enemy planes
        setting(Settings):the basic value of the game.
        screen(Any):values of the screen. 
        plane(Plane):the values and function of plane.
        stats(GameStats):data of the game
        score_board(Scoreboard):The scoring
      
    """
    bullets.update()
    for bullet in bullets.copy():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)
    collisions=pygame.sprite.groupcollide(bullets,eplanes,True,True)
    if collisions:
        enemy1_down_sound.play()
        for eplane in collisions.values():
            stats.score += setting.eplane_points * len(eplane)
            score_board.prep_score()
        check_high_score(stats, score_board)
        if stats.score%1000==0:
            bullets.empty()
            setting.increase_speed()
            stats.level+=1
            score_board.prep_level()
            creat_eplane(setting,screen, eplanes)

def check_high_score(stats, score_board):
    """

    check the highest score

    Args:
        stats(GameStats):data of the game
        score_board(Scoreboard):The scoring
    """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()

def creat_eplane(setting,screen,eplanes):
    """

    creat eplane

    Args:        
        setting(Settings):the basic value of the game.
        screen(Any):values of the screen. 
        eplanes(Group):A group of enemy planes
        eplane_number(int):The number of enemy planes that can be accommodated in a row
        number_rows(int):The number of rows that can be accommodated in a screen
      
    """
    eplane =Eplane(setting,screen)   
    eplanes.add(eplane)
    
def update_eplanes(setting,eplanes,plane, stats, screen, bullets,scord_board):
    """

    update eplanes

    Args:        
        setting(Settings):the basic value of the game.       
        eplanes(Group):A group of enemy planes   
        plane(Plane):the values and function of plane.
        stats(GameStats):data of the game
        screen(Any):values of the screen. 
        bullets(Any):the gruop of bullet.    
        score_board(Scoreboard):The scoring
      
    """
    eplanes.update()
    game_over = pygame.sprite.spritecollideany(plane, eplanes)
    if game_over:
        plane_hit(setting,stats,screen,plane,eplanes,bullets,scord_board)
    check_eplanes_bottom(setting, eplanes, plane, stats, screen, bullets,scord_board)
    
def plane_hit(setting,stats,screen,plane,eplanes,bullets,scord_board):
    """

    check if plane hit

    Args:        
        setting(Settings):the basic value of the game.       
        stats(GameStats):data of the game
        screen(Any):values of the screen.
        plane(Plane):the values and function of plane.
        eplanes(Group):A group of enemy planes            
        bullets(Any):the gruop of bullet.    
        score_board(Scoreboard):The scoring
      
    """
    if stats.planes_left >0:
        stats.planes_left-=1
        scord_board.prep_planes()
        eplanes.empty()
        bullets.empty()
        plane.center_plane()
        creat_eplane(setting,screen,eplanes)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_eplanes_bottom(setting, eplanes, plane, stats, screen, bullets,scord_board):
    """

    check if eplanes touch the bottom of the screen

    Args:        
        setting(Settings):the basic value of the game.       
        eplanes(Group):A group of enemy planes   
        plane(Plane):the values and function of plane.
        stats(GameStats):data of the game
        screen(Any):values of the screen. 
        bullets(Any):the gruop of bullet.    
        score_board(Scoreboard):The scoring
      
    """
    screen_rect = screen.get_rect()
    for eplane in eplanes.sprites():
        if eplane.rect.bottom >= screen_rect.bottom:
            eplanes.remove(eplane)
            break


