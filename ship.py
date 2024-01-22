import pygame


ship_img = pygame.image.load('images/ship.png')


class Ship():
    def __init__(self, screen, column, row, x, y, color, size, has_pirates=True, active=False):
        self.screen = screen
        self.column = column
        self.row = row
        self.x = x
        self.y = y
        self.swing_y = 0
        self.swing_direction = -0.3
        self.color = color
        self.has_pirates = has_pirates
        self.active = active
        self.size = size
        if row == 6:
            self.movement = 'vertical'
        else:
            self.movement = 'horizontal'
        self.image = pygame.transform.scale(ship_img, (self.size, self.size))

    def draw(self):
        y = self.y

        if self.active:
            self.swing()
            y += self.swing_y

        self.screen.blit(self.image, (self.x, y))

    def add_pirates(self):
        self.has_pirates = True

    def remove_pirates(self):
        self.has_pirates = False

    def set_active(self, active):
        self.active = active

        if active:
            self.start_swinging()

    def swing(self):
        if self.swing_y <= -5:
            self.swing_direction = 0.3
        elif self.swing_y >= 0:
            self.swing_direction = -0.3

        self.swing_y += self.swing_direction

    def start_swinging(self):
        self.swing_y = 0
        self.swing_direction = -0.3

    def move(self, cell):
        self.x = cell.x
        self.y = cell.y
        self.column = cell.column
        self.row = cell.row