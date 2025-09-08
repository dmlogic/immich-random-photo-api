from decimal import *
import pygame
from datetime import datetime

white = (255, 255, 255)
black = (0, 0, 0)

class Display:
    max_width: None
    max_height: None
    canvas: None
    font_path: None
    title_font: None
    date_font: None

    def __init__(self, font_path, max_width, max_height):
        self.max_width = int(max_width)
        self.max_height = int(max_height)
        self.font_path = font_path
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        pygame.mouse.set_visible(0)
        self.canvas = pygame.display.set_mode(
            (self.max_width, self.max_height),
            pygame.FULLSCREEN
        )
        self.title_font = pygame.font.Font(self.font_path+'OpenSans-SemiBold.ttf', 36)
        self.date_font = pygame.font.Font(self.font_path+'OpenSans-SemiBoldItalic.ttf', 24)

    def send_to_hdmi(self, imageData, imageBtyes):
        image = self.load_image(imageBtyes)
        self.render_image(image)
        self.render_title(imageData['album'])
        self.render_date(imageData['date'])

        pygame.mouse.set_visible(0)
        pygame.display.update()

    def load_image(self, image_path):
        try:
            return pygame.image.load(image_path)
        except:
            print("Bad image")
            print(image_path)
            quit()

    def render_image(self, image):
        self.canvas.blit(image, (0, 0))

    def render_title(self, text ):
        shadow = self.title_font.render(text, True, black)
        shadow_rect = shadow.get_rect()
        shadow_rect.left = 50
        shadow_rect.top = self.max_height - 130
        self.canvas.blit(shadow, shadow_rect)

        title = self.title_font.render(text, True, white)
        title_rect = title.get_rect()
        title_rect.left = shadow_rect.left - 2
        title_rect.top = shadow_rect.top - 2
        self.canvas.blit(title, title_rect)

    def render_date(self, rawDate ):
        # created_date = datetime.strptime(rawDate, '%Y-%m-%d %H:%M:%S')
        created_date = datetime.strptime(rawDate, '%Y-%m-%d')
        text = created_date.strftime("%A, %d %B %Y")

        shadow = self.date_font.render(text, True, black)
        shadow_rect = shadow.get_rect()
        shadow_rect.left = 50
        shadow_rect.top = self.max_height - 80
        self.canvas.blit(shadow, shadow_rect)

        date = self.date_font.render(text, True, white)
        date_rect = date.get_rect()
        date_rect.left = shadow_rect.left - 2
        date_rect.top = shadow_rect.top - 2
        self.canvas.blit(date, date_rect)

