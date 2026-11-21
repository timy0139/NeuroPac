# environment.py : la logiquez du jeu (carte, Pac-Man, gommes, score) sans affichage 
# Game l'utilise pour jouer, et l'IA pour simuler

import sprites
from entities import Entities
from pacman import Pacman


class Simulator:
    def __init__(self, tilemap, max_seconds = None):
        self.tilemap = tilemap
        self.max_miliseconds = None if max_seconds is None else max_seconds * 1000
        self.ms_passés = 0.0
        self.finished = False
        self.won = False
        self.pacman = None
        self.entities = []
        self.reset()

    def create_entities(self):
        entities = []
        for objet in self.tilemap.entities:
            name = objet["name"]
            if name == "pacman":
                self.pacman = Pacman(objet["x"], objet["y"], self.tilemap)
                entities.append(self.pacman)
                continue
            elif name in sprites.GHOST_ROWS:
                frames = sprites.ghost_frames(name)
            else:
                continue
            entities.append(Entities(name, objet["x"], objet["y"], frames, self.tilemap))
        return entities


    def reset(self):
        self.tilemap.reset()
        self.entities = self.create_entities()
        self.ms_passés = 0.0
        self.finished = False
        self.won = False

    def check_finished(self):
        if self.tilemap.gommes_left == 0:
            self.won = True
            self.done = True
        elif self.max_miliseconds is not None and self.ms_passés >= self.max_miliseconds:
            self.done = True

    def update(self, dt):
        if self.finished:
            return
        for entity in self.entities:
            entity.update(dt)
        self.ms_passés += dt
        self.check_finished()