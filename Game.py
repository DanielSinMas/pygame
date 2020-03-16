from Constants import *
import pygame
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

from Utilities.MapProcessor import MapProcessor
from entities.Camera import Camera
from entities.Obstacle import Obstacle
from entities.Transition import Transition
from entities.player import Player


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.transitions = pygame.sprite.Group()
        self.player = Player(self, 0, 0)
        self.player_interaction_allowed = False
        self.map_processor = MapProcessor(self, 'maps/map1/map1.tmx')

    def load_data(self, map):
        self.map_processor.change_map(map)
        self.new()
        self.fade_out()
        self.fade_in()

    def new(self):
        self.all_sprites.empty()
        self.walls.empty()
        self.transitions.empty()
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.transitions = pygame.sprite.Group()

        for tile_object in self.map_processor.tiled_map.tmxdata.objects:
            if tile_object.name == 'Player':
                self.player = Player(self, tile_object.x, tile_object.y)
            elif tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            elif tile_object.name == 'transition':
                Transition(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tile_object.goto)
        self.camera = Camera(self.map_processor.tiled_map.width, self.map_processor.tiled_map.height)

    def run(self):
        self.playing = True
        self.dt = self.clock.tick(FPS) / 100
        self.load_data('maps/map1/map1.tmx')
        while self.playing:
            self.dt = self.clock.tick(FPS) / 100
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.map_processor.processed_map, self.camera.apply_rect(self.map_processor.processed_map.get_rect()))
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
        self.player_interaction_allowed = False
        for alpha in range(0, 100):
            fade_surface.set_alpha(alpha)
            self.screen.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5)

    def fade_in(self):
        fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.update()
        for alpha in range(0, 300):
            fade_surface.set_alpha(alpha)
            self.map_processor.processed_map.set_alpha(alpha)
            self.draw()
            #self.screen.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.delay(1)
        self.player_interaction_allowed = True

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
