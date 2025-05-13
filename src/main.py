from graphics import Window, Point, Line
from cell import Cell, Maze
from tkinter import Tk
import sys


def main():
    sys.setrecursionlimit(10000)
    win = Window(800, 600)
    # c1 = Cell(win)
    # c1.has_right_wall = False
    # c1.draw(50, 50, 100, 100)

    # c2 = Cell(win)
    # c2.has_left_wall = False
    # c2.has_bottom_wall = False
    # c2.draw(100, 50, 150, 100)

    # c1.draw_move(c2)

    # c3 = Cell(win)
    # c3.has_top_wall = False
    # c3.has_right_wall = False
    # c3.draw(100, 100, 150, 150)

    # c2.draw_move(c3)

    # c4 = Cell(win)
    # c4.has_left_wall = False
    # c4.draw(150, 100, 200, 150)

    # c3.draw_move(c4, True)

    m1 = Maze(x1=50, y1=70, num_rows=80, num_cols=80, cell_size_x=10, cell_size_y=10, win=win, seed=10, speed=0)
    m1._break_entrance_and_exit()
    m1._break_walls_r(0,0)
    m1.solve()
    win.wait_for_close()

main()