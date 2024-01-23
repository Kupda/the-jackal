import pygame
import button
from .events import OPEN_MENU_SCREEN
from audio import audio


back_img = pygame.image.load('images/button_quit2.png')
sound_on_img = pygame.image.load('images/on_sound.png')
sound_off_img = pygame.image.load('images/off_sound.png')
music_on_img = pygame.image.load('images/on_music.png')
music_off_img = pygame.image.load('images/off_music.png')


class SettingsScreen():
    def __init__(self, screen, font):
        self.x, self.y = screen.get_size()
        self.font = font
        self.screen = screen
        self.back_button = button.Button(self.x / 2 - 150, self.y / 2 + 150, back_img, 0.75, self.back_to_menu)

        self.sound_on_btn = button.Button(self.x / 2 - 150, self.y / 2 - 150, sound_on_img, 0.75, self.toggle_sound)
        self.sound_off_btn = button.Button(self.x / 2 - 150, self.y / 2 - 150, sound_off_img, 0.75, self.toggle_sound)
        self.music_on_btn = button.Button(self.x / 2 - 150, self.y / 2 + 0, music_on_img, 0.75, self.toggle_music)
        self.music_off_btn = button.Button(self.x / 2 - 150, self.y / 2 + 0, music_off_img, 0.75, self.toggle_music)

    def draw_text(self, text, text_col):
        img = self.font.render(text, True, text_col)
        text_rect = img.get_rect(center=(self.x / 2, self.y / 2 - 300))
        self.screen.blit(img, text_rect)

    def draw(self):
        self.draw_text("НАСТРОЙКИ", 'white')
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
