from graphics import Line, Point
import time, random


class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

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
        else:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line, fill_color="white")
        if self.has_left_wall:
            line = Line(Point(x1,y2), Point(x1,y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y2), Point(x1,y1))
            self._win.draw_line(line, fill_color="white")
        if self.has_right_wall:
            line = Line(Point(x2,y2), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2,y2), Point(x2, y1))
            self._win.draw_line(line, fill_color="white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color="white")
    
    def draw_move(self, to_cell, undo=False):
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
        win=None,
        seed=None,
        speed=0.005
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._speed = speed
        self._create_cells()
        if seed != None:
            random.seed(seed)

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
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(self._speed)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        i = len(self._cells) -1
        j = len(self._cells[-1]) -1
        self._draw_cell(i, j)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        up = None
        down = None
        left = None
        right = None
        if j > 0:
            up = (i, j - 1)
        if j < len(self._cells[i]) - 1:
            down = (i, j + 1)
        if i > 0:
            left = (i - 1, j)
        if i < len(self._cells) - 1:
            right = (i + 1,j)
        while True:
            to_visit = []
            if up is not None:
                if self._cells[i][j - 1].visited == False:
                    to_visit.append("up")
            if down is not None:
                if self._cells[i][j + 1].visited == False:
                    to_visit.append("down")
            if left is not None:
                if self._cells[i - 1][j].visited == False:
                    to_visit.append("left")
            if right is not None:
                if self._cells[i + 1][j].visited == False:
                    to_visit.append("right")
            if to_visit == []:
                self._draw_cell(i, j)
                return
            else:
                direction = to_visit[random.randrange(0, len(to_visit))]
            if direction == "up":
                self._cells[i][j - 1].has_bottom_wall = False
                current.has_top_wall = False
                self._draw_cell(i, j - 1)
                self._break_walls_r(i , j - 1)
            elif direction == "down":
                self._cells[i][j + 1].has_top_wall = False
                current.has_bottom_wall = False
                self._draw_cell(i, j + 1)
                self._break_walls_r(i , j + 1)
            elif direction == "left":
                self._cells[i - 1][j].has_right_wall = False
                current.has_left_wall = False
                self._draw_cell(i - 1, j)
                self._break_walls_r(i - 1 , j)
            elif direction == "right":
                self._cells[i + 1][j].has_left_wall = False
                current.has_right_wall = False
                self._draw_cell(i + 1, j)
                self._break_walls_r(i + 1, j)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        self._reset_cells_visited()
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[-1][-1]:
            return True
        current = self._cells[i][j]
        up = None
        down = None
        left = None
        right = None
        if j > 0:
            up = self._cells[i][j - 1]
        if j < len(self._cells[i]) - 1:
            down = self._cells[i][j + 1]
        if i > 0:
            left = self._cells[i - 1][j]
        if i < len(self._cells) - 1:
            right = self._cells[i + 1][j]

        
        if up and not up.visited and (not current.has_top_wall or not up.has_bottom_wall):
            current.draw_move(up)
            if self._solve_r(i, j - 1):
                return True
            else:
                current.draw_move(up, undo=True)
        if down and not down.visited and (not current.has_bottom_wall or not down.has_top_wall):
            current.draw_move(down)
            if self._solve_r(i, j + 1):
                return True
            else:
                current.draw_move(down, undo=True)
        if left and not left.visited and (not current.has_left_wall or not left.has_right_wall):
            current.draw_move(left)
            if self._solve_r(i - 1, j):
                return True
            else:
                current.draw_move(left, undo=True)
        if right and not right.visited and (not current.has_right_wall or not right.has_left_wall):
            current.draw_move(right)
            if self._solve_r(i + 1, j):
                return True
            else:
                current.draw_move(right, undo=True)
        return False