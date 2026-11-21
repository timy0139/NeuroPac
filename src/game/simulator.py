# environment.py : la logiquez du jeu (carte, Pac-Man, gommes, score) sans affichage 
# Game l'utilise pour jouer, et l'IA pour simuler

import sprites
from entities import Entities
from pacman import Pacman


class Simulator:
    def __init__(self, tilemap):
        self.tilemap = tilemap
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

    def update(self, dt):
        for entity in self.entities:
            entity.update(dt)