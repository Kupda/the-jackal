import button
from .events import *


resume_img = pygame.image.load("images/resume1.png")
options_img = pygame.image.load("images/options.png")
quit_img = pygame.image.load("images/quit.png")
replay_img = pygame.image.load("images/start_game.png")


class MenuScreen():
    def __init__(self, screen, font):
        self.x, self.y = screen.get_size()
        self.font = font
        self.screen = screen
        self.resume_available = False
        self.resume_button = button.Button(self.x / 2 - 150, self.y / 2 - 150, resume_img, 0.75, self.resume_game)
        self.replay_button = button.Button(self.x / 2 - 150, self.y / 2 - 0, replay_img, 0.75, self.start_game)
        self.options_button = button.Button(self.x / 2 - 150, self.y / 2 + 150, options_img, 0.75, self.open_settings)
        self.quit_button = button.Button(self.x / 2 - 150, self.y / 2 + 300, quit_img, 0.75, self.quit_game)

    def draw_text(self, text, text_col):
        img = self.font.render(text, True, text_col)
        text_rect = img.get_rect(center=(self.x / 2, self.y / 2 - 300))
        self.screen.blit(img, text_rect)

    def draw(self):
        self.draw_text("ШАКАЛ", 'white')
        if self.resume_available:
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

    def pass_event(self, event):
        pass

    def resume_game(self):
        if self.resume_available:
            resume_game_event = pygame.event.Event(OPEN_GAME_SCREEN)
            pygame.event.post(resume_game_event)