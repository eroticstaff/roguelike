from .objects import *

"""File where all game objects contain"""

class Wall(Block):
    """Simple '#" wall object"""
    def __init__(self, x, y):
        self.symbol = '#'
        super().__init__(x, y, symbol=self.symbol)


class Grass(Block):
    """Simple '.' grass object"""
    def __init__(self, x, y):
        self.symbol = '.'
        super().__init__(x, y, symbol=self.symbol, isPassable=True)
