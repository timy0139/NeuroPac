import pygame
import sprites
import utils
from movable import Movable


class Pacman(Movable):
    def __init__(self, x, y, tilemap):
        super().__init__("pacman", x, y, sprites.PACMAN_FRAMES, tilemap, "left", utils.PACMAN_SPEED)
        self.score = 0 

    def set_direction(self, direction):
        self.next_direction = direction

    def arrive(self):
        super().arrive()
        tile = self.tilemap.eat_gomme(self.col, self.row) #change tile en tile vide si gomme
        #update score

        if tile == utils.GOMME_TILE:
            self.score += 10
        if tile == utils.SPECIAL_TILE:
            self.score += 50

