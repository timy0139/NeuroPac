import pygame
import sprites
import utils
from movable import Movable


class Pacman(Movable):
    def __init__(self, x, y, tilemap):
        super().__init__("pacman", x, y, sprites.PACMAN_FRAMES, tilemap, "left", utils.PACMAN_SPEED)

    def handle_input(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.next_direction = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.next_direction = "right"
        elif keys[pygame.K_UP] or keys[pygame.K_z]:
            self.next_direction = "up"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.next_direction = "down"

    def arrive(self):
        super().arrive()
        self.tilemap.eat_gomme(self.col, self.row) 