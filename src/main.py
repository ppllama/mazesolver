from graphics import Window, Point, Line
from tkinter import Tk

def main():
    win = Window(800, 600)
    p1 = Point(36, 55)
    p2 = Point(54, 234)
    p3 = Point(234, 235)
    l1 = Line(p1, p2)
    l2 = Line(p3, p2)
    l3 = Line(p1, p3)
    win.draw_line(l2, fill_color="red")
    win.draw_line(l3, fill_color="pink")

    win.draw_line(l1, fill_color="black")
    win.wait_for_close()

main()