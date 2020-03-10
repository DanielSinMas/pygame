from os import path
from entities.Wall import Wall

class FileProcessor:
    def __init__(self, game):
        self.game = game

    def processFile(self, file):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, file), 'rt') as file:
            for line in file:
                self.map_data.append(line)

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self.game, col, row)