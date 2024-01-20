import pygame
from pirate import Pirate
from ship import Ship

start_pos = {
    'black': [6, 0],
    'white': [6, 12],
    'yellow': [12, 6],
    'red': [0, 6]
}


class Player():
    def __init__(self, screen, field, color, coins=0):
        self.screen = screen
        self.field = field
        self.coins = coins
        self.color = color
        self.active_pirate = 0
        self.pirates = []
        self.ship = self.create_ship()
        self.create_pirates()
        self.select_pirate(0)

    def create_pirates(self):
        pirates_size = self.field.size_cell / 3
        column, row = start_pos[self.color]
        cell = self.field.get_cell_by_pos(column, row)
        for i in range(3):
            self.pirates.append(Pirate(self.screen, cell.x+i*pirates_size, cell.y, column, row, self.color, pirates_size))

    def draw_pirates(self):
        for pirate in self.pirates:
            pirate.draw()

    def draw(self):
        self.ship.draw()
        self.draw_pirates()

    def select_pirate(self, num):
        self.active_pirate = num
        for pirate in self.pirates:
            pirate.set_active(self.pirates.index(pirate) == num)

    def create_ship(self):
        ship_size = self.field.size_cell - 2
        column, row = start_pos[self.color]
        cell = self.field.get_cell_by_pos(column, row)
        return Ship(self.screen, cell.x+1, cell.y+1, self.color, ship_size)

    def move_pirate(self, column, row):
        cell = self.field.get_cell_by_pos(column, row)
        self.pirates[self.active_pirate].move(cell)
