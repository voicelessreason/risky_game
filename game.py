import pygame
import sys
from world import World
from kingdom import Kingdom
from config import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True

    def new(self):
        self.kingdom_colors = [(RED, 'red'), (BLUE, 'blue'), (GREEN, 'green')]
        self.playing = True
        self.world = World(self, WORLD_DATA)
        self.clock = pygame.time.Clock()
        self.turn = 1
        self.tile_list = []
        self.territory_list = []
        self.kingdom_list = []

        # for color in self.kingdom_colors:
        #     self.kingdom_list.append(Kingdom(self, color[0], color[1]))

        self.kingdom_list.append(Kingdom(self, RED, 'red'))

    def main(self):
        while self.playing:
            self.events()
            self.take_turn()
            self.draw()

    def events(self):
        # check that we haven't quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def take_turn(self):
        self.world.update()
        for terr in self.territory_list:
            terr.get_adjacent_territories()

        for current_kingdom in self.kingdom_list:
            # Update UI:
            # Outline the kingdom who's turn it is
            # Outline the territories they could attack
            # Conduct Player Actions
            # Calculate troop income and have player assign reinforcements for their kingdom
            # Calculate the number of attacks they are allowed and for each allowed attack,
            # have the player select a single territory from within their attackable territories
            # carry out combat...update the troop totals in both territories and update color as necessary
            print(current_kingdom.text_color)


    def draw(self):
        self.world.draw()
        for kingdom in self.kingdom_list:
            kingdom.update_territories()
            kingdom.outline_kingdom()
        pygame.display.update()
        self.clock.tick(FPS)

g = Game()
g.new()
while g.running:
    g.main()
pygame.quit()
sys.exit()
