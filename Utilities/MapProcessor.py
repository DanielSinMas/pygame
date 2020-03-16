from Utilities.TiledMap import TiledMap


class MapProcessor:
    def __init__(self, game, initial_map):
        self.game = game
        self.initial_map = initial_map
        self.tiled_map = TiledMap(initial_map)
        self.processed_map = self.tiled_map.make_map()

    def change_map(self, new_map):
        self.tiled_map = TiledMap(new_map)
        self.processed_map = self.tiled_map.make_map()
        return self.processed_map
