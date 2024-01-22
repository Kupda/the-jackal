import pygame
import button
import time
from screens import menu_screen, settings_screen, events, game_screen, players_screen
from audio import audio



pygame.init()

# create game window
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Main Menu")
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

# game variables
game_paused = True


# define fonts
font = pygame.font.SysFont("arialblack", 40)

menu_screen = menu_screen.MenuScreen(screen, font)
settings_screen = settings_screen.SettingsScreen(screen, font)
game_screen = game_screen.GameScreen(screen)
players_screen = players_screen.PlayersScreen(screen, font)

active_screen = menu_screen

# define colours
TEXT_COL = (255, 255, 255)


"""video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)"""
#back_button = button.Button(x / 2 - 150, y / 2 + 300, quit_img, 0.75)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# game loop
run = True
clock = pygame.time.Clock()
fps = 60
while run:
    screen.fill('#94ac80')
    active_screen.draw()
    clock.tick(fps)

    # event handler
    for event in pygame.event.get():
        active_screen.pass_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
        if event.type == events.OPEN_MENU_SCREEN:
            active_screen = menu_screen
        if event.type == events.OPEN_SETTINGS_SCREEN:
            active_screen = settings_screen
        if event.type == events.OPEN_GAME_SCREEN:
            game_screen.set_players(event.count)
            active_screen = game_screen
        if event.type == events.OPEN_PLAYERS_SCREEN:
            active_screen = players_screen
    pygame.display.update()
pygame.quit()
