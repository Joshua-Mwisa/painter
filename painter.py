from kivy.app import App
from random import random
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line, Ellipse

class Avdoodler (Widget):
    def on_touch_down (self, touch):
        with self.canvas:
            Color (random (), random (), random ())
            d= 10
            Ellipse(pos=(touch.x-5, touch.y-5), size=(d,d))
            touch.ud ['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move (self, touch):
        touch.ud ['line'].points += (touch.x, touch.y)

class av (App):
    
    def build (self):
        return Avdoodler()

if __name__=='__main__':
    av().run()
