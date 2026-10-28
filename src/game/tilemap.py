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
        self.tile_w = int(self.root.get("tilewidth"))
        self.tile_h = int(self.root.get("tileheight"))

        utils.setMapWidth(self.width)
        utils.setMapHeight(self.height)

        #récupération du CSV et création de la matrice 2D
        data_text = self.root.find(".//data").text.strip()
        flat_list = [int(v) for v in data_text.split(",") if v.strip()]

        self.matrix = [flat_list[y*self.width : (y+1)*self.width]for y in range(self.height)]
        self.tiles = {}