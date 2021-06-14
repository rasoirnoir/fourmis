from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.graphics import *
import kivy.graphics as G


class Board(Widget):
    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()

    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            G.Rectangle(pos=(10, 10), size=(500, 500))


class FourmisApp(App):
    def build(self):
        return Board()
