import pygame
from card import Card
from coin import Coin


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
        self.coin = None
        self.fort_color = None

        if self.card_type:
            coin_size = round(self.size * 0.4)
            self.card = Card(self.screen, self.size, self.x, self.y, self.card_type, False)
            self.coin = Coin(self.screen, self.column, self.row, self.x + self.size - coin_size * 1.1, self.y + self.size - coin_size * 1.1, coin_size)

            if 'COINS_' in self.card_type:
                coins_quantity = int(self.card_type.replace('COINS_', ''))
                self.coin.set_quantity(coins_quantity)

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



        if not self.available:
            disabled_surface = pygame.Surface((self.size, self.size))
            disabled_surface.set_alpha(100)
            disabled_surface.fill('#333333')
            self.screen.blit(disabled_surface, (self.x, self.y))

        if self.card_type and self.card.opened:
            self.coin.draw()

    def check_if_hovered(self):
        if not self.available:
            return

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

    def set_available(self, available):
        self.available = available