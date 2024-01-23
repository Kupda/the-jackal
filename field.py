from cell import Cell
import random
from card_types import card_types, coin_disallowed_card_types
from card import Card

empty_cells = [[0, 0], [1, 0], [11, 0], [12, 0], [0, 1], [12, 1], [0, 11], [0, 12], [1, 12], [12, 11], [11, 12], [12, 12]]


def create_random_cards():
    card_types_list = []
    for key, card_type in card_types.items():
        for i in range(card_type['quantity']):
            card_types_list.append(key)
    random.shuffle(card_types_list)
    return card_types_list


def check_can_move_with_coin(cell, player=None):
    active_pirate = player.get_active_pirate()

    return ((active_pirate.with_coin and cell.card_type and cell.card.opened and not(cell.card_type in coin_disallowed_card_types))
            or not active_pirate.with_coin or cell.type == 'water')


def check_cell_available(cell, column, row, player=None):
    active_pirate = player.get_active_pirate()
    type = 'water' if active_pirate.swimming else 'ground'
    dist = 1
    if not active_pirate.can_move:
        return False
    return (abs(column - cell.column) <= dist and (abs(row - cell.row) <= dist)
            and not (column == cell.column and row == cell.row)
            and (cell.type == type or cell.column == player.ship.column and cell.row == player.ship.row)
            and check_can_move_with_coin(cell, player))


def check_fort_available(cell, player):
    return (((cell.card_type == 'FORT' or cell.card_type == 'FORT_LIVE') and
             (cell.fort_color == player.color or cell.fort_color == None))
            or (cell.card_type != 'FORT' and cell.card_type != 'FORT_LIVE'))


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
        card_types_list = create_random_cards()
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
            available = check(cell, column, row, player) and check_fort_available(cell, player)
            cell.set_available(available)

    def get_available_cells(self):
        return [cell for cell in self.cells if cell.available]


