# général_prites = 14 colonnes
COLONNES = 14

def idex(row, col):
    return row * COLONNES + col

#pacman=>lignes 0 droite, 1 gauche, 2 hau, 3 bas
#  0 bouche ouverte,1 mi-ouverte, 2 fermée
def pac(row):
    #rotation d'animation
    return [idex(row, 2), idex(row, 1), idex(row, 0), idex(row, 1)]

PACMAN_FRAMES = {"right": pac(0), "left": pac(1), "up": pac(2), "down": pac(3)}


GHOST_ROWS = {"blinky": 4, "pinky": 5, "inky": 6, "clyde": 7}   
GHOST_COL = {"right": 0, "left": 2, "up": 4, "down": 6} # 1ère colonne de chaque direction

def ghost_frames(name):
    row = GHOST_ROWS[name]

    frames_du_fantome = {}
    # 2 frames par direction
    for direction, colonne in GHOST_COL.items():
        # Pour chaque direction, on calcule les 2 images d'animation
        image1 = idex(row, colonne)
        image2 = idex(row, colonne + 1)
        
        frames_du_fantome[direction] = [image1, image2]
    return frames_du_fantome

#états des fantômes
FRIGHTENED = [idex(4, 8), idex(4, 9)]        
FRIGHTENED_FLASH = [idex(4, 10), idex(4, 11)] 
EYES = {"right": idex(5, 8), "left": idex(5, 9), "up": idex(5, 10), "down": idex(5, 11)}