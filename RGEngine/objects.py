from unicurses import *

class GameObject:
    """Main game object class"""
    def __init__(self, x, y, symbol = '?'):
        self.x = x
        self.y = y
        self.symbol = symbol
    def draw(self, screen):
        """Drawing game object"""
        wmove(screen, 1+self.y,1+self.x)
        waddstr(screen, self.symbol)

class Block(GameObject):
    """Block is a simple game object like wall or grass that can be passable or not"""
    def __init__(self, x, y, symbol='?', isPassable=False):
        super().__init__(x, y, symbol=symbol)
        self.isPassable = isPassable
