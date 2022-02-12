from kivy.app import App
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

from models import Reactor




class MainWidget(BoxLayout):
    toggle_state = BooleanProperty(False)
    product = StringProperty('')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reactors = [
            Reactor("1.1", 5000),
            Reactor("1.2", 5500),
            Reactor("1.3", 6000),
            Reactor("1.4", 6000),
        ]
    def toggle_button(self,widget):
        if widget.state == 'down':
            for reactor in self.reactors:
                if reactor.name == widget.text:
                    self.product = str(reactor.show_info())
        else:
            self.product == ''


class TheLabApp(App):
    pass


TheLabApp().run()