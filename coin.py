import pygame

coin_img = pygame.image.load('images/coin.png')


class Coin():
    def __init__(self, screen, column, row, x, y, size, quantity = 0):
        self.screen = screen
        self.column = column
        self.row = row
        self.x = x
        self.y = y
        self.size = size
        self.quantity = quantity
        self.image = pygame.transform.scale(coin_img, (self.size, self.size))
        self.font = pygame.font.SysFont("arialblack", round(self.size * 0.35))

    def set_quantity(self, quantity):
        self.quantity = quantity

    def add_coin(self):
        self.quantity += 1

    def remove_coin(self):
        self.quantity -= 1

    def draw_text(self):
        text = self.font.render(f'{self.quantity}', True, '#FFFFFF')
        text_rect = text.get_rect(center=(self.x + self.size * 0.68, self.y - self.size * 0.05))
        pygame.draw.circle(self.screen, '#FFFFFF', (self.x + self.size * 0.7, self.y), round(self.size * 0.35))
        pygame.draw.circle(self.screen, '#000000', (self.x + self.size * 0.7, self.y), round(self.size * 0.3))
        #
        self.screen.blit(text, text_rect)

    def draw(self):
        if self.quantity == 0:
            return
    
        self.screen.blit(self.image, (self.x, self.y))
        self.draw_text()