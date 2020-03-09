import pygame
from Constants import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, movementX = 0, movementY = 0):
        if not self.collide_with_wall(movementX, movementY):
            self.x += movementX
            self.y += movementY

    def collide_with_wall(self, movementX=0, movementY=0):
        for wall in self.game.walls:
            if wall.x == self.x + movementX and wall.y == self.y + movementY:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
