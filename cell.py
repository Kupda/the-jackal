import pygame
from card import Card

class Cell():
    def __init__(self, screen, size, column, row, x, y, card_type=None, type="ground"):
        self.screen = screen
        self.size = size
        self.row = row
        self.column = column
        self.x = x
        self.y = y
        self.type = type
        self.card_type = card_type
        if self.card_type:
            self.card = Card(self.screen, self.size, self.x, self.y, self.card_type, False)

    def draw(self):
        if self.type == 'water':
            pygame.draw.rect(self.screen, 'blue', (self.x, self.y, self.size, self.size), 4)
        if self.card_type:
            self.card.draw()




