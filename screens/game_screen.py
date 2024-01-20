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
        self.current_player = 0
        self.players = []

    def draw(self):
        self.board.draw()
        self.draw_players()

    def set_players(self, count):
        for i in range(count):
            self.players.append(Player(self.screen, self.board.field, player_colors[i]))

    def draw_players(self):
        for player in self.players:
            player.draw()

    def click_cell(self, column, row):
        self.players[self.current_player].move_pirate(column, row)
        self.change_player()

    def change_player(self):
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0