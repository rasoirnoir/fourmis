import kivy.graphics as G
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
import fourmis
import kivy
kivy.require('2.0.0')


class Board(Widget):
    def __init__(self, board, **kwargs):
        print("Tableau d'arguments de Board : {}".format(kwargs))
        super(Board, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()
        fourmis.startSimu(board)

    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            G.Rectangle(pos=(10, 10), size=(500, 500))
            Label(text='Salut', color='white', pos=(20, 10), size=self.size)


class FourmisApp(App):
    def build(self):
        print("board : {}, fps : {}".format(self.board, self.fps))
        theBoard = Board(self.board)
        return theBoard
