import pygame
from pirate import Pirate
from ship import Ship

start_pos = {
    'black': [6, 0],
    'white': [6, 12],
    'yellow': [12, 6],
    'red': [0, 6]
}


def check_ship_cell_available(cell, column, row, player=None):
    movement_direction = player.ship.movement
    if ((movement_direction == 'horizontal' and (row != cell.row or abs(column - cell.column) != 1))
            or (movement_direction == 'vertical' and (column != cell.column or abs(row - cell.row) != 1))
            or cell.type != 'water') or (not player.ship.has_pirates):
        return False
    else:
        return True


class Player():
    def __init__(self, screen, field, color, coins=0):
        self.screen = screen
        self.field = field
        self.coins = coins
        self.color = color
        self.mode = 'pirate'
        self.active_pirate = 0
        self.pirates = []
        self.ship = self.create_ship()
        self.another_step_mode = False
        self.plane_available = False
        self.auto_steps = 0
        self.create_pirates()
        self.select_pirate(self.active_pirate)

    def create_pirates(self):
        pirates_size = self.field.size_cell / 3
        column, row = start_pos[self.color]
        cell = self.field.get_cell_by_pos(column, row)
        for i in range(3):
            self.pirates.append(Pirate(self.screen, i, cell.x+i*pirates_size, cell.y, column, row, self.color, pirates_size))

    def draw_pirates(self):
        pirates_on_ship = []

        if self.mode == 'ship':
            pirates_on_ship = self.get_pirates_on_ship()

        for pirate in self.pirates:
            if pirate in pirates_on_ship:
                pirate.ship_y = self.ship.swing_y
            else:
                pirate.ship_y = 0
                
            pirate.draw()

    def draw(self):
        self.ship.draw()
        self.draw_pirates()

    def select_pirate(self, num):
        if self.mode == 'ship' or self.another_step_mode:
            return
        
        self.active_pirate = num
        for pirate in self.pirates:
            pirate.set_active(self.pirates.index(pirate) == num)

        self.field.update_available_cells(self.pirates[self.active_pirate].column, self.pirates[self.active_pirate].row, self)

    def select_first_alive_pirate(self):
        for i, pirate in enumerate(self.pirates):
            if pirate.alive:
                self.select_pirate(i)
                break

    def deselect_pirates(self):
        for pirate in self.pirates:
            pirate.set_active(False)

    def create_ship(self):
        ship_size = self.field.size_cell - 2
        column, row = start_pos[self.color]
        cell = self.field.get_cell_by_pos(column, row)
        return Ship(self.screen, column, row, cell.x + 1, cell.y + 1, self.color, ship_size)

    def move_pirate(self, cell, pirate=None):
        if cell.card and not cell.card.opened:
            cell.card.open()
            if cell.card_type == 'PLANE':
                self.plane_available = True

        pirates_near = 0
        for another_pirate in self.pirates:
            if another_pirate.column == cell.column and another_pirate.row == cell.row:
                another_pirate.move(cell, pirates_near)
                pirates_near += 1

        if not pirate:
            pirate = self.pirates[self.active_pirate]

        pirate.move(cell, pirates_near)
        pirates_on_ship = self.get_pirates_on_ship()
        if len(pirates_on_ship) > 0:
            self.ship.add_pirates()
        else:
            self.ship.remove_pirates()

        if cell.type == 'water' and (self.ship.column != pirate.column or self.ship.row != pirate.row):
            pirate.go_to_water()
        else:
            pirate.go_to_sand()

        self.another_step_mode = False

    def move_ship(self, cell):
        pirates_on_ship = self.get_pirates_on_ship()
        for i, pirate in enumerate(pirates_on_ship):
            pirate.move(cell, i)
        self.ship.move(cell)
        self.update_ship_available_cells()

    def update_ship_available_cells(self):
        self.field.update_available_cells(self.ship.column, self.ship.row, self,
                                          check_ship_cell_available)

    def respawn_pirate(self, pirate):
        cell = self.field.get_cell_by_pos(self.ship.column, self.ship.row)
        self.move_pirate(cell, pirate)

    def enter_ship_mode(self):
        self.mode = 'ship'
        self.ship.set_active(True)
        self.deselect_pirates()
        self.update_ship_available_cells()
    
    def enter_pirate_mode(self):
        self.mode = 'pirate'
        self.ship.set_active(False)
        self.select_pirate(0)

    def get_pirates_on_ship(self):
        return [pirate for pirate in self.pirates if (pirate.column == self.ship.column and pirate.row == self.ship.row)]
    
    def get_active_pirate(self):
        return self.pirates[self.active_pirate]
    
    def get_active_pirate_prev_pos(self):
        return [self.get_active_pirate().prev_column, self.get_active_pirate().prev_row]