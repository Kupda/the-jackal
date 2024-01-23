import pygame
import button
from .events import OPEN_MENU_SCREEN, OPEN_PLAYERS_SCREEN


quit_img = pygame.image.load("images/button_quit2.png")
replay_img = pygame.image.load("images/button_replay.png")


class FinishScreen():
    def __init__(self, screen, font):
        self.x, self.y = screen.get_size()
        self.font = font
        self.screen = screen
        self.winner = ''
        self.replay_button = button.Button(self.x / 2 - 150, self.y / 2 + 0, replay_img, 0.75, self.replay)
        self.quit_button = button.Button(self.x / 2 - 150, self.y / 2 + 300, quit_img, 0.75, self.back_to_menu)

    def draw_text(self, text, text_col):
        img = self.font.render(text, True, text_col)
        text_rect = img.get_rect(center=(self.x / 2, self.y / 2 - 300))
        self.screen.blit(img, text_rect)

    def draw(self):
        self.draw_text(f"{self.winner} ПОБЕДИЛ", 'white')
        self.replay_button.draw(self.screen)
        self.quit_button.draw(self.screen)

    def back_to_menu(self):
        back_event = pygame.event.Event(OPEN_MENU_SCREEN)
        pygame.event.post(back_event)

    def replay(self):
        replay_event = pygame.event.Event(OPEN_PLAYERS_SCREEN)
        pygame.event.post(replay_event)

    def pass_event(self, event):
        pass
