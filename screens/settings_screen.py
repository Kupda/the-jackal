import pygame
import button
import time
import os
from .events import OPEN_MENU_SCREEN
from audio import audio


back_img = pygame.image.load('images/quit.png')
sound_on_img = pygame.image.load('images/on_sound.png')
sound_off_img = pygame.image.load('images/off_sound.png')
music_on_img = pygame.image.load('images/on_music.png')
music_off_img = pygame.image.load('images/off_music.png')
TEXT_COL = (255, 255, 255)


class SettingsScreen():
    def __init__(self, screen, font):
        self.x, self.y = screen.get_size()
        self.font = font
        self.screen = screen
        self.back_button = button.Button(100, 50, back_img, 0.75, self.back_to_menu)

        self.sound_on_btn = button.Button(self.x / 2 - 150, self.y / 2 - 150, sound_on_img, 0.75, self.toggle_sound)
        self.sound_off_btn = button.Button(self.x / 2 - 150, self.y / 2 - 150, sound_off_img, 0.75, self.toggle_sound)
        self.music_on_btn = button.Button(self.x / 2 - 150, self.y / 2 + 0, music_on_img, 0.75, self.toggle_music)
        self.music_off_btn = button.Button(self.x / 2 - 150, self.y / 2 + 0, music_off_img, 0.75, self.toggle_music)

    def draw_text(self, text, text_col, x, y):
        img = self.font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def draw(self):
        self.draw_text("Settings", TEXT_COL, self.x / 2 - 50, self.y / 2 - 300)
        self.back_button.draw(self.screen)
        if audio.sounds_muted:
            self.sound_on_btn.draw(self.screen)
        else:
            self.sound_off_btn.draw(self.screen)

        if audio.music_muted:
            self.music_on_btn.draw(self.screen)
        else:
            self.music_off_btn.draw(self.screen)

    def back_to_menu(self):
        back_event = pygame.event.Event(OPEN_MENU_SCREEN)
        pygame.event.post(back_event)

    def toggle_sound(self):
        audio.toggle_sounds()

    def toggle_music(self):
        audio.toggle_music()

    def pass_event(self, event):
        pass
