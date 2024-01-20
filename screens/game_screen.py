import pygame
from board import Board
from pirate import Pirate
from ship import Ship
from player import Player

player_colors = ['black', 'white', 'yellow', 'red']


class GameScreen():
    def __init__(self, screen):
        self.x, self.y = screen.get_size()
        self.screen = screen
        self.board = Board(screen, self.x, self.y)
        self.players = []
        #self.pirate = Pirate(425, 325, 1, 1)
        #self.ship = Ship(400, 300, 1, True)

    def draw(self):
        self.board.draw()
        self.draw_players()
        #self.ship.draw(self.screen)
        #self.pirate.draw(self.screen)

    def set_players(self, count):
        for i in range(count):
            self.players.append(Player(self.screen, self.board.field, player_colors[i]))

    def draw_players(self):
        for player in self.players:
            player.draw()
