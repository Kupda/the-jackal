import pygame
from cell import Cell
import random
import card_types
from card import Card

empty_cells = [[0, 0], [1, 0], [11, 0], [12, 0], [0, 1], [12, 1], [0, 11], [0, 12], [1, 12], [12, 11], [11, 12], [12, 12]]
card_types_list = []
for key, card_type in card_types.card_types.items():
    for i in range(card_type['quantity']):
        card_types_list.append(key)
random.shuffle(card_types_list)


def check_cell_available(cell, column, row, player=None):
    type = 'water' if player.pirates[player.active_pirate].swimming else 'ground'
    dist = 1
    if not player.get_active_pirate().can_move:
        return False
    return (abs(column - cell.column) <= dist and (abs(row - cell.row) <= dist)
            and not (column == cell.column and row == cell.row) and cell.type == type)


class Field():
    def __init__(self, screen):
        self.screen = screen
        self.w, self.h = screen.get_size()
        self.margin = 50
        self.x = self.margin
        panel_width = 300
        self.size = min(self.w - panel_width, self.h) - self.margin * 2
        self.y = self.h / 2 - self.size / 2
        self.cells = []
        self.size_cell = self.size / 13 - 1
        self.create_cells()

    def draw(self):
        self.draw_cells()

    def draw_cells(self):
        for cell in self.cells:
            cell.draw()

    def create_cells(self):
        for row in range(13):
            for column in range(13):
                if [column, row] not in empty_cells:
                    cell_type = 'ground'
                    card_type = None
                    if (column == 0 or row == 0 or column == 12 or row == 12 or (row == 1 and column == 1)
                            or (column == 11 and row == 1) or
                            (column == 1 and row == 11) or (column == 11 and row == 11)):
                        cell_type = 'water'
                    else:
                        card_type = card_types_list[0]
                        card_types_list.pop(0)
                    x = self.x + 1 + column * (self.size_cell + 1)
                    y = self.y + 1 + row * (self.size_cell + 1)
                    cell = Cell(self.screen, self.size_cell, column, row, x, y, card_type, cell_type)
                    self.cells.append(cell)

    def get_cell_by_pos(self, column, row):
        return next((cell for cell in self.cells if cell.column == column and cell.row == row), None)

    def update_available_cells(self, column, row, player=None, check=check_cell_available):
        for cell in self.cells:
            cell.hovered = False
            available = check(cell, column, row, player)
            cell.set_available(available)

    def get_available_cells(self):
        return [cell for cell in self.cells if cell.available]

