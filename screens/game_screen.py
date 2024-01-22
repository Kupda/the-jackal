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
        effect_cards = ['HORSE', 'BALLOON', 'PLANE', 'ICE', 'CROCODILE',
                        'GUN_TOP', 'ARROW_1S', 'ARROW_2S', 'ARROW_1D',
                        'ARROW_2D', 'ARROW_3', 'ARROW_4D', 'ARROW_4S', 'GUN_BOTTOM', 'GUN_LEFT', 'GUN_RIGHT']
        current_player = self.get_current_player()
        sound = audio.steps_sound
        enemy_beaten = self.check_enemies_in_cell(cell)
        move_end = False

        if enemy_beaten and current_player.mode == 'pirate':
            sound = audio.shoot_sound
        elif enemy_beaten and current_player.mode == 'ship':
            sound = audio.dead_sound

        if current_player.mode == 'pirate':
            current_player.move_pirate(cell)
        elif current_player.mode == 'ship':
            current_player.move_ship(cell)

        for pirate in current_player.pirates:
            pirate.can_move = True

        if cell.card_type in effect_cards:
            current_player.auto_steps += 1
            if current_player.auto_steps > 20:
                current_player.get_active_pirate().die()
                self.change_player()
                move_end = True
            current_player.another_step_mode = True
            self.field.update_available_cells(cell.column, cell.row, current_player, card_types.card_types[cell.card_type]['available cells'])
            
            if cell.card_type == 'PLANE' and current_player.plane_available:
                current_player.plane_available = False
            elif cell.card_type == 'PLANE':
                move_end = True
                self.change_player()
            if 'sound' in card_types.card_types[cell.card_type]:
                sound = card_types.card_types[cell.card_type]['sound']
        else:
            if cell.card_type == 'KEG':
                current_player.get_active_pirate().can_move = False
            elif cell.card_type == 'CANNIBAL':
                current_player.get_active_pirate().die()
            move_end = True
            self.change_player()
        
        sound.play()

        if move_end:
            return

        available_cells = self.field.get_available_cells()

        if len(available_cells) == 1 and current_player.mode == 'pirate':
            self.click_cell(available_cells[0])

    def check_enemies_in_cell(self, cell):
        enemy_beaten = False

        for i, player in enumerate(self.players):
            if i != self.current_player:
                if player.ship.column == cell.column and player.ship.row == cell.row:
                    self.get_current_player().get_active_pirate().die()
                    enemy_beaten = True
                    break

                for pirate in player.pirates:
                    if pirate.column == cell.column and pirate.row == cell.row:
                        if player.mode == 'pirate':
                            player.respawn_pirate(pirate)
                        else:
                            pirate.die()
                        enemy_beaten = True

        return enemy_beaten

    def change_player(self):
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0
        self.get_current_player().enter_pirate_mode()
        self.update_active_pirate()
        self.get_current_player().auto_steps = 0

    def update_active_pirate(self):
        for i, player in enumerate(self.players):
            if i == self.current_player:
                if not player.get_active_pirate().alive:
                    player.select_first_alive_pirate()
                else:
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
                if pirate.rect.collidepoint(mouse_pos) and not(pirate.active) and pirate.alive:
                    return self.get_current_player().select_pirate(pirate.index)

            for cell in self.field.cells:
                if cell.rect.collidepoint(mouse_pos) and cell.available:
                    return self.click_cell(cell)
           
    def enter_pirate_mode(self):
        if self.get_current_player().another_step_mode == False:
            self.get_current_player().enter_pirate_mode()
               
    def enter_ship_mode(self):
        if self.get_current_player().another_step_mode == False:
            self.get_current_player().enter_ship_mode()