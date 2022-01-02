from config import *

# maybe we can dictate a defense and production value based off of the territory_type?
# ocean and mountain can be impassable but others like forest plains or swamp dictate the defense and production value?
# we can also generate it to some random int within a range to keep things interesting


class Territory:
    def __init__(self, game, x, y, color):
        self.game = game
        self.color = color
        self.adjacent_territories = []
        self.index = (x, y)
        self.adjacent_points = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]

    @staticmethod
    def convert_2d_to_1d(index_tuple):
        return index_tuple[1] * 8 + index_tuple[0]

    def get_adjacent_territories(self):
        for point in self.adjacent_points:
            if 0 <= point[0] < len(WORLD_DATA) and 0 <= point[1] < len(WORLD_DATA):
                territory = self.game.territory_list[self.convert_2d_to_1d(point)]
                self.adjacent_territories.append(territory)
