from unicurses import *

class Player:
    """Player class"""
    def __init__(self,screen, x, y, world):
        self.x = x
        self.y = y
        self.screen = screen
        self.symbol = '@'
        self.world = world
        wmove(screen, y, x)
        waddstr(screen, self.symbol)

    def move(self, x, y):
        """Moving to x and y"""
        next_world_object = self.world.find_block(x-1, y-1)
        if next_world_object != None and next_world_object.isPassable:
            past_world_object = self.world.find_block(self.x-1, self.y-1)
            symbol = '?'
            if past_world_object != None:
                symbol = past_world_object.symbol
            wmove(self.screen, self.y, self.x)
            waddstr(self.screen, symbol)
            wmove(self.screen, y, x)
            waddstr(self.screen, self.symbol)
            self.x = x
            self.y = y