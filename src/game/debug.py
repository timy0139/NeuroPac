#permet de faire des tests in game
import pygame
import utils


def draw_walkable(surface, tilemap):
    # Taille d'une case À L'ÉCRAN (8 px * zoom)
    size = tilemap.tile_width * utils.ZOOM
    calque = pygame.Surface((size, size), pygame.SRCALPHA)   # carré semi-transparent
    for row in range(tilemap.height):
        for col in range(tilemap.width):
            if tilemap.is_walkable(col, row):
                calque.fill((0, 255, 0, 80))                 # vert = on peut marcher
            else:
                calque.fill((255, 0, 0, 80))                 # rouge = mur
            surface.blit(calque, (col * size, row * size))
    
#fait par IA        
def draw_score(surface, font):
    texte = font.render(f"SCORE : {utils.SCORE}", True, (255, 255, 255))
    # petit fond noir semi-transparent pour rester lisible sur la carte
    fond = pygame.Surface((texte.get_width() + 10, texte.get_height() + 6), pygame.SRCALPHA)
    fond.fill((0, 0, 0, 160))
    surface.blit(fond, (5, 5))
    surface.blit(texte, (10, 8))