from config import *
import pygame


class Kingdom:
    def __init__(self, game, rgb_color, text_color):
        self.game = game
        self.territories = self.get_territories()
        self.attackable_territories = []
        self.gold = 0
        self.total_troops = 0
        self.rgb_color = rgb_color
        self.text_color = text_color

    def get_territories(self):
        owned_territories = []
        for territory in self.game.territory_list:
            if territory.color == self.rgb_color:
                owned_territories.append(territory)
        return owned_territories

    def update_territories(self):
        self.territories = self.get_territories()
        for territory in self.territories:
            for adj_territory in territory.adjacent_territories:
                if adj_territory.color != self.rgb_color:
                    self.attackable_territories.append(adj_territory)

    @staticmethod
    def convert_2d_to_1d(index_tuple):
        return index_tuple[1] * 8 + index_tuple[0]

    def outline_kingdom(self):
        # for territory in self.territories:
        #     tile = self.game.tile_list[self.convert_2d_to_1d(territory.index)]
        #     pygame.draw.rect(self.game.screen, BLACK, tile[1], 5)

        for territory in self.attackable_territories:
            tile = self.game.tile_list[self.convert_2d_to_1d(territory.index)]
            pygame.draw.rect(self.game.screen, YELLOW, tile[1], 3)
