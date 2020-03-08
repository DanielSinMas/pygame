import pygame
import random
from Constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center = (
                random.randint(0, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        #self.speed = random.randint(0, 3)

    def update(self):
        self.rect.move_ip(0, 0)
        if self.rect.right < 0:
            self.kill
