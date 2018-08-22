from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, VariableListProperty
import random
from kivy.clock import Clock


class circle1(Widget):
    pass

class inner_circle(Widget):
    pass

class circle2(Widget):
    pass

class lines(Widget):
    pass

class arc_reacter(Widget):
    circlearc1 = ObjectProperty(None)
    circlearc2 = ObjectProperty(None)
    line1 = ObjectProperty(None)
    color_code = VariableListProperty(None)

    def update(self, color_code):
        self.color_code = random.choice([(.811, .854, .921, 1), (.933, .968, .964, 1)])

class arc(App):
    def build(self):
        arcs = arc_reacter()
        Clock.schedule_interval(arcs.update, 1.0/5.0)
        return arcs

if __name__ == '__main__':
    arc().run()
