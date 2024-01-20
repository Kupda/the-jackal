import pygame


ship_img = pygame.image.load('images/ship.png')


class Ship():
    def __init__(self, screen, x, y, color, size, has_pirates=True):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.has_pirates = has_pirates
        self.size = size
        self.image = pygame.transform.scale(ship_img, (self.size, self.size))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def add_pirates(self):
        self.has_pirates = True

    def remove_pirates(self):
        self.has_pirates = False

