# IMPORTS
from functions import *

# TESTS

S1 = Sudoku(Board)
S1.printBoard()

while S1.isSolved() == False:
    fillPretendents(S1)

S1.printBoard()
