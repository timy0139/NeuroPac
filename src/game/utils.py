# utils.py : constantes globales du projet NeuroPac
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
ASSETS_DIR = ROOT_DIR / "assets"
MAP_FILE = ASSETS_DIR / "map" / "Carte1.tmx"

# Constantes d'affichage
WINDOW_TITLE = "NeuroPac"
ZOOM = 3
TILE_SIZE = 8
SCREEN_WIDTH = 28 * TILE_SIZE * ZOOM
SCREEN_HEIGHT = 31 * TILE_SIZE * ZOOM
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60                    
MAP_WIDTH = 0
MAP_HEIGHT = 0

def setMapWidth(width):
    global MAP_WIDTH
    MAP_WIDTH = width

def setMapHeight(height):
    global MAP_HEIGHT
    MAP_HEIGHT = height

def setTileSize(size):
    global TILE_SIZE
    TILE_SIZE = size