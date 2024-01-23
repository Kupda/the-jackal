import pygame
import button
from board import Board
from pirate import Pirate, pirates_img
from coin import coin_img
from ship import Ship
from player import Player
from audio import audio
from .events import OPEN_MENU_SCREEN, OPEN_FINISH_GAME
import card_types

dead_pirate_img = pygame.image.load('images/dead_pirate.png')
back_img = pygame.image.load('images/button_quit2.png')
pirate_mode_img = pygame.image.load('images/pirate_button.png')
ship_mode_img = pygame.image.load('images/ship_button.png')
grab_coin_img = pygame.image.load('images/grab_coin_button.png')
drop_coin_img = pygame.image.load('images/drop_coin_button.png')
revive_pirate_img = pygame.image.load('images/revive_pirate_button.png')

player_colors = ['black', 'white', 'yellow', 'red']


class GameScreen():
    def __init__(self, screen):
        self.dead_pirate_image = None
        self.dead_pirate_size = None
        self.revive_pirate_button = None
        self.drop_coin_button = None
        self.grab_coin_button = None
        self.ship_mode_button = None
        self.pirate_mode_button = None
        self.quit_button = None
        self.panel_buttons_x = None
        self.buttons_scale = None
        self.dead_pirates = None
        self.players = None
        self.current_player = None
        self.panel_y = None
        self.panel_x = None
        self.panel_height = None
        self.panel_width = None
        self.field = None
        self.board = None
        self.x, self.y = screen.get_size()
        self.screen = screen

    def start_game(self):
        self.board = Board(self.screen, self.x, self.y)
        self.field = self.board.field
        self.panel_width = self.x - self.board.field.size - 250
        self.panel_height = self.y - self.board.field.y * 2
        self.panel_x = self.x - self.panel_width - 50
        self.panel_y = self.board.field.y
        self.current_player = 0
        self.players = []
        self.dead_pirates = []
        self.buttons_scale = self.x / 3500
        self.panel_buttons_x = self.panel_x + self.panel_width / 2 - (840 * self.buttons_scale) / 2

        self.quit_button = button.Button(self.x - 275, 50, back_img, self.buttons_scale, self.back_to_menu)

        self.pirate_mode_button = button.Button(self.panel_buttons_x, self.y / 2 - 50, pirate_mode_img,
                                                self.buttons_scale, self.enter_pirate_mode)
        self.ship_mode_button = button.Button(self.panel_buttons_x, self.y / 2 - 50, ship_mode_img, self.buttons_scale,
                                              self.enter_ship_mode)
        self.grab_coin_button = button.Button(self.panel_buttons_x + 300 * self.buttons_scale, self.y / 2 - 50,
                                              grab_coin_img, self.buttons_scale, self.grab_coin)
        self.drop_coin_button = button.Button(self.panel_buttons_x + 300 * self.buttons_scale, self.y / 2 - 50,
                                              drop_coin_img, self.buttons_scale, self.drop_coin)
        self.revive_pirate_button = button.Button(self.panel_buttons_x + 600 * self.buttons_scale, self.y / 2 - 50,
                                                  revive_pirate_img, self.buttons_scale, self.revive_pirate)

        self.dead_pirate_size = self.panel_width * 0.1
        self.dead_pirate_image = pygame.transform.scale(dead_pirate_img, (self.dead_pirate_size, self.dead_pirate_size))

    def set_players(self, count):
        self.players = []
        for i in range(count):
            self.players.append(Player(self.screen, self.board.field, player_colors[i]))
        self.update_active_pirate()

    def click_cell(self, cell):
        effect_cards = ['HORSE', 'BALLOON', 'PLANE', 'ICE', 'CROCODILE',
                        'GUN_TOP', 'ARROW_1S', 'ARROW_2S', 'ARROW_1D',
                        'ARROW_2D', 'ARROW_3', 'ARROW_4D', 'ARROW_4S', 'GUN_BOTTOM', 'GUN_LEFT', 'GUN_RIGHT']
        current_player = self.get_current_player()
        enemy_ship_in_cell = self.check_enemy_ship_in_cell(cell)

        if enemy_ship_in_cell:
            self.change_player()
            return

        sound = audio.steps_sound
        enemies_in_cell = self.check_enemies_in_cell(cell)
        move_end = False

        if enemies_in_cell:
            sound = None

        if current_player.mode == 'pirate':
            current_player.move_pirate(cell)
        elif current_player.mode == 'ship':
            current_player.move_ship(cell)

        for pirate in current_player.pirates:
            if pirate.can_move:
                continue

            pirate_cell = self.field.get_cell_by_pos(pirate.column, pirate.row)

            if pirate_cell.card_type == 'KEG':
                pirate.can_move = True

        if cell.card_type in effect_cards:
            current_player.auto_steps += 1
            if current_player.auto_steps > 20:
                current_player.get_active_pirate().die(cell)
                self.change_player()
                return

            current_player.another_step_mode = True
            self.field.update_available_cells(cell.column, cell.row, current_player,
                                              card_types.card_types[cell.card_type]['available cells'])

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
            elif cell.card_type == 'PITFALL':
                self.enter_pitfall(cell, current_player)
            elif cell.card_type == 'CANNIBAL':
                current_player.get_active_pirate().die(cell)
            move_end = True
            self.change_player()

        if sound:
            sound.play()

        if move_end:
            return

        available_cells = self.field.get_available_cells()

        if len(available_cells) == 1 and current_player.mode == 'pirate':
            self.click_cell(available_cells[0])

    def check_enemies_in_cell(self, cell):
        enemies_in_cell = False

        for i, player in enumerate(self.players):
            if i != self.current_player:
                for pirate in player.pirates:
                    if pirate.column == cell.column and pirate.row == cell.row:
                        if self.get_current_player().mode == 'pirate':
                            player.respawn_pirate(pirate, cell)
                        else:
                            pirate.die(cell)
                        enemies_in_cell = True

        return enemies_in_cell

    def check_enemy_ship_in_cell(self, cell):
        ship_in_cell = False

        for i, player in enumerate(self.players):
            if i != self.current_player and player.ship.column == cell.column and player.ship.row == cell.row:
                self.get_current_player().get_active_pirate().die(cell)
                ship_in_cell = True
                break

        return ship_in_cell

    def change_player(self):
        sum = self.calculate_coins()
        if sum == 37:
            winner = self.get_winner()
            finish_event = pygame.event.Event(OPEN_FINISH_GAME, winner=winner)
            pygame.event.post(finish_event)
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0
        self.update_forts_colors()
        self.get_current_player().enter_pirate_mode()
        self.update_active_pirate()
        self.update_dead_pirates()
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
                
    def update_forts_colors(self):
        for cell in self.field.cells:
            if cell.card_type == 'FORT' or cell.card_type == 'FORT_LIVE':
                cell.fort_color = None
                for player in self.players:
                    for pirate in player.pirates:
                        if pirate.column == cell.column and pirate.row == cell.row:
                            cell.fort_color = player.color

    def update_dead_pirates(self):
        self.dead_pirates = self.get_current_player().get_dead_pirates()

    def back_to_menu(self):
        menu_event = pygame.event.Event(OPEN_MENU_SCREEN, resume=True)
        pygame.event.post(menu_event)

    def get_current_player(self):
        return self.players[self.current_player]

    def get_current_cell(self):
        current_player = self.get_current_player()

        if current_player.mode == 'ship':
            active_item = current_player.ship
        else:
            active_item = current_player.get_active_pirate()

        return self.field.get_cell_by_pos(active_item.column, active_item.row)

    def pass_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()

            for pirate in self.get_current_player().pirates:
                if pirate.rect.collidepoint(mouse_pos) and not (pirate.active) and pirate.alive:
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

    def grab_coin(self):
        current_player = self.get_current_player()
        current_cell = self.get_current_cell()

        current_player.get_active_pirate().grab_coin(current_cell)
        self.field.update_available_cells(current_cell.column, current_cell.row, current_player)

    def drop_coin(self):
        current_player = self.get_current_player()
        current_cell = self.get_current_cell()

        current_player.get_active_pirate().drop_coin(current_cell)
        self.field.update_available_cells(current_cell.column, current_cell.row, current_player)

    def revive_pirate(self):
        current_player = self.get_current_player()
        current_cell = self.get_current_cell()
        current_player.revive_pirate(current_cell)
        self.change_player()

    def enter_pitfall(self, cell, player):
        active_pirate = player.get_active_pirate()
        is_occupied = False
        for pirate in player.pirates:
            if (pirate.index != active_pirate.index and pirate.column == cell.column
                    and pirate.row == cell.row):
                pirate.can_move = True
                is_occupied = True

        if not is_occupied:
            active_pirate.can_move = False

    def draw(self):
        self.board.draw()
        self.draw_players()
        self.draw_panel()
        self.quit_button.draw(self.screen)

    def draw_players(self):
        for player in self.players:
            player.draw()

    def draw_panel(self):
        pygame.draw.rect(self.screen, '#368df9', (self.panel_x, self.panel_y, self.panel_width, self.panel_height))
        self.draw_mode_button()
        self.draw_coin_button()
        self.draw_revive_pirate_button()
        self.draw_players_coins()
        self.draw_dead_pirates()

    def draw_mode_button(self):
        if self.get_current_player().mode == 'pirate':
            self.ship_mode_button.draw(self.screen)
        else:
            self.pirate_mode_button.draw(self.screen)

    def draw_coin_button(self):
        current_player = self.get_current_player()

        if current_player.mode == 'ship':
            return

        active_pirate = current_player.get_active_pirate()

        if active_pirate.with_coin:
            self.drop_coin_button.draw(self.screen)
        else:
            cell_column, cell_row = [active_pirate.column, active_pirate.row]
            current_cell = self.field.get_cell_by_pos(cell_column, cell_row)

            if current_cell and current_cell.coin and current_cell.coin.quantity > 0:
                self.grab_coin_button.draw(self.screen)

    def draw_revive_pirate_button(self):
        current_player = self.get_current_player()

        if current_player.mode == 'ship':
            return

        active_pirate = current_player.get_active_pirate()
        cell_column, cell_row = [active_pirate.column, active_pirate.row]
        current_cell = self.field.get_cell_by_pos(cell_column, cell_row)

        if current_cell.card_type == 'FORT_LIVE' and len(current_player.get_dead_pirates()) > 0:
            self.revive_pirate_button.draw(self.screen)

    def draw_players_coins(self):
        pirate_size = self.x * 0.04
        pirate_offset = pirate_size * 1.4
        pirates_x = self.panel_x + (self.panel_width / 2 - len(self.players) * pirate_offset / 2)
        font_size = round(pirate_size * 0.2)

        for i, player in enumerate(self.players):
            is_current = i == self.current_player
            size = pirate_size * 1.2 if is_current else pirate_size
            coin_size = size * 0.8
            pirate_x = pirates_x + i * pirate_offset
            pirate_y = self.panel_y + self.panel_height * 0.2
            coin_x = pirate_x + (size - coin_size) / 2
            coin_y = pirate_y + pirate_size
            pirate_image = pygame.transform.scale(pirates_img[player.color], (size, size))
            coin_image = pygame.transform.scale(coin_img, (coin_size, coin_size))
            circle_size = round(coin_size * 0.3)
            circle_x = coin_x + coin_size / 2
            circle_y = coin_y + coin_size
            font = pygame.font.SysFont("arialblack", font_size)

            self.screen.blit(pirate_image, (pirate_x, pirate_y))
            self.screen.blit(coin_image, (coin_x, coin_y))

            text = font.render(f'{player.coins}', True, '#FFFFFF')
            text_rect = text.get_rect(center=(circle_x, circle_y))
            pygame.draw.circle(self.screen, '#000000', (circle_x, circle_y), circle_size)
            self.screen.blit(text, text_rect)

    def draw_dead_pirates(self):
        dead_pirates_count = len(self.dead_pirates)

        if dead_pirates_count > 0:
            for i in range(dead_pirates_count):
                dead_pirate_x = self.panel_x + self.panel_width - 50 - i * self.dead_pirate_size
                dead_pirate_y = self.panel_y + self.panel_height - self.dead_pirate_size * 1.2
                self.screen.blit(self.dead_pirate_image, (dead_pirate_x, dead_pirate_y))
        return self.players[self.current_player]
    
    def get_current_cell(self):
        current_player = self.get_current_player()

        if current_player.mode == 'ship':
            active_item = current_player.ship
        else:
            active_item = current_player.get_active_pirate()

        return self.field.get_cell_by_pos(active_item.column, active_item.row)

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
        if not self.get_current_player().another_step_mode:
            self.get_current_player().enter_pirate_mode()
               
    def enter_ship_mode(self):
        if not self.get_current_player().another_step_mode:
            self.get_current_player().enter_ship_mode()

    def grab_coin(self):
        current_player = self.get_current_player()
        current_cell = self.get_current_cell()

        current_player.get_active_pirate().grab_coin(current_cell)
        self.field.update_available_cells(current_cell.column, current_cell.row, current_player)
    
    def drop_coin(self):
        current_player = self.get_current_player()
        current_cell = self.get_current_cell()

        current_player.get_active_pirate().drop_coin(current_cell)
        self.field.update_available_cells(current_cell.column, current_cell.row, current_player)

    def revive_pirate(self):
        current_player = self.get_current_player()
        current_cell = self.get_current_cell()
        current_player.revive_pirate(current_cell)
        self.change_player()

    def draw(self):
        self.board.draw()
        self.draw_players()
        self.draw_panel()
        self.quit_button.draw(self.screen)

    def draw_players(self):
        for player in self.players:
            player.draw()

    def draw_panel(self):
        pygame.draw.rect(self.screen, '#368df9', (self.panel_x, self.panel_y, self.panel_width, self.panel_height))
        self.draw_mode_button()
        self.draw_coin_button()
        self.draw_revive_pirate_button()
        self.draw_players_coins()
        self.draw_dead_pirates()

    def draw_mode_button(self):
        if self.get_current_player().mode == 'pirate':
            self.ship_mode_button.draw(self.screen)
        else:
            self.pirate_mode_button.draw(self.screen)

    def draw_coin_button(self):
        current_player = self.get_current_player()

        if current_player.mode == 'ship':
            return
        
        active_pirate = current_player.get_active_pirate()

        if active_pirate.with_coin:
            self.drop_coin_button.draw(self.screen)
        else:
            cell_column, cell_row = [active_pirate.column, active_pirate.row]
            current_cell = self.field.get_cell_by_pos(cell_column, cell_row)

            if current_cell.coin and current_cell.coin.quantity > 0:
                self.grab_coin_button.draw(self.screen)
    
    def draw_revive_pirate_button(self):
        current_player = self.get_current_player()

        if current_player.mode == 'ship':
            return
        
        active_pirate = current_player.get_active_pirate()
        cell_column, cell_row = [active_pirate.column, active_pirate.row]
        current_cell = self.field.get_cell_by_pos(cell_column, cell_row)

        if current_cell.card_type == 'FORT_LIVE' and len(current_player.get_dead_pirates()) > 0:
            self.revive_pirate_button.draw(self.screen)

    def draw_players_coins(self):
        pirate_size = self.x * 0.04
        pirate_offset = pirate_size * 1.4
        pirates_x = self.panel_x + (self.panel_width / 2 - len(self.players) * pirate_offset / 2)
        font_size = round(pirate_size * 0.2)

        for i, player in enumerate(self.players):
            is_current = i == self.current_player
            size = pirate_size * 1.2 if is_current else pirate_size
            coin_size = size * 0.8
            pirate_x = pirates_x + i * pirate_offset
            pirate_y = self.panel_y + self.panel_height * 0.2
            coin_x = pirate_x + (size - coin_size) / 2
            coin_y = pirate_y + pirate_size
            pirate_image = pygame.transform.scale(pirates_img[player.color], (size, size))
            coin_image = pygame.transform.scale(coin_img, (coin_size, coin_size))
            circle_size = round(coin_size * 0.3)
            circle_x = coin_x + coin_size / 2
            circle_y = coin_y + coin_size
            font = pygame.font.SysFont("arialblack", font_size)

            self.screen.blit(pirate_image, (pirate_x, pirate_y))
            self.screen.blit(coin_image, (coin_x, coin_y))

            text = font.render(f'{player.coins}', True, '#FFFFFF')
            text_rect = text.get_rect(center=(circle_x, circle_y))
            pygame.draw.circle(self.screen, '#000000', (circle_x, circle_y), circle_size)
            self.screen.blit(text, text_rect)

    def draw_dead_pirates(self):
        dead_pirates_count = len(self.dead_pirates)

        if dead_pirates_count > 0:
            for i in range(dead_pirates_count):
                dead_pirate_x = self.panel_x + self.panel_width - 50 - i * self.dead_pirate_size
                dead_pirate_y = self.panel_y + self.panel_height - self.dead_pirate_size * 1.2
                self.screen.blit(self.dead_pirate_image, (dead_pirate_x, dead_pirate_y))

    def calculate_coins(self):
        sum = 0
        for player in self.players:
            sum += player.coins
        return sum

    def get_winner(self):
        max = 0
        winner = ''
        for player in self.players:
            if player.coins > max:
                max = player.coins
                winner = player.color
        return winner