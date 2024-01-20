import pygame
import card_types


class Card():
    def __init__(self, screen, size, x, y, type="EMPTY", opened=False):
        self.type = type
        self.screen = screen
        self.size = size
        self.x = x
        self.y = y
        self.opened = opened
        self.default_image = pygame.transform.scale(card_types.default_image_file, (self.size, self.size))
        self.image = pygame.transform.scale(card_types.card_types[type]['image'], (self.size, self.size))

    def draw(self):
        card_image = self.image if self.opened else self.default_image
        self.screen.blit(card_image, (self.x, self.y))


