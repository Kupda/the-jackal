import pygame
from audio import audio


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
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0] and self.pressed == 0:
				self.pressed = 1
			if pygame.mouse.get_pressed() == (0, 0, 0) and self.pressed == 1:
				self.on_click()
				audio.click_sound.play()
				self.pressed = 0

	def draw(self, surface):
		self.check_if_click()
		self.render(surface)