#!/usr/bin/env python

import argparse, sys, os.path
import fourmis

'''

    Implémentation en python de la fourmis de Langton
    Règles du jeu :
     - Si la fourmis se tient sur une case noire, elle tourne à gauche
     - Si elle se trouve sur une case blanche, elle tourne à droite
     - La case sur laquelle elle se tenait change de couleur

'''

'''
TODO: Définir la position de la fourmis. Elle sera représentée par un 2 dans la matrice.
        - Pour l'instant tout le board sera update à chaque itération. A terme, il serai plus judicieux de 
            ne mettre à jour que la position de la fourmis et la case qu'elle viens de quitter
'''

#Définition des constantes
FILE = ""
FPS = 30
VERSION = "0.1"
DEBUG = False

def version():
    print("fourmis.py version {} by CactusPin".format(VERSION))

def main():
    version()
    print('Lancement de la simu.')
    fourmis.startSimu(parseFile(), FPS)

def parser():
    parser = argparse.ArgumentParser(description='''La fourmis de Langton. 
        Automate cellulaire célèbre implémenté en python
    ''')

    parser.add_argument("file", help="The file containing the game board as a matrix.")
    parser.add_argument("-v", "--version", help="prints the version and exits.", action="store_true")
    parser.add_argument("-s", "--speed", help="The speed of the game in frames per second (fps)")

    return parser.parse_args()

def parseFile():
    # returns a matrix from the file
    matrix = []
    if os.path.isfile(FILE):
        with open(FILE) as f:
            content = f.readlines()
        for line in content:
            row = list(line.strip("\n"))
            matrix.append(row)
    return matrix
        




if __name__ == '__main__':
    
    args = parser()

    if args.version:
        version()
        sys.exit(0)
    if args.speed:
        FPS = int(args.speed)

    FILE = args.file
    main()

