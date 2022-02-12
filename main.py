from kivy.app import App
from kivy.properties import BooleanProperty, StringProperty, ObjectProperty
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
        self.reactor_now.product = self.product
        self.state = False

    def unload_reactor(self):
        self.reactor_now.product = ''
        self.product = str(self.reactor_now.show_info())
        self.state = False

    def show_info(self):
        self.ids.label_text.text = str(self.reactor_now.show_info())
        self.state = False

    def spinner_clicked(self,widget):
        self.product = widget.text




    production_dict = {
        'name' : {
        'ПД-100Н':'',
        'ИН-200М':'',
        'Х-400':'',
        'Х-230':'',
        'ПА-600':'',
        'ПА-600Н':'',
        'БР-280':'',
    }
    }




class TheLabApp(App):
    pass


TheLabApp().run()