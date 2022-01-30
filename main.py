from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from models import Reactor


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reactors = [
            Reactor




        ]




class TheLabApp(App):
    pass


TheLabApp().run()