import pygame
from card import Card

class Cell():
    def __init__(self, screen, size, column, row, x, y, card_type = None, type = 'ground', available = False):
        self.screen = screen
        self.size = size
        self.row = row
        self.column = column
        self.x = x
        self.y = y
        self.type = type
        self.card_type = card_type
        self.rect = pygame.rect.Rect(self.x, self.y, self.size, self.size)
        self.hovered = False
        self.available = False
        if self.card_type:
            self.card = Card(self.screen, self.size, self.x, self.y, self.card_type, True)
        else:
            self.card = None

    def draw(self):
        self.check_if_hovered()
        if self.type == 'water':
            if self.hovered:
                pygame.draw.rect(self.screen, (53, 134, 235), (self.x, self.y, self.size, self.size))

            pygame.draw.rect(self.screen, (33, 118, 225), (self.x, self.y, self.size, self.size), 4)

        elif self.type == 'ground':
            if self.card_type:
                self.card.draw()

            if self.hovered:
                pygame.draw.rect(self.screen, '#22C95E', (self.x, self.y, self.size, self.size), 4)

    def check_if_hovered(self):
        if not self.available:
            return
        
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

    def set_available(self, available):
        self.available = available