import pygame
import utils
from screen import Screen
from tilemap import TileMap


class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.running = False
        self.tilemap = TileMap(utils.MAP_FILE)

    def hundle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False


    def update(self, dt):
        pass

    def draw(self):
        self.screen.clear()

        for y in range(self.tilemap.height):
            for x in range(self.tilemap.width):
                tile_id = self.tilemap.matrix[y][x]
                if tile_id != 0:
                    tile_image = self.tilemap.tiles.get(tile_id)
                    if tile_image:
                        pos_x = x* self.tilemap.tile_width*utils.ZOOM
                        pos_y = y*self.tilemap.tile_height*utils.ZOOM
                        self.screen.get_display().blit(tile_image,(pos_x, pos_y))


    def quit(self):
        pygame.quit()

    def run(self):
        self.running = True
        while self.running:
            self.hundle_events()
            self.update(self.screen.get_deltatime())
            self.draw()
            self.screen.update()
        self.quit()