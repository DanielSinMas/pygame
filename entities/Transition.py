import pygame

from entities.BaseEntity import BaseEntity


class Transition(BaseEntity):

    def __init__(self,game, position_x, position_y, width, height, goto):
        self.groups = game.transitions
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(position_x, position_y, width, height)
        self.x = position_x
        self.y = position_y
        self.rect.width = width
        self.rect.height = height
        self.go_to = goto