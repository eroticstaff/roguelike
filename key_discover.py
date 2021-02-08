from unicurses import *

strscr = initscr()

while True:
    c = getch()
    mvaddstr(0,0,str(c))
    mvaddstr(0,30, f"The key {chr(c)} num is {c}")
    move(0,0)
