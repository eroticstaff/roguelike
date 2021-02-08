from .objects import *


class Wall(Block):
    def __init__(self, x, y):
        self.symbol = '#'
        super().__init__(x, y, symbol=self.symbol)


class Grass(Block):
    def __init__(self, x, y):
        self.symbol = '.'
        super().__init__(x, y, symbol=self.symbol, isPassable=True)
