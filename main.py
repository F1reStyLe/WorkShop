from kivy.app import App
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

from models import Reactor




class MainWidget(BoxLayout):
    state = BooleanProperty(False)
    product = StringProperty('')
    reactor_now = object
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
            self.state = True
            for reactor in self.reactors:
                if reactor.name == widget.text:
                    self.reactor_now = reactor
                    self.product = str(reactor.show_info())

    def load_reactor(self):
        self.reactor_now.product = 'PD-100'
        self.product = str(self.reactor_now.show_info())
        self.state = False






class TheLabApp(App):
    pass


TheLabApp().run()