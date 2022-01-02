import pygame
from config import *
from territory import Territory


class World:
    def __init__(self, game, data):
        self.game = game
        self.data = data

    def update(self):
        row_cnt = 0
        for row in self.data:
            col_cnt = 0
            for tile in row:
                img = pygame.Surface((TILE_SIZE, TILE_SIZE))
                img_rect = img.get_rect()
                img_rect.x = (col_cnt * TILE_SIZE) + TILE_SIZE
                img_rect.y = (row_cnt * TILE_SIZE) + TILE_SIZE
                if tile == 1:
                    img.fill(BLUE)
                    tile = (img, img_rect)
                    self.game.tile_list.append(tile)
                    self.game.territory_list.append(Territory(self.game, col_cnt, row_cnt, BLUE))
                if tile == 2:
                    img.fill(GREEN)
                    tile = (img, img_rect)
                    self.game.tile_list.append(tile)
                    self.game.territory_list.append(Territory(self.game, col_cnt, row_cnt, GREEN))
                if tile == 3:
                    img.fill(RED)
                    tile = (img, img_rect)
                    self.game.tile_list.append(tile)
                    self.game.territory_list.append(Territory(self.game, col_cnt, row_cnt, RED))
                if tile == 0:
                    img.fill(BACKGROUND_COLOR)
                    tile = (img, img_rect)
                    self.game.tile_list.append(tile)
                    self.game.territory_list.append(Territory(self.game, col_cnt, row_cnt, BACKGROUND_COLOR))
                col_cnt += 1
            row_cnt += 1

    def draw_grid(self):
        width = SCREEN_WIDTH - TILE_SIZE
        lines = width // TILE_SIZE
        for x in range(0, lines):
            # down
            pygame.draw.line(self.game.screen, WHITE,
                             ((TILE_SIZE * x) + TILE_SIZE, TILE_SIZE),
                             ((TILE_SIZE * x) + TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
            # across
            pygame.draw.line(self.game.screen, WHITE,
                             (TILE_SIZE, (TILE_SIZE * x) + TILE_SIZE),
                             (SCREEN_WIDTH - TILE_SIZE, (TILE_SIZE * x) + TILE_SIZE))

    def draw(self):
        for tile in self.game.tile_list:
            self.game.screen.blit(tile[0], tile[1])
        self.draw_grid()
