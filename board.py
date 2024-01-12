import pygame
import math

water_image_file = pygame.image.load('images/water_tile.png')


class Board():
    def __init__(self, screen, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.screen = screen

    def draw_background(self):
        water_image = water_image_file
        tile_size = 225
        water_tiles_cols = math.ceil(self.window_width / tile_size)
        water_tiles_rows = math.ceil(self.window_height / tile_size)
        water_image.set_alpha(180)

        for x in range(water_tiles_cols):
            for y in range(water_tiles_rows):
                self.screen.blit(water_image, (x * tile_size, y * tile_size))