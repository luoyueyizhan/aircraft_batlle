from setting import Settings
import pygame
import sys
from bullet import Bullet
from 敌机 import Eplane
from time import sleep

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
    control the plane through checking the keyboard, this one is not accomplished.
    Args:
      event(Any):What keyboard do.
      plane(Plane):the values and function of plane.
      setting(Settings):the basic value of the game.
      screen(Any):values of the screen.
      bullets(Any):the gruop of bullet.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,plane,setting,screen,bullets)       
        elif event.type ==pygame.KEYUP:
            check_keyup_events(event,plane)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(plane, setting, screen, bullets, stats, play_button, mouse_x, mouse_y,eplanes,score_board)

def check_play_button(plane, setting, screen, bullets, stats, play_button, mouse_x, mouse_y,eplanes,score_board):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
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
    update the screen,not accomplished.
    Args:
      screen(Any):values of the screen. 
      bg_color(Any):the color of screen.
      plane(Plane):the values and function of plane.
      bullets(Any):the gruop of bullet.
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
    update bullets,not accomplished.
    Args:
      bullets(Any):the gruop of bullet.
      setting(Settings):the basic value of the game.
      screen(Any):values of the screen. 
      plane(Plane):the values and function of plane.
      bullet(Any): one bullet of the group.
      
    """
    bullets.update()
    for bullet in bullets.copy():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)
    collisions=pygame.sprite.groupcollide(bullets,eplanes,True,True)
    if collisions:
        for eplane in collisions.values():
            stats.score += setting.eplane_points * len(eplane)
            score_board.prep_score()
        check_high_score(stats, score_board)

    if len(eplanes)==0:
        bullets.empty()
        setting.increase_speed()
        stats.level+=1
        score_board.prep_level()
        creat_fleet(setting,screen, eplanes, plane)

def check_high_score(stats, score_board):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()

def get_number_eplane_x(setting,eplane_width):
    available_space_x=setting.screen_width-(2*eplane_width)
    number_eplane_x=int(available_space_x/(2*eplane_width))
    return number_eplane_x

def get_number_rows(setting,plane_height,eplane_height):
    available_space_y=setting.screen_height-7*eplane_height-plane_height
    print(available_space_y,eplane_height)
    number_rows=int(available_space_y/eplane_height)
    return number_rows

def creat_eplane(setting,screen,eplanes,eplane_number,number_rows):
    eplane=Eplane(setting,screen)
    eplane_width=eplane.rect.width
    eplane.x=eplane_width+2*eplane_width*eplane_number
    eplane.rect.x=eplane.x
    eplane.rect.y=eplane.rect.height+2*eplane.rect.height*number_rows
    eplanes.add(eplane)

def creat_fleet(setting,screen,eplanes,plane):
    eplane=Eplane(setting,screen)
    number_eplane_x=get_number_eplane_x(setting,eplane.rect.width)
    number_rows=get_number_rows(setting,plane.rect.height,eplane.rect.height)
    for row_number in range(5):#number_rows
        for eplane_number in range(5):#number_eplane_x
            creat_eplane(setting,screen,eplanes,eplane_number,row_number)
        
def change_fleet_direction(setting,eplanes):
    for eplane in eplanes.sprites():
        eplane.rect.y+=setting.fleet_drop_speed
    setting.fleet_direction*=-1

def check_fleet_edges(setting,eplanes):
    for eplane in eplanes.sprites():
        if eplane.check_edges():
            change_fleet_direction(setting,eplanes)
            break

def update_eplanes(setting,eplanes,plane, stats, screen, bullets,scord_board):
    eplanes.update()
    check_fleet_edges(setting,eplanes)
    game_over = pygame.sprite.spritecollideany(plane, eplanes)
    if game_over:
        plane_hit(setting,stats,screen,plane,eplanes,bullets,scord_board)
    check_eplanes_bottom(setting, eplanes, plane, stats, screen, bullets,scord_board)
    
def plane_hit(setting,stats,screen,plane,eplanes,bullets,scord_board):
    if stats.planes_left >0:
        stats.planes_left-=1
        scord_board.prep_planes()
        eplanes.empty()
        bullets.empty()
        creat_fleet(setting,screen,eplanes,plane)
        plane.center_plane()
        sleep(1)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_eplanes_bottom(setting, eplanes, plane, stats, screen, bullets,scord_board):
    screen_rect = screen.get_rect()
    for eplane in eplanes.sprites():
        if eplane.rect.bottom >= screen_rect.bottom:
            plane_hit(setting,stats,screen,plane,eplanes,bullets,scord_board)
            break


