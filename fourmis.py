
def fourmisModule():
    """Confirme le chargement du module Fourmis"""
    print("Fourmis module loaded")

class Direction:
    HAUT, BAS, GAUCHE, DROITE = range(1,5)

def startSimu(matrix, fps):
    """Initialise le Board

    Args:
        matrix (Array): une image du board
        fps (integer): le nombre d'images par secondes affichées 
    """
    position = [int(len(matrix[0]) / 2), int(len(matrix) / 2)] #position initiale de la fourmis : le centre du board
    direction = Direction.HAUT
    nbIte = 0
    nextIte(matrix, position, direction)

def nextIte(matrix, position, direction):
    """Calcule la matrice suivante d'apres les règles du jeu

    Args:
        matrix (array): la représentation du board, array en 2 dimensions
        position (array): coordonnées de la fourmis dans le board
        direction (Direction): La direction dans laquelle regarde la fourmis
    """
    # case noire : tourne à gauche
    # case blanche : tourne à droite
    # la case précédente change de couleur

    couleur = matrix[position[0]][position[1]]
    
