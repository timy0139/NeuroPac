import pygame
import debug
import utils
import sprites
from entities import Entities
from pacman import Pacman
from screen import Screen
from tilemap import TileMap
from hud import Hud

KEY_DIRECTIONS = {
    pygame.K_LEFT: "left", pygame.K_q: "left",
    pygame.K_RIGHT: "right", pygame.K_d: "right",
    pygame.K_UP: "up", pygame.K_z: "up",
    pygame.K_DOWN: "down", pygame.K_s: "down",
}
class Game:
    def __init__(self, render=True, ai_controled=False):
        self.render = render
        self.ai_controled = ai_controled
        if self.render:
            pygame.init()
            self.screen = Screen()
            self.hud = Hud()
            
        else:
            self.screen = None
            self.hud = None
            self.font = None

        self.pacman = None
        self.running = False
        self.debug = False
        self.tilemap = TileMap(utils.MAP_FILE)
        self.entities = self.create_entities()   

    def read_keyboard(self):
        keys = pygame.key.get_pressed()
        for key, direction in KEY_DIRECTIONS.items():
            if keys[key]:
                self.pacman.set_direction(direction)   
                break

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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.reset()

    def update(self, dt):
        if self.pacman is not None and not self.ai_controled:
            self.read_keyboard()
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
        score = self.pacman.score if self.pacman is not None else 0
        self.hud.draw(self.screen.get_display(), score)
        if self.debug:
            debug.draw_walkable(self.screen.get_display(), self.tilemap)
            

    def reset(self):
        self.tilemap.reset()                         
        self.entities = self.create_entities()

    def quit(self):
        pygame.quit()

    def run(self):
        self.running = True
        while self.running:
            self.update(self.screen.get_deltatime())
            if self.render:
                self.hundle_events()
                self.draw()
                self.screen.update()
        self.quit()