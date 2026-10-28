from pathlib import Path
from xml.etree import ElementTree  #parseur XML 

import pygame
import utils


class TileMap:
    def __init__(self, tmx_path):
        tmx_path = Path(tmx_path)
        tree = ElementTree.parse(tmx_path)
        self.root = tree.getroot() #racine de mon arbre (map pour carte1)

        self.width = int(self.root.get("width"))
        self.height = int(self.root.get("height"))
        self.tile_width = int(self.root.get("tilewidth"))
        self.tile_height = int(self.root.get("tileheight"))

        utils.setMapWidth(self.width)
        utils.setMapHeight(self.height)

        #récupération du CSV et création de la matrice 2D
        data_text = self.root.find(".//data").text.strip()
        flat_list = [int(v) for v in data_text.split(",") if v.strip()]

        self.matrix = [flat_list[y*self.width : (y+1)*self.width]for y in range(self.height)]
        self.tiles = {}
        self.load_tileset(tmx_path.parent)


    #permet de découper l'affichage en fonction du nombre de tuile
    def load_tileset(self, base_directory):
        tsx_source = self.root.find("tileset").get("source")
        tsx_root = ElementTree.parse(base_directory/tsx_source).getroot() #combine les 2 chemins
        spacing = int(tsx_root.get("spacing", 1))
        columns = int(tsx_root.get("columns"))
        tilecount = int(tsx_root.get("tilecount"))

        image_path = base_directory/tsx_root.find("image").get("source")
        image = pygame.image.load(image_path).convert_alpha()

        #découpage et calcule de la position des tuiles
        for tile_num in range(tilecount):
            colonne, ligne = tile_num%columns, tile_num//columns
            x, y = colonne*(self.tile_width+spacing), ligne*(self.tile_height+spacing) #calcule la position de la tuile
            rect = pygame.Rect(x, y, self.tile_width, self.tile_height)
            tile_surface = image.subsurface(rect).copy()
            self.tiles[tile_num+1] = pygame.transform.scale(tile_surface, (self.tile_width*utils.ZOOM, self.tile_height*utils.ZOOM))

