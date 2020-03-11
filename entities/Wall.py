from Constants import *
from entities.BaseEntity import *


class Wall(BaseEntity):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.color = GREEN
        self.x = x
        self.y = y
        self.__print__()

    def __print__(self):
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def player_interaction(self):
        self.change_color()

    def change_color(self):
        if self.color == GREEN:
            self.color = RED
        elif self.color == RED:
            self.color = GREEN
        self.__print__()
