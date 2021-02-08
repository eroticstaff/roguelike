from unicurses import *
class GameScreen:
    def __init__(self, stdscr, tool_window_size = 30, info_window_size = 10):
        self.max_y, self.max_x = getmaxyx(stdscr)
        self.tool_panel_size = tool_window_size
        self.info_panel_size = info_window_size

        self.main_window = newwin(self.max_y, self.max_x, 0, 0)
        box(self.main_window)
        main_panel = new_panel(self.main_window)

        self.screen = newwin(self.max_y - self.info_panel_size, self.max_x - self.tool_panel_size, 0, 0)
        box(self.screen)
        screen_panel = new_panel(self.screen)

        self.tool_window = newwin(self.max_y, self.tool_panel_size, 0, self.max_x - self.tool_panel_size)
        box(self.tool_window)
        tool_panel = new_panel(self.tool_window)

        self.info_window = newwin(10, self.max_x - self.tool_panel_size, self.max_y - self.info_panel_size, 0)
        box(self.info_window)
        self.info_panel = new_panel(self.info_window)
    def render(self):
        update_panels()
        doupdate()