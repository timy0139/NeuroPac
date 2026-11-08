import pygame
import debug
import utils
import sprites
from entities import Entities
from pacman import Pacman
from screen import Screen
from tilemap import TileMap


class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.running = False
        self.debug = False
        self.pacman = None
        self.tilemap = TileMap(utils.MAP_FILE)
        self.entities = self.create_entities()   

    def create_entities(self):
        entities = []
        for obj in self.tilemap.entities:
            name = obj["name"]
            if name == "pacman":
                self.pacman = Pacman(obj["x"], obj["y"], self.tilemap)
                entities.append(self.pacman)
                continue
            elif name in sprites.GHOST_ROWS:
                frames = sprites.ghost_frames(name)
            else:
                continue                      
            entities.append(Entities(name, obj["x"], obj["y"], frames, self.tilemap))
        return entities

    def hundle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
                # activer/désactiver le mode debug
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.debug = not self.debug

    def update(self, dt):
        if self.pacman is not None:
            self.pacman.handle_input(pygame.key.get_pressed())
        for entity in self.entities:
            entity.update(dt) 

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
        for entity in self.entities:
            entity.draw(self.screen.get_display())
        if self.debug:
            debug.draw_walkable(self.screen.get_display(), self.tilemap)

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