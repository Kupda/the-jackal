import pygame


pirate_img = pygame.image.load('images/pirate.png')


class Pirate():
    def __init__(self, x, y, check_number, color, alive=True, with_coin=False, can_move=True):
        self.x = x
        self.y = y
        self.check_number = check_number
        self.alive = alive
        self.with_coin = with_coin
        self.can_move = can_move
        self.color = color
        self.image = pygame.transform.scale(pirate_img, (75, 75))


    def die(self):
        self.alive = False

    def revive(self):
        self.alive = True

    def drop_coin(self):
        self.with_coin = False

    def bring_coin(self):
        self.with_coin = True

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))