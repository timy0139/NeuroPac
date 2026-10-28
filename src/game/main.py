# main.py : point d'entrée du jeu
from game import Game  # importe la classe Game depuis game.py (même dossier)

if __name__ == "__main__":
    game = Game()
    game.run()