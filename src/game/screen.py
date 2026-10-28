# screen.py : gestion de la fenêtre, de l'horloge et du delta time
import pygame
import utils


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT))
        pygame.display.set_caption(utils.WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.framerate = utils.FPS
        self.deltatime = 0

    #évite la superposition d'image
    def clear(self):
        self.display.fill(utils.BACKGROUND_COLOR)

    #rafraichit la fenêtre
    def update(self):
        pygame.display.update()
        self.deltatime = self.clock.tick(utils.FPS)

    def get_deltatime(self):
        return self.deltatime

    def get_size(self):
        return self.display.get_size()

    def get_display(self):
        return self.display