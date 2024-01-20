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

# game variables
game_paused = True
game_state = "menu"


# define fonts
font = pygame.font.SysFont("arialblack", 40)

menu_screen = menu_screen.MenuScreen(screen, font)
settings_screen = settings_screen.SettingsScreen(screen, font)
game_screen = game_screen.GameScreen(screen)
players_screen = players_screen.PlayersScreen(screen, font)

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
while run:
    screen.fill('#94ac80')
    # check if game is paused
    if game_paused:
        # check menu state
        if game_state == "menu":
            menu_screen.draw()
        if game_state == 'settings':
            settings_screen.draw()
        if game_state == 'game':
            game_screen.draw()
        if game_state == 'players':
            players_screen.draw()
            """# draw pause screen buttons
            if resume_button.draw(screen):
                game_paused = False
            if replay_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        # check if the options menu is open
        if menu_state == "options":
            # draw the different options buttons
            if back_button.draw(screen):
                menu_state = "main"
                time.sleep(0.1)"""
    else:
        draw_text("Gaming. Press SPACE to pause", font, TEXT_COL, 160, 250)
    clock.tick(200)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
        if event.type == events.OPEN_MENU_SCREEN:
            game_state = "menu"
        if event.type == events.OPEN_SETTINGS_SCREEN:
            game_state = "settings"
        if event.type == events.OPEN_GAME_SCREEN:
            game_screen.set_players(event.count)
            game_state = "game"
        if event.type == events.OPEN_PLAYERS_SCREEN:
            game_state = "players"
        if event.type == events.CLICK_CELL:
            game_screen.click_cell(event.column, event.row)
    pygame.display.update()
pygame.quit()
