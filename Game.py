from Constants import *
import pygame
from Utilities.FileProcessor import FileProcessor
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

from Utilities.TiledMap import TiledMap
from entities.Camera import Camera
from entities.Obstacle import Obstacle
from entities.Transition import Transition
from entities.player import Player


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.transitions = pygame.sprite.Group()
        self.player = Player(self, 0, 0)
        self.load_data('maps/map1/map1.tmx')

    def load_data(self, map):
        self.tiledmap = TiledMap(map)
        self.map = self.tiledmap.make_map()
        self.new()

    def new(self):
        self.all_sprites.empty()
        self.walls.empty()
        self.transitions.empty()
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.transitions = pygame.sprite.Group()

        pygame.time.wait(500)

        for tile_object in self.tiledmap.tmxdata.objects:
            if tile_object.name == 'Player':
                self.player = Player(self, tile_object.x, tile_object.y)
            elif tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            elif tile_object.name == 'transition':
                Transition(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tile_object.goto)
        self.camera = Camera(self.tiledmap.width, self.tiledmap.height)

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
        # self.draw_grid()
        print(self.clock)
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.map, self.camera.apply_rect(self.map.get_rect()))
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
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    self.player.action_pressed()

    def fade_out(self):
        fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        fade_surface.fill((0, 0, 0))
        for alpha in range(0, 300):
            print(alpha)
            fade_surface.set_alpha(alpha)
            self.screen.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
