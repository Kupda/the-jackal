import pygame
import button
import time
import os
from .events import *


resume_img = pygame.image.load("images/start_game.png")
options_img = pygame.image.load("images/options.png")
quit_img = pygame.image.load("images/quit.png")
replay_img = pygame.image.load("images/replay.png")
video_img = pygame.image.load('images/button_video.png')
audio_img = pygame.image.load('images/button_audio.png')
keys_img = pygame.image.load('images/button_keys.png')
back_img = pygame.image.load('images/button_back.png')
TEXT_COL = (255, 255, 255)


class MenuScreen():
    def __init__(self, screen, font):
        self.x, self.y = screen.get_size()
        self.font = font
        self.screen = screen
        self.resume_button = button.Button(self.x / 2 - 150, self.y / 2 - 150, resume_img, 0.75, self.start_game)
        self.replay_button = button.Button(self.x / 2 - 150, self.y / 2 + 0, replay_img, 0.75)
        self.options_button = button.Button(self.x / 2 - 150, self.y / 2 + 150, options_img, 0.75, self.open_settings)
        self.quit_button = button.Button(self.x / 2 - 150, self.y / 2 + 300, quit_img, 0.75, self.quit_game)

    def draw_text(self, text, text_col, x, y):
        img = self.font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def draw(self):
        self.draw_text("GAME", TEXT_COL, self.x / 2 - 50, self.y / 2 - 300)
        self.resume_button.draw(self.screen)
        self.replay_button.draw(self.screen)
        self.options_button.draw(self.screen)
        self.quit_button.draw(self.screen)

    def quit_game(self):
        quit_event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(quit_event)

    def open_settings(self):
        open_settings_event = pygame.event.Event(OPEN_SETTINGS_SCREEN)
        pygame.event.post(open_settings_event)

    def start_game(self):
        start_game_event = pygame.event.Event(OPEN_PLAYERS_SCREEN)
        pygame.event.post(start_game_event)