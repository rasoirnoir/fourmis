#!/usr/bin/env python

import argparse
import sys
import os.path
import fourmis
from signal import signal, SIGINT
from sys import exit

'''

    Implémentation en python de la fourmis de Langton
    Règles du jeu :
     - Si la fourmis se tient sur une case noire, elle tourne à gauche
     - Si elle se trouve sur une case blanche, elle tourne à droite
     - La case sur laquelle elle se tenait change de couleur

'''


# Définition des constantes
FILE = ""
FPS = 10
VERSION = "0.1"
DEBUG = False


def version():
    print("fourmis.py version {} by CactusPin".format(VERSION))


def main():
    fourmis.startSimu(parseFile(), FPS)


def parser():
    parser = argparse.ArgumentParser(description='''La fourmis de Langton. 
        Automate cellulaire célèbre implémenté en python
    ''')

    parser.add_argument(
        "file", help="The file containing the game board as a matrix.", nargs='?')
    parser.add_argument(
        "-v", "--version", help="prints the version and exits.", action="store_true")
    parser.add_argument(
        "-s", "--speed", help="The speed of the game in frames per second (fps)")

    return parser.parse_args()


def parseFile():
    # returns a matrix from the file
    matrix = []
    if os.path.isfile(FILE):
        with open(FILE) as f:
            content = f.readlines()
        for line in content:
            row = list(line.strip("\n"))
            for i in range(0, len(row)):
                row[i] = int(row[i])
            matrix.append(row)
    return matrix


def handler(signal_received, frame):
    # Handle any cleanup here
    print('CTRL-C detected. Exiting...')
    exit(0)


if __name__ == '__main__':

    signal(SIGINT, handler)

    args = parser()

    if args.version:
        version()
        sys.exit(0)
    if args.speed:
        FPS = int(args.speed)
    FILE = args.file
    if not FILE:
        print("No file specified. Exiting...")
        exit(1)
    main()
