import pygame.font

class Button():
    """

    button

    Args:        
        screen(Any):values of the screen. 
        screen_rect(Any):the size of the screen and some function.
        width(int):the width of button
        height(int):the height of button
        button_color(tuple):the color of the button
        text_color(tuple):the color of the text
        font(Any):Font size and type
        rect(Any):the size and position of the image and some funtion
      
    """
    def __init__(self, setting, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = 200
        self.height = 20
        self.button_color = (0, 255, 0)
        self.text_color = (200, 200, 200) 
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        """
        
        Create button label

        Args:
            msg(Any):Text to render as an image

        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """
        
        draw the button
        
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)  
        
