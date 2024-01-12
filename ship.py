import pygame


ship_img = pygame.image.load('images/ship.png')


class Ship():
    def __init__(self, x, y, color, has_pirates=True):
        self.x = x
        self.y = y
        self.color = color
        self.has_pirates = has_pirates
        self.image = pygame.transform.scale(ship_img, (200, 200))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def add_pirates(self):
        self.has_pirates = True

    def remove_pirates(self):
        self.has_pirates = False

