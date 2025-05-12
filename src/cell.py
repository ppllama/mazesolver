from graphics import Line, Point
import time


class Cell:
    def __init__(self, win):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def __repr__(self):
        return f"{self._x1, self._x2, self._y1, self._y2}"

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_bottom_wall:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line)
        if self.has_left_wall:
            line = Line(Point(x1,y2), Point(x1,y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2,y2), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
    
    def draw_move(self, to_cell, undo = False):
        fill_color = "red"
        if undo == True:
            fill_color = "gray"
        line = Line(Point(abs(self._x1 + self._x2) // 2, abs(self._y1 + self._y2) // 2), Point(abs(to_cell._x1 + to_cell._x2) // 2, abs(to_cell._y1 + to_cell._y2) // 2))
        self._win.draw_line(line, fill_color)



class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                row.append(cell)
            self._cells.append(row)
        
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
        
        print(self._cells)
        
    def _draw_cell(self, i, j):

        x1 = self._x1 + self._cell_size_x * i
        y1 = self._y1 + self._cell_size_y * j
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.005)