import pygame


pirate_img = pygame.image.load('images/pirate.png')
pirates_img = {
    'black': pygame.image.load('images/pirate_black.png'),
    'white':  pygame.image.load('images/pirate_white.png'),
    'yellow':  pygame.image.load('images/pirate_yellow.png'),
    'red':  pygame.image.load('images/pirate_red.png')
}


class Pirate():
    def __init__(self, screen, x, y, column, row, color, size, alive=True, with_coin=False, can_move=True):
        self.screen = screen
        self.x = x
        self.y = y
        self.column = column
        self.row = row
        self.alive = alive
        self.with_coin = with_coin
        self.can_move = can_move
        self.color = color
        self.size = size
        self.active = False
        self.image = pygame.transform.scale(pirates_img[self.color], (size, size))

    def die(self):
        self.alive = False

    def revive(self):
        self.alive = True

    def drop_coin(self):
        self.with_coin = False

    def bring_coin(self):
        self.with_coin = True

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def set_active(self, active):
        self.active = active
        if active:
            size = self.size*1.2
        else:
            size = self.size
        self.image = pygame.transform.scale(pirates_img[self.color], (size, size))