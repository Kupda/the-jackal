import pygame
import button
from board import Board
from pirate import Pirate
from ship import Ship
from player import Player
from audio import audio
from .events import CLICK_CELL, CLICK_PIRATE
import card_types

back_img = pygame.image.load('images/quit.png')
pirate_mode_img = pygame.image.load('images/pirate_button.png')
ship_mode_img = pygame.image.load('images/ship_button.png')

player_colors = ['black', 'white', 'yellow', 'red']


class GameScreen():
    def __init__(self, screen):
        self.x, self.y = screen.get_size()
        self.screen = screen
        self.board = Board(screen, self.x, self.y)
        self.field = self.board.field
        self.current_player = 0
        self.players = []

        self.quit_button = button.Button(self.x - 200, 50, back_img, 0.75, self.quit_game)
        self.pirate_mode_button = button.Button(self.x - 400, self.y / 2 - 30, pirate_mode_img, 0.75, self.enter_pirate_mode)
        self.ship_mode_button = button.Button(self.x - 400, self.y / 2 - 30, ship_mode_img, 0.75, self.enter_ship_mode)

    def draw(self):
        self.board.draw()
        self.draw_mode_button()
        self.draw_players()
        self.quit_button.draw(self.screen)

    def set_players(self, count):
        for i in range(count):
            self.players.append(Player(self.screen, self.board.field, player_colors[i]))

        self.update_active_pirate()

    def draw_players(self):
        for player in self.players:
            player.draw()

    def draw_mode_button(self):
        if self.get_current_player().mode == 'pirate':
            self.ship_mode_button.draw(self.screen)
        else:
            self.pirate_mode_button.draw(self.screen)

    def click_cell(self, cell):
        self.check_enemies_in_cell(cell)
        if self.get_current_player().mode == 'pirate':
            self.get_current_player().move_pirate(cell)
            audio.steps_sound.play()
        elif self.get_current_player().mode == 'ship':
            self.get_current_player().move_ship(cell)
        if cell.card_type == 'HORSE':
            self.field.update_available_cells(cell.column, cell.row, 'ground', None, card_types.card_types['HORSE']['available cells'])
        elif cell.card_type == 'BALLOON':
            self.field.update_available_cells(cell.column, cell.row, 'ground', self.get_current_player(), card_types.card_types['BALLOON']['available cells'])
        elif cell.card_type == 'PLANE':
            self.field.update_available_cells(cell.column, cell.row, 'ground', self.get_current_player(), card_types.card_types['PLANE']['available cells'])
        else:
            self.change_player()
            return 1
        available_cells = self.field.get_available_cells()
        if len(available_cells) == 1 and self.get_current_player().mode == 'pirate':
            self.click_cell(available_cells[0])

    def check_enemies_in_cell(self, cell):
        enemy_killed = False
        for i, player in enumerate(self.players):
            if i != self.current_player:
                for pirate in player.pirates:
                    if pirate.column == cell.column and pirate.row == cell.row:
                        player.respawn_pirate(pirate)
                        enemy_killed = True

        if enemy_killed:
            audio.shoot_sound.play()

    def change_player(self):
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0
        self.get_current_player().enter_pirate_mode()
        self.update_active_pirate()

    def update_active_pirate(self):
        for i, player in enumerate(self.players):
            if i == self.current_player:
                player.select_pirate(player.active_pirate)
            else:
                player.deselect_pirates()
                player.ship.set_active(False)

    def quit_game(self):
        quit_event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(quit_event)

    def get_current_player(self):
        return self.players[self.current_player]

    def pass_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            
            for pirate in self.get_current_player().pirates:
                if pirate.rect.collidepoint(mouse_pos) and not(pirate.active):
                    return self.get_current_player().select_pirate(pirate.index)

            for cell in self.field.cells:
                if cell.rect.collidepoint(mouse_pos) and cell.available:
                    return self.click_cell(cell)
           
    def enter_pirate_mode(self):
        self.get_current_player().enter_pirate_mode()
               
    def enter_ship_mode(self):
        self.get_current_player().enter_ship_mode()