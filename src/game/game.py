import pygame
from screen import Screen


class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.running = False

    def hundle_events(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        self.screen.clear()

    def quit(self):
        pygame.quit()

    def run(self):
        self.running = True
        if self.running:
            self.hundle_events()
            self.update(self.screen.get_deltatime())
            self.draw()
            self.screen.update()
        self.quit()