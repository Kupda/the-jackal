import pygame
import button
from .events import OPEN_MENU_SCREEN, OPEN_GAME_SCREEN


players2 = pygame.image.load("images/players2.png")
players3 = pygame.image.load("images/players3.png")
players4 = pygame.image.load("images/players4.png")
back_img = pygame.image.load('images/quit.png')


class PlayersScreen():
    def __init__(self, screen, font):
        self.x, self.y = screen.get_size()
        self.screen = screen
        self.font = font
        self.player2_btn = button.Button(self.x / 2 - 150, self.y / 2 - 150, players2, 0.75, self.select_player2)
        self.player3_btn = button.Button(self.x / 2 - 150, self.y / 2 + 0, players3, 0.75, self.select_player3)
        self.player4_btn = button.Button(self.x / 2 - 150, self.y / 2 + 150, players4, 0.75, self.select_player4)
        self.back_button = button.Button(self.x / 2 - 150, self.y / 2 + 300, back_img, 0.75, self.back_to_menu)

    def back_to_menu(self):
        back_event = pygame.event.Event(OPEN_MENU_SCREEN)
        pygame.event.post(back_event)

    def draw_text(self, text, text_col, x, y):
        img = self.font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def draw(self):
        self.draw_text("Choose player count", "black", self.x / 2 - 50, self.y / 2 - 300)
        self.player2_btn.draw(self.screen)
        self.player3_btn.draw(self.screen)
        self.player4_btn.draw(self.screen)
        self.back_button.draw(self.screen)

    def select_player2(self):
        self.start_game(2)

    def select_player3(self):
        self.start_game(3)

    def select_player4(self):
        self.start_game(4)

    def start_game(self, count):
        start_event = pygame.event.Event(OPEN_GAME_SCREEN, count=count)
        pygame.event.post(start_event)

    def pass_event(self, event):
        pass