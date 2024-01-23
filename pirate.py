import pygame
from audio import audio

pirates_img = {
    'black': pygame.image.load('images/pirate_black.png'),
    'white': pygame.image.load('images/pirate_white.png'),
    'yellow': pygame.image.load('images/pirate_yellow.png'),
    'red': pygame.image.load('images/pirate_red.png')
}

coin_img = pygame.image.load('images/coin.png')


class Pirate():
    def __init__(self, screen, index, x, y, column, row, color, size, alive=True, with_coin=False, can_move=True):
        self.screen = screen
        self.index = index
        self.x = x
        self.y = y
        self.jump_y = 0
        self.jump_direction = -0.5
        self.ship_y = 0
        self.column = column
        self.row = row
        self.prev_column = 0
        self.prev_row = 0
        self.alive = alive
        self.with_coin = with_coin
        self.can_move = can_move
        self.color = color
        self.size = size
        self.active = False
        self.swimming = False
        self.image = pygame.transform.scale(pirates_img[self.color], (size, size))
        self.coin_image = pygame.transform.scale(coin_img, (self.size * 0.6, self.size * 0.6))
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def die(self, cell):
        self.alive = False
        self.column = -1
        self.row = -1
        audio.dead_sound.play()

        if self.with_coin:
            self.drop_coin(cell)

    def revive(self):
        self.alive = True

    def drop_coin(self, cell):
        self.with_coin = False
        cell.coin.add_coin()

    def grab_coin(self, cell):
        self.with_coin = True
        cell.coin.remove_coin()

    def draw(self):
        if not self.alive:
            return

        y = self.y + self.ship_y

        if self.active:
            self.jump()
            y += self.jump_y

        self.screen.blit(self.image, (self.x, y))

        if self.with_coin:
            self.screen.blit(self.coin_image, (self.x, y + self.size))

    def set_active(self, active):
        self.active = active

        if active:
            size = self.size * 1.2
            self.start_jumping()
        else:
            size = self.size

        self.image = pygame.transform.scale(pirates_img[self.color], (size, size))

    def move(self, cell, pirates_near=0):
        self.x = cell.x + self.size * pirates_near
        self.y = cell.y
        self.prev_column = self.column
        self.prev_row = self.row
        self.column = cell.column
        self.row = cell.row
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def start_jumping(self):
        self.jump_y = 0
        self.jump_direction = -0.5

    def jump(self):
        if self.jump_y <= -10:
            self.jump_direction = 0.5
        elif self.jump_y >= 0:
            self.jump_direction = -0.5

        self.jump_y += self.jump_direction

    def go_to_water(self):
        self.swimming = True

    def go_to_sand(self):
        self.swimming = False

    def __eq__(self, other):
        return self.index == other.index