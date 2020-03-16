import pygame
from pytmx import pytmx
from pytmx.util_pygame import load_pygame


class TiledMap:
    def __init__(self, filename):
        tm = load_pygame(filename)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.imagemap.items()
        for indice, layer in enumerate(self.tmxdata.visible_layers):
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmxdata.get_tile_image(x, y, indice)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    def make_map(self):
        surface = pygame.Surface((self.width, self.height))
        self.render(surface)
        return surface
