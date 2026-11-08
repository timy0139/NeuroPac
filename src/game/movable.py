# déplacement case par case
import utils
from entities import Entities


DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}


class Movable(Entities):
    def __init__(self, name, x, y, frames, tilemap, direction="left", speed=utils.PACMAN_SPEED):
        super().__init__(name, x, y, frames, tilemap, direction)
        self.tile = tilemap.tile_width      
        self.col = int(x // self.tile)      
        self.row = int(y // self.tile)
        self.speed = speed                 
        self.next_direction = direction    
        self.target = None                 
        self.progress = 0.0                 
        self.moving = True                       

    #Lorsqu'au centre d'une case prend la direction demandée
    def start_move(self):
        self.direction = self.next_direction
        dx, dy = DIRECTIONS[self.direction]
        self.target = (self.col + dx, self.row + dy)  
        self.progress = 0.0

    def arrive(self):
        self.col, self.row = self.target
        self.target = None
        self.progress = 0.0

    def update_position(self):
        centrex = self.col * self.tile + self.tile / 2
        centrey = self.row * self.tile + self.tile / 2
        if self.target is not None:
            dx, dy = DIRECTIONS[self.direction]
            centrex += dx * self.progress
            centrey += dy * self.progress
        self.x, self.y = centrex, centrey

    def update(self, dt):
        distance = self.speed * dt / 1000
        while distance > 0:
            if self.target is None:
                self.start_move()           
            step = min(distance, self.tile - self.progress)
            self.progress += step
            distance -= step
            if self.progress >= self.tile:
                self.arrive()              
        self.update_position()
        super().update(dt)                  
      