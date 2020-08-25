# IMPORTS
from functions import Sudoku
from gui_loop import *


# Declaration of sudoku board
Board = [   [2, 0, 0,   0, 3, 1,    0, 0, 6],
            [5, 0, 7,   4, 0, 8,    2, 3, 9],
            [0, 6, 0,   0, 0, 0,    4, 0, 7],

            [3, 4, 0,   2, 5, 0,    0, 0, 0],
            [0, 8, 1,   0, 0, 0,    6, 2, 5],
            [6, 5, 0,   0, 0, 7,    0, 4, 0],

            [9, 2, 0,   1, 7, 3,    0, 6, 4],
            [1, 0, 5,   6, 8, 0,    7, 0, 2],
            [4, 7, 0,   0, 2, 5,    3, 0, 0]]

# TESTS

# Transform a matrice into sudoku class
S1 = Sudoku(Board)
S1.printBoard()

S1.solve()

S1.printBoard()
