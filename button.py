import pygame
from audio import audio


#button class
class Button():
	def __init__(self, x, y, image, scale, on_click=lambda: print('click')):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.pressed = 0
		self.on_click = on_click
		self.rect.topleft = (x, y)

	def render(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))

	def check_if_click(self):
		''' checks if you click on the button and makes the call to the action just one time'''
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0] and self.pressed == 0:
				# print("Execunting code for button '" + self.text + "'")
				self.pressed = 1
			if pygame.mouse.get_pressed() == (0, 0, 0) and self.pressed == 1:
				self.on_click()
				audio.click_sound.play()
				self.pressed = 0

	def draw(self, surface):
		self.check_if_click()
		self.render(surface)



"""
import pygame
from .audio import audio

class Button():

    def __init__(
            self,
            screen,
            pos = (0, 0), 
            size = (200, 100),
            text = 'Button',
            bg_color = (255, 255, 255),
            hover_bg_color = (200, 200, 200),
            font_color = (0, 0, 0),
            hover_font_color = (0, 0, 0),
            on_click = lambda:print('click')
            ) -> None:
        self.screen = screen
        self.pos = pos
        self.size = size
        self.text = text
        self.font = pygame.font.SysFont("Arial", 16)
        self.bg_color = bg_color
        self.hover_bg_color = hover_bg_color
        self.font_color = font_color
        self.hover_font_color = hover_font_color
        self.pressed = 0
        self.on_click = on_click
        self.rect = pygame.Rect(self.pos, self.size)

    def render(self):
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        surface = pygame.Surface(self.size)

        text = self.font.render(self.text, True, self.hover_font_color if hovered else self.font_color)
        text_rect = text.get_rect(center=(self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2))    

        if hovered:
            surface.fill(self.hover_bg_color)
        else:
            surface.fill(self.bg_color)

        self.screen.blit(surface, self.pos)
        self.screen.blit(text, text_rect)

    def draw(self):
        self.check_if_click()
        self.render()

    def check_if_click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 0:
                # print("Execunting code for button '" + self.text + "'")
                self.pressed = 1
            if pygame.mouse.get_pressed() == (0,0,0) and self.pressed == 1:
                self.on_click()
                audio.click_sound.play()
                self.pressed = 0
"""