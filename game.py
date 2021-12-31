import pygame
import sys
from world import World
from config import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True

    def new(self):
        self.playing = True
        self.world = World(self, WORLD_DATA)
        self.clock = pygame.time.Clock()
        self.turn = 1


    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        # check that we haven't quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.world.update()

    def draw(self):
        self.world.draw()
        pygame.display.update()
        self.clock.tick(FPS)


g = Game()
g.new()
while g.running:
    g.main()
pygame.quit()
sys.exit()
