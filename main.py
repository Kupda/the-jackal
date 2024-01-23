import pygame
from screens import menu_screen, settings_screen, events, game_screen, players_screen, finish_screen

pygame.init()

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Main Menu")
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

game_paused = True

font = pygame.font.SysFont("arialblack", 40)

menu_screen = menu_screen.MenuScreen(screen, font)
settings_screen = settings_screen.SettingsScreen(screen, font)
game_screen = game_screen.GameScreen(screen)
players_screen = players_screen.PlayersScreen(screen, font)
finish_screen = finish_screen.FinishScreen(screen, font)

active_screen = menu_screen

TEXT_COL = (255, 255, 255)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


run = True
clock = pygame.time.Clock()
fps = 60
while run:
    screen.fill('#94ac80')
    active_screen.draw()
    clock.tick(fps)
    for event in pygame.event.get():
        active_screen.pass_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
        if event.type == events.OPEN_MENU_SCREEN:
            resume = False
            if hasattr(event, 'resume'):
                resume = event.resume
            menu_screen.resume_available = resume
            active_screen = menu_screen
        if event.type == events.OPEN_SETTINGS_SCREEN:
            active_screen = settings_screen
        if event.type == events.OPEN_GAME_SCREEN:
            if hasattr(event, 'count'):
                game_screen.start_game()
                game_screen.set_players(event.count)
            active_screen = game_screen
        if event.type == events.OPEN_PLAYERS_SCREEN:
            active_screen = players_screen
        if event.type == events.OPEN_FINISH_GAME:
            finish_screen.winner = event.winner
            active_screen = finish_screen
    pygame.display.update()
pygame.quit()
