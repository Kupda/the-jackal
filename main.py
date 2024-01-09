import pygame
import button
import time

pygame.init()

# create game window
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Main Menu")

# game variables
game_paused = True
menu_state = "main"

# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colours
TEXT_COL = (255, 255, 255)

# load button images
resume_img = pygame.image.load("images/start_game.png").convert_alpha()
options_img = pygame.image.load("images/options.png").convert_alpha()
quit_img = pygame.image.load("images/quit.png").convert_alpha()
replay_img = pygame.image.load("images/replay.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

x, y = screen.get_size()

# create button instances
resume_button = button.Button(x / 2 - 150, y / 2 - 150, resume_img, 0.75)
replay_button = button.Button(x / 2 - 150, y / 2 + 0, replay_img, 0.75)
options_button = button.Button(x / 2 - 150, y / 2 + 150, options_img, 0.75)
quit_button = button.Button(x / 2 - 150, y / 2 + 300, quit_img, 0.75)


"""video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)"""
back_button = button.Button(x / 2 - 150, y / 2 + 300, quit_img, 0.75)


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
        if menu_state == "main":
            draw_text("GAME", font, TEXT_COL, x / 2 - 50, y / 2 - 300)
            # draw pause screen buttons
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
                time.sleep(0.1)
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
    pygame.display.update()
pygame.quit()

