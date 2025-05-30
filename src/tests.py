import unittest
from cell import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 13
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertNotEqual(m1._cells[-1][-1].has_bottom_wall, True)

    def test_reset_cells_visited(self):
        num_cols = 25
        num_rows = 46
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._reset_cells_visited()
        self.assertEqual(m1._cells[3][15].visited, False)
        self.assertNotEqual(m1._cells[20][39].visited, True)
        self.assertEqual(m1._cells[0][0].visited, False)
        self.assertEqual(m1._cells[24][45].visited, False)
        self.assertEqual(m1._cells[10][5].visited, False)
        self.assertEqual(m1._cells[15][20].visited, False)
        self.assertEqual(m1._cells[8][30].visited, False)
        self.assertNotEqual(m1._cells[5][5].visited, True)
        self.assertNotEqual(m1._cells[20][40].visited, True)
        self.assertNotEqual(m1._cells[12][22].visited, True)
        self.assertNotEqual(m1._cells[17][1].visited, True)
        self.assertNotEqual(m1._cells[3][19].visited, True)


if __name__ == "__main__":
    unittest.main()