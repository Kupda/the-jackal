import pygame
from board import Board
from pirate import Pirate
from ship import Ship


class GameScreen():
    def __init__(self, screen):
        self.x, self.y = screen.get_size()
        self.screen = screen
        self.board = Board(screen, self.x, self.y)
        self.pirate = Pirate(425, 325, 1, 1)
        self.ship = Ship(400, 300, 1, True)

    def draw(self):
        self.board.draw_background()
        self.ship.draw(self.screen)
        self.pirate.draw(self.screen)