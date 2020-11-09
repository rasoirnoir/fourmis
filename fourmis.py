#!/usr/bin/env python

import pygame, argparse, sys

'''

    Implémentation en python de la fourmis de Langton
    Règles du jeu :
     - Si la fourmis se tient sur une case noire, elle tourne à gauche
     - Si elle se trouve sur une case blanche, elle tourne à droite
     - La case sur laquelle elle se tenait change de couleur

'''

#Définition des constantes
FILE = ""
FPS = 30
VERSION = "0.1"
DEBUG = False

def version():
    print("fourmis.py version {} by CactusPin".format(VERSION))

def main():
    print('Lancement de la simu.')
    version()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''La fourmis de Langton. 
        Automate cellulaire célèbre implémenté en python
    ''')

    parser.add_argument("file", help="The file containing the game board as a matrix.")
    parser.add_argument("-v", "--version", help="prints the version and exits.", action="store_true")
    parser.add_argument("-s", "--speed", help="The speed of the game in frames per second (fps)")

    args = parser.parse_args()

    if args.version:
        version()
        sys.exit(0)
    if args.speed:
        FPS = int(args.speed)

    FILE = args.file
    main()

