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
        self.sprite_firstgid = None
        # Charge chaque tileset déclaré dans le .tmx
        self.load_tilesets(tmx_path.parent)
        self.entities = self.load_objects()


    #permet de découper l'affichage en fonction du nombre de tuile
    def load_tilesets(self, base_directory):
        # findall car 2 tilesets dans la carte
        for tileset in self.root.findall("tileset"):
            firstgid = int(tileset.get("firstgid"))   # 1 pour le labyrinthe, 145 pour les sprites
            tsx_path = (base_directory / tileset.get("source")).resolve()
            self.load_one_tileset(tsx_path, firstgid)
            # permet de retrouver les sprites en les marquant
            if tsx_path.stem == "General_Sprites":
                self.sprite_firstgid = firstgid

    def load_one_tileset(self, tsx_path, firstgid):
        tsx_root = ElementTree.parse(tsx_path).getroot()
        # Taille de tuile DU TILESET (8 pour le labyrinthe, 16 pour les sprites)
        tilewidth = int(tsx_root.get("tilewidth"))
        tileheight = int(tsx_root.get("tileheight"))
        spacing = int(tsx_root.get("spacing", 0))
        margin = int(tsx_root.get("margin", 0))
        columns = int(tsx_root.get("columns"))
        tilecount = int(tsx_root.get("tilecount"))

      
        image_path = (tsx_path.parent / tsx_root.find("image").get("source")).resolve()
        image = pygame.image.load(image_path).convert_alpha()

        for n in range(tilecount):
            col, row = n % columns, n // columns
            x = margin + col * (tilewidth + spacing)   # position de la tuile dans l'image
            y = margin + row * (tileheight + spacing)
            surf = image.subsurface(pygame.Rect(x, y, tilewidth, tileheight)).copy()
            
            self.tiles[firstgid + n] = pygame.transform.scale(surf, (tilewidth * utils.ZOOM, tileheight * utils.ZOOM))

    def load_objects(self):
        entities = []
        # Cherche objectgroup name="Entities" ; None si le calque n'existe pas
        group = self.root.find("objectgroup[@name='Entities']")
        if group is None:
            return entities

        for obj in group.findall("object"):
            
            gid = int(obj.get("gid")) & 0x0FFFFFFF
            w = float(obj.get("width"))
            h = float(obj.get("height"))
            x = float(obj.get("x"))
            y = float(obj.get("y")) - h      
            entities.append({
                "name": obj.get("name"),     
                "gid": gid,
                "x": x + w / 2,              
                "y": y + h / 2,
            })
        return entities

    def is_walkable(self, col, row):
        if col < 0 or col >= self.width or row < 0 or row >= self.height:
            return False
        return self.matrix[row][col] in utils.WALKABLE_TILES

    def eat_gomme(self, col, row):
        if col < 0 or col >= self.width or row < 0 or row >= self.height:
            return 0
        tile = self.matrix[row][col]
        if tile == utils.GOMME_TILE or tile == utils.SPECIAL_TILE:
            self.matrix[row][col] = utils.EMPTY_TILE
            return tile          
        return 0                 