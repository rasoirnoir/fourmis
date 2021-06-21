import kivy.graphics as G
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.clock import Clock
# from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.label import Label
from random import *

from kivy.config import Config
import fourmis
import kivy
kivy.require('2.0.0')


class Cell(Widget):
    def __init__(self, **kwargs):
        print("Dessin d'une Cellule")
        super(Cell, self).__init__(**kwargs)
        self.bind(size=self.draw)
        self.draw()

    def draw(self, *args):
        self.canvas.clear
        with self.canvas:
            G.Color(random(), random(), random())
            G.Rectangle(pos=self.pos, size=self.size)
            # self.add_widget(Label(text="label", size=self.size, pos=self.pos))


class Board(RelativeLayout):
    def __init__(self, board, **kwargs):
        print("Tableau d'arguments de Board : {}".format(kwargs))
        self.board = board
        super(Board, self).__init__(**kwargs)
        self.size = (Config.get('graphics', 'width'),
                     Config.get('graphics', 'height'))
        # self.bind(pos=self.update_canvas)
        # self.bind(size=self.update_canvas)
        # self.update_canvas()

        # fourmis.startSimu(board)

    def init_canvas(self):
        print("Init canvas")
        self.canvas.clear()
        with self.canvas:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if(self.board[i][j] == 0):
                        G.Color(0, 0, 0)
                    else:
                        G.Color(1, 1, 1)
                    G.Color(1, 0, 0)
                    newCell = Cell()
                    newCell.size = (
                        self.size[0] /
                        len(self.board), self.size[1] / len(self.board[j]))
                    newCell.pos = (
                        (i * newCell.size[0]), (j * newCell.size[1]))
                    self.add_widget(newCell)

                    print("Rectangle size: ({}, {}), position: ({}, {})".format(
                        self.size[0] / len(self.board), self.size[1] / len(self.board[j]), i, j))

    def update_canvas(self, *args):
        print("Canvas update.")

        for cell in self.children:
            cell.size = (
                self.size[0] /
                len(self.board), self.size[1] / len(self.board))
        # définir une variable de classe Fourmis


class FourmisApp(App):
    def build(self):
        print("board : {}, fps : {}".format(self.board, self.fps))
        from kivy.config import Config
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '800')
        Config.write()
        theBoard = Board(self.board)
        theBoard.init_canvas()
        Clock.schedule_interval(theBoard.update_canvas, 1.0 / self.fps)
        return theBoard
