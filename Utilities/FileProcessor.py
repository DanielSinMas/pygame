from os import path
from Constants import *

class FileProcessor:
    def __init__(self, game, file):
        self.game = game
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, file), 'rt') as file:
            for line in file:
                self.map_data.append(line.strip())

        self.tilewidth = len(self.map_data[0])
        self.tileheight = len(self.map_data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE