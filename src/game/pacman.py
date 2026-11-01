import pygame
import sprites
import utils
from entities import Entities

# Vecteur (dx, dy) pour chaque direction
DIRS = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}


class Pacman(Entities):
    def __init__(self, x, y, tilemap):
        super().__init__("pacman", x, y, sprites.PACMAN_FRAMES, tilemap, "left")
        self.speed = utils.PACMAN_SPEED     
        self.moving = False                 

    def handle_input(self, keys):
        self.moving = True
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.direction = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = "right"
        elif keys[pygame.K_UP] or keys[pygame.K_z]:
            self.direction = "up"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = "down"
        else:
            self.moving = False             

    def update(self, dt):
        if not self.moving:
            return
        dx, dy = DIRS[self.direction]
        dist = self.speed * dt / 1000
        self.x += dx * dist
        self.y += dy * dist
        super().update(dt)