# hud.py : affichage des informations de jeu (score...) sous le labyrinthe
import pygame
import utils


class Hud:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface, score):
        text = self.font.render(f"SCORE  {score:05d}", True, (255, 255, 255))
        y = utils.MAP_PIXEL_HEIGHT + (utils.HUD_HEIGHT - text.get_height()) // 2
        surface.blit(text, (16, y))