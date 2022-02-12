

class Reactor:
    name = ''
    product = '111'
    volume = 0
    empty = True

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def show_info(self):
        return self.name, self.product, self.volume

    def load(self, product):
        self.product = product

