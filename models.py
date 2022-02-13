

class Reactor:
    name = ''
    product = ''
    volume = 0
    empty = True

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def show_info(self):
        return (f'Номер реактора: {self.name} \n' 
               f'Загружено: {self.product} \n'
               f'Объем: {self.volume}')

    def load(self, product):
        self.product = product

