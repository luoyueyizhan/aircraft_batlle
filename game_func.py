from setting import Settings
import pygame
import sys
from bullet import Bullet
def check_keydown_events(event,plane,setting,screen,bullets):
    if event.key == pygame.K_RIGHT:
        plane.mv_right=True
    elif event.key==pygame.K_LEFT:
        plane.mv_left=True
    elif event.key==pygame.K_SPACE:
        if len(bullets)<setting.bullet_allowed:
            new_bullet=Bullet(setting,screen,plane)
            bullets.add(new_bullet)

def check_keyup_events(event,plane):
    if event.key==pygame.K_RIGHT:
        plane.mv_right=False
    elif event.key==pygame.K_LEFT:
        plane.mv_left=False


def check_events(plane,setting,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,plane,setting,screen,bullets)
        
        elif event.type ==pygame.KEYUP:
            check_keyup_events(event,plane)

def update_screen(screen,bg_color,plane,bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    plane.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)