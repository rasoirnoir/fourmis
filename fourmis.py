import time


def fourmisModule():
    """Confirme le chargement du module Fourmis"""
    print("Fourmis module loaded")


class Direction:
    HAUT, DROITE, BAS, GAUCHE = range(0, 4)


class Fourmis:
    """Class Fourmis qui définie sa position et son orientation sur le board
    """

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.ite = 0
        self.previousPos = [-1, -1]

    def deplacement(self, couleur):
        """Déplace la fourmis sur le board d'après les règles du jeu

        Args:
            couleur (integer): la couleur de la case de départ de la fourmis
        """
        # self.previousPos = self.position
        self.previousPos[0] = self.position[0]
        self.previousPos[1] = self.position[1]
        if couleur == 0:  # case noire
            # on déplace la fourmis d'une case à gauche et on change son orientation
            # on tourne à gauche
            if self.direction == Direction.HAUT:
                self.position[1] -= 1
            if self.direction == Direction.DROITE:
                self.position[0] -= 1
            if self.direction == Direction.BAS:
                self.position[1] += 1
            if self.direction == Direction.GAUCHE:
                self.position[0] += 1

            self.direction = (self.direction - 1) % 4

        if couleur == 1:  # case blanche
            # On déplace la fourmis d'une case vers la droite
            # on tourne à droite
            if self.direction == Direction.HAUT:
                self.position[1] += 1
            if self.direction == Direction.DROITE:
                self.position[0] += 1
            if self.direction == Direction.BAS:
                self.position[1] -= 1
            if self.direction == Direction.GAUCHE:
                self.position[0] -= 1

            self.direction = (self.direction + 1) % 4

    def toString(self):
        """Retourne une version affichable de la fourmis

        Returns:
            [string]: affichage de la fourmis
        """
        pos = "({},{})".format(self.position[0], self.position[1])
        dir = ""
        if self.direction == Direction.HAUT:
            dir = "\u2B06"
        if self.direction == Direction.DROITE:
            dir = "\u27A1"
        if self.direction == Direction.BAS:
            dir = "\u2B07"
        if self.direction == Direction.GAUCHE:
            dir = "\u2B05"
        ite = "Etat de la fourmis à l'itération {}".format(self.ite)
        return ite + "\n" + pos + " " + dir

    def hasMoved(self):
        print("previous pos : {}, current pos : {}".format(
            self.previousPos, self.position))
        # if self.previousPos[0] == self.position[0] and self.previousPos[1] == self.position[1]:
        if self.previousPos == self.position:
            return False
        return True


def startSimu(matrix, fps):
    """Initialise le Board

    Args:
        matrix (Array): une image du board
        fps (integer): le nombre d'images par secondes affichées
    """
    position = [(int(len(matrix[0]) / 2)) - 1, (int(len(matrix) / 2)) - 1
                ]  # position initiale de la fourmis : le centre du board
    direction = Direction.HAUT
    fourmis = Fourmis(position, direction)
    # printBoard(matrix, fourmis)
    finished = False
    tmpMatrix = matrix
    nextMatrix = []
    while not finished:
        printBoard(tmpMatrix, fourmis)
        nextMatrix = nextIte(tmpMatrix, fourmis)
        if not fourmis.hasMoved():
            finished = True
        tmpMatrix = nextMatrix
        time.sleep(1 / fps)


def nextIte(matrix, fourmis):
    """Calcule la matrice suivante d'apres les règles du jeu

    Args:
        matrix (array): la représentation du board, array en 2 dimensions
        fourmis (Fourmis): la fourmis (contenant sa position et sa direction)
    """
    # case noire : tourne à gauche
    # case blanche : tourne à droite
    # la case précédente change de couleur

    originalPosition = fourmis.position
    # couleur = matrix[originalPosition[0]][originalPosition[1]]
    couleur = couleurCell(matrix, originalPosition)
    fourmis.deplacement(couleur)
    if fourmis.position[0] < 0:
        fourmis.position[0] = 0
    if fourmis.position[1] < 0:
        fourmis.position[1] = 0
    if fourmis.position[0] > len(matrix[0]) - 1:
        fourmis.position[0] = len(matrix[0]) - 1
    if fourmis.position[1] > len(matrix) - 1:
        fourmis.position[1] = len(matrix) - 1
    # matrix[originalPosition[0]][originalPosition[1]] = 1 if couleur == 0 else 0
    matrix[fourmis.previousPos[0]][fourmis.previousPos[1]
                                   ] = 1 if couleur == 0 else 0
    fourmis.ite += 1

    return matrix


def printBoard(matrix, fourmis):
    """print the current state of the board matrix

    Args:
        matrix (array): bidimensional array (matrix) representing the board matrix
        ite (int): the current iteration number
    """
    print(fourmis.toString())
    print(couleurCell(matrix, fourmis.position))
    # for row in matrix:
    #     rowString = ""
    #     for cell in row:
    #         rowString += "{} ".format(cell)
    #     print(rowString)
    for i in range(len(matrix)):
        rowString = ""
        for j in range(len(matrix[i])):
            if i == fourmis.position[0] and j == fourmis.position[1]:
                rowString += "{} ".format("2")
            else:
                rowString += "{} ".format(matrix[i][j])
        print(rowString)


def couleurCell(matrix, position):
    return matrix[position[0]][position[1]]
