from Constants import *
import pygame
from Utilities.FileProcessor import FileProcessor
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from entities.Camera import Camera
from entities.Wall import Wall
from entities.player import Player


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        self.processor = FileProcessor(self, '../maps/level2.txt')

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tiles in enumerate(self.processor.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        self.camera = Camera(self.processor.width, self.processor.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 100
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.fill(BGCOLOR)
        #self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (SCREEN_WIDTH, y))

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
