from unicurses import *

class GameObject:
    def __init__(self, x, y, symbol = '?'):
        self.x = x
        self.y = y
        self.symbol = symbol
    def draw(self, screen):
        wmove(screen, 1+self.y,1+self.x)
        waddstr(screen, self.symbol)

class Block(GameObject):
    def __init__(self, x, y, symbol='?', isPassable=False):
        super().__init__(x, y, symbol=symbol)
        self.isPassable = isPassable
