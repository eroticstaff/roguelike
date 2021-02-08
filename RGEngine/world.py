class World:
    """World class"""
    def __init__(self, world):
        self.world = world
    def draw(self,screen):
        """Drawing world on screen"""
        for game_object in self.world:
            game_object.draw(screen)
    def find_block(self, x, y):
        """Find game object on exact x and t. Needed for collisions and inspecting"""
        for game_object in self.world:
            if game_object.x == x and game_object.y == y:
                return game_object