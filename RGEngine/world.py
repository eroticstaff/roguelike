class World:
    def __init__(self, world):
        self.world = world
    def draw(self,screen):
        for game_object in self.world:
            game_object.draw(screen)
    def find_block(self, x, y):
        for game_object in self.world:
            if game_object.x == x and game_object.y == y:
                return game_object