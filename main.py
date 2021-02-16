from RGEngine.renderer import GameScreen
from RGEngine.game_objects import *
from RGEngine.world import *
from RGEngine.player import Player

stdscr = initscr()
start_color()
noecho()
curs_set(False)

game_screen = GameScreen(stdscr)
game_screen.render()

world_map = []

for i in range(15):
    for j in range(15):
        if i == 5 and j == 5:
            world_map.append(Wall(i, j))
        else:
            world_map.append(Grass(i, j))

world = World(world_map)
world.draw(game_screen.screen)
player = Player(game_screen.screen, 2, 2, world)
game_screen.render()

while True:
    key = getch()
    if key == 97:  # A
        player.move(player.x - 1, player.y)
    elif key == 119:  # W
        player.move(player.x, player.y - 1)
    elif key == 100:  # D
        player.move(player.x + 1, player.y)
    elif key == 115:  # S
        player.move(player.x, player.y + 1)
    game_screen.render()

game_screen.render()
getch()
endwin()
