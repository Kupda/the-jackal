import pygame
from card import Card
from screens.events import CLICK_CELL

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
        self.rect = pygame.rect.Rect(self.x, self.y, self.size, self.size)
        self.pressed = 0
        if self.card_type:
            self.card = Card(self.screen, self.size, self.x, self.y, self.card_type, False)

    def draw(self):
        self.check_if_click()
        if self.type == 'water':
            pygame.draw.rect(self.screen, 'blue', (self.x, self.y, self.size, self.size), 4)
        if self.card_type:
            self.card.draw()

    def check_if_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 0:
                # print("Execunting code for button '" + self.text + "'")
                self.pressed = 1
            if pygame.mouse.get_pressed() == (0, 0, 0) and self.pressed == 1:
                self.on_click()
                self.pressed = 0

    def on_click(self):
        cell_click_event = pygame.event.Event(CLICK_CELL, column=self.column, row=self.row)
        pygame.event.post(cell_click_event)
